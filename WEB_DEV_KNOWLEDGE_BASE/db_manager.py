import sys
import io
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass
"""
Web Development Knowledge Base Database & Query Engine
Manages SQLite database with FTS5 Full-Text Search for all web dev markdown docs.
"""

import os
import re
import sys
import json
import sqlite3
import datetime
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "web_dev_knowledge.db"

CATEGORY_MAP = {
    "00": "Index & Quick Reference",
    "01": "UI/UX & Design Systems",
    "02": "Frontend Frameworks",
    "03": "Backend Frameworks",
    "04": "CSS & Styling",
    "05": "Typography & Fonts",
    "06": "Icons & Illustrations",
    "07": "Animations & Motion",
    "08": "3D Graphics & WebGL",
    "09": "Databases & ORM",
    "10": "Authentication & Security",
    "11": "State Management",
    "12": "Testing & QA",
    "13": "Build Tools & Bundlers",
    "14": "Performance & CWV",
    "15": "Accessibility (A11y)",
    "16": "SEO & Analytics",
    "17": "Deployment & DevOps",
    "18": "APIs & WebSockets",
    "19": "Component Libraries",
    "20": "Color & Design Tokens",
    "21": "UI Components (Deep-Dive)",
    "22": "Scroll & Animation Libs",
    "23": "Icons & Fonts (Exhaustive)",
    "24": "Forms & File Uploads",
    "25": "E-Commerce & Payments",
    "26": "i18n & Localization & RTL",
    "27": "AI Integration & Generative UI",
    "README": "Master Directory & Guides",
}

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def parse_markdown(filepath: Path):
    text = filepath.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    
    title = filepath.stem
    description = ""
    
    # Extract title from first # heading
    for line in lines:
        if line.startswith("# "):
            title = line.replace("# ", "").strip()
            break
            
    # Extract description from > quote or first paragraph
    for line in lines:
        if line.startswith("> "):
            description = line.replace("> ", "").strip()
            break
            
    prefix = filepath.stem.split("_")[0]
    category = CATEGORY_MAP.get(prefix, "General Web Development")
    
    # Extract sections
    sections = []
    current_heading = "Introduction"
    current_level = 1
    current_lines = []
    
    for line in lines:
        match = re.match(r"^(#{2,4})\s+(.+)$", line)
        if match:
            if current_lines:
                sections.append((current_heading, current_level, "\n".join(current_lines).strip()))
                current_lines = []
            current_level = len(match.group(1))
            current_heading = match.group(2).strip()
        else:
            current_lines.append(line)
    if current_lines:
        sections.append((current_heading, current_level, "\n".join(current_lines).strip()))

    tags = []
    tag_keywords = [
        "react", "vue", "angular", "svelte", "nextjs", "tailwind", "css", "animation",
        "gsap", "framer", "3d", "threejs", "postgres", "prisma", "drizzle", "auth",
        "jwt", "clerk", "zustand", "redux", "vitest", "playwright", "vite", "docker",
        "seo", "accessibility", "wcag", "stripe", "i18n", "ai", "icons", "fonts"
    ]
    lower_text = text.lower()
    for kw in tag_keywords:
        if kw in lower_text:
            tags.append(kw)
            
    return {
        "filename": filepath.name,
        "title": title,
        "category": category,
        "description": description,
        "tags": ", ".join(tags),
        "content": text,
        "sections": sections,
        "size_bytes": len(text.encode("utf-8")),
    }

def init_database():
    conn = get_db()
    cur = conn.cursor()
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        tags TEXT,
        content TEXT NOT NULL,
        size_bytes INTEGER,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        article_id INTEGER NOT NULL,
        heading TEXT NOT NULL,
        level INTEGER NOT NULL,
        content TEXT NOT NULL,
        FOREIGN KEY(article_id) REFERENCES articles(id) ON DELETE CASCADE
    );
    """)
    
    # Check if FTS5 is available
    try:
        cur.execute("DROP TABLE IF EXISTS articles_fts;")
        cur.execute("""
        CREATE VIRTUAL TABLE articles_fts USING fts5(
            filename,
            title,
            category,
            description,
            tags,
            content,
            content='articles',
            content_rowid='id'
        );
        """)
        
        cur.execute("DROP TABLE IF EXISTS sections_fts;")
        cur.execute("""
        CREATE VIRTUAL TABLE sections_fts USING fts5(
            heading,
            content,
            content='sections',
            content_rowid='id'
        );
        """)
        has_fts = True
    except sqlite3.OperationalError:
        has_fts = False
        print("[WARN] SQLite FTS5 extension not compiled in standard build, falling back to LIKE index.")

    cur.execute("DELETE FROM sections;")
    cur.execute("DELETE FROM articles;")

    md_files = sorted(list(BASE_DIR.glob("*.md")))
    inserted_count = 0
    
    for f in md_files:
        data = parse_markdown(f)
        cur.execute("""
        INSERT INTO articles (filename, title, category, description, tags, content, size_bytes, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["filename"],
            data["title"],
            data["category"],
            data["description"],
            data["tags"],
            data["content"],
            data["size_bytes"],
            datetime.datetime.now().isoformat()
        ))
        article_id = cur.lastrowid
        
        for heading, level, scontent in data["sections"]:
            cur.execute("""
            INSERT INTO sections (article_id, heading, level, content)
            VALUES (?, ?, ?, ?)
            """, (article_id, heading, level, scontent))
            section_id = cur.lastrowid
            if has_fts:
                cur.execute("INSERT INTO sections_fts (rowid, heading, content) VALUES (?, ?, ?)",
                            (section_id, heading, scontent))
                            
        if has_fts:
            cur.execute("""
            INSERT INTO articles_fts (rowid, filename, title, category, description, tags, content)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (article_id, data["filename"], data["title"], data["category"],
                  data["description"], data["tags"], data["content"]))
                  
        inserted_count += 1
        
    conn.commit()
    conn.close()
    print(f"[SUCCESS] Ingested {inserted_count} Markdown files into {DB_PATH.name}")

def search_articles(query: str, limit: int = 5):
    conn = get_db()
    cur = conn.cursor()
    
    # Try FTS5 first
    try:
        sql = """
        SELECT a.id, a.filename, a.title, a.category, snippet(articles_fts, 5, '==[', ']==', '...', 20) as matched_snippet,
               bm25(articles_fts) as rank
        FROM articles_fts
        JOIN articles a ON a.id = articles_fts.rowid
        WHERE articles_fts MATCH ?
        ORDER BY rank
        LIMIT ?;
        """
        cur.execute(sql, (query, limit))
        rows = cur.fetchall()
        if rows:
            return [dict(r) for r in rows]
    except sqlite3.OperationalError:
        pass
        
    # Fallback to standard LIKE
    like_term = f"%{query}%"
    sql = """
    SELECT id, filename, title, category, SUBSTR(content, INSTR(LOWER(content), LOWER(?)), 150) as matched_snippet, 0 as rank
    FROM articles
    WHERE title LIKE ? OR content LIKE ? OR tags LIKE ?
    LIMIT ?;
    """
    cur.execute(sql, (query, like_term, like_term, like_term, limit))
    return [dict(r) for r in cur.fetchall()]

def search_sections(query: str, limit: int = 5):
    conn = get_db()
    cur = conn.cursor()
    like_term = f"%{query}%"
    sql = """
    SELECT s.heading, a.filename, a.title, s.content
    FROM sections s
    JOIN articles a ON a.id = s.article_id
    WHERE s.heading LIKE ? OR s.content LIKE ?
    LIMIT ?;
    """
    cur.execute(sql, (like_term, like_term, limit))
    return [dict(r) for r in cur.fetchall()]

def list_articles():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, filename, title, category, size_bytes FROM articles ORDER BY filename ASC;")
    return [dict(r) for r in cur.fetchall()]

def get_article(identifier: str):
    conn = get_db()
    cur = conn.cursor()
    if identifier.isdigit():
        cur.execute("SELECT * FROM articles WHERE id = ?;", (int(identifier),))
    else:
        cur.execute("SELECT * FROM articles WHERE filename LIKE ? OR title LIKE ? LIMIT 1;", 
                    (f"%{identifier}%", f"%{identifier}%"))
    row = cur.fetchone()
    return dict(row) if row else None

RECOMMENDATIONS = {
    "portfolio": [
        ("01_UI_UX_DESIGN.md", "Design systems, layout hierarchy, dark mode"),
        ("02_FRONTEND_FRAMEWORKS.md", "Astro or Next.js for high performance"),
        ("04_CSS_STYLING.md", "Tailwind CSS styling"),
        ("07_ANIMATIONS_MOTION.md", "Framer Motion & GSAP animations"),
        ("08_3D_GRAPHICS_WEBGL.md", "Three.js / React Three Fiber interactive 3D hero"),
        ("17_DEPLOYMENT_DEVOPS.md", "Vercel / Cloudflare zero-cost global edge deploy")
    ],
    "saas": [
        ("02_FRONTEND_FRAMEWORKS.md", "Next.js App Router full-stack"),
        ("09_DATABASE_ORM.md", "PostgreSQL + Prisma / Drizzle ORM"),
        ("10_AUTH_SECURITY.md", "Clerk / Auth.js authentication & sessions"),
        ("11_STATE_MANAGEMENT.md", "Zustand + TanStack Query"),
        ("19_COMPONENT_LIBRARIES.md", "shadcn/ui + Radix primitives"),
        ("24_FORMS_VALIDATION_UPLOADS.md", "React Hook Form + Zod validation"),
        ("25_ECOMMERCE_PAYMENTS.md", "Stripe subscriptions & webhook listeners"),
        ("27_AI_INTEGRATION_LLM_UI.md", "Vercel AI SDK integration")
    ],
    "ecommerce": [
        ("02_FRONTEND_FRAMEWORKS.md", "Next.js e-commerce storefront"),
        ("25_ECOMMERCE_PAYMENTS.md", "Stripe Checkout, cart state, webhooks"),
        ("09_DATABASE_ORM.md", "PostgreSQL product catalog & inventory"),
        ("16_SEO_ANALYTICS.md", "Product Schema JSON-LD & meta tags"),
        ("14_PERFORMANCE.md", "Image optimization with Sharp & WebP for conversions")
    ],
    "landing": [
        ("01_UI_UX_DESIGN.md", "Bento grid, glassmorphism & visual balance"),
        ("07_ANIMATIONS_MOTION.md", "ScrollTrigger & stagger animations"),
        ("19_COMPONENT_LIBRARIES.md", "Aceternity UI / Magic UI animated cards"),
        ("14_PERFORMANCE.md", "Sub-second LCP & Core Web Vitals"),
        ("16_SEO_ANALYTICS.md", "OpenGraph previews for viral sharing")
    ]
}

def recommend(use_case: str):
    use_case = use_case.lower().strip()
    for key, items in RECOMMENDATIONS.items():
        if key in use_case:
            return items
    # default general recommendation
    return RECOMMENDATIONS["saas"]

class KnowledgeServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)
        
        if parsed.path == "/api/search":
            q = qs.get("q", [""])[0]
            limit = int(qs.get("limit", [10])[0])
            results = search_articles(q, limit=limit) if q else []
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(results, indent=2).encode("utf-8"))
            return
            
        elif parsed.path == "/api/list":
            items = list_articles()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(items, indent=2).encode("utf-8"))
            return
            
        elif parsed.path == "/api/get":
            file_id = qs.get("id", [""])[0]
            article = get_article(file_id)
            self.send_response(200 if article else 404)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(article or {"error": "Not found"}).encode("utf-8"))
            return
            
        # Serve simple HTML search UI
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <title>Web Dev Knowledge Base Database</title>
          <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="bg-slate-900 text-slate-100 min-h-screen p-8">
          <div class="max-w-4xl mx-auto">
            <h1 class="text-3xl font-bold mb-2 text-blue-400">🌐 Web Dev Knowledge Base Database</h1>
            <p class="text-slate-400 mb-6">Real-time SQLite FTS5 search across all 28 curated web development guides.</p>
            
            <div class="flex gap-2 mb-8">
              <input id="search-box" type="text" placeholder="Search (e.g. tailwind, animation, auth, postgres, threejs)..." 
                     class="flex-1 px-4 py-3 bg-slate-800 border border-slate-700 rounded-lg outline-none focus:border-blue-500 text-white"/>
              <button onclick="doSearch()" class="px-6 py-3 bg-blue-600 hover:bg-blue-500 rounded-lg font-medium transition">Search</button>
            </div>
            
            <div id="results" class="space-y-4"></div>
          </div>
          
          <script>
            async function doSearch() {
              const q = document.getElementById('search-box').value;
              const res = await fetch('/api/search?q=' + encodeURIComponent(q));
              const data = await res.json();
              const container = document.getElementById('results');
              if (data.length === 0) {
                container.innerHTML = '<p class="text-slate-500">No results found.</p>';
                return;
              }
              container.innerHTML = data.map(item => `
                <div class="p-4 bg-slate-800/80 border border-slate-700 rounded-xl hover:border-blue-500/50 transition">
                  <div class="flex justify-between items-start mb-1">
                    <h2 class="text-lg font-semibold text-blue-300">${item.title}</h2>
                    <span class="text-xs px-2 py-1 bg-blue-900/60 text-blue-300 rounded">${item.category}</span>
                  </div>
                  <p class="text-xs text-slate-400 font-mono mb-2">${item.filename}</p>
                  <p class="text-sm text-slate-300">${item.matched_snippet || ''}</p>
                </div>
              `).join('');
            }
            document.getElementById('search-box').addEventListener('keypress', (e) => {
              if (e.key === 'Enter') doSearch();
            });
            doSearch();
          </script>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

def print_help():
    print("""
🌐 Web Development Knowledge Base CLI
-------------------------------------
Usage:
  python db_manager.py init             -> Ingests/updates all .md files into SQLite
  python db_manager.py list             -> Lists all stored documents
  python db_manager.py search <query>   -> Full-text search with relevance ranking
  python db_manager.py section <query>  -> Search specific headings and code sections
  python db_manager.py get <id/file>    -> View full markdown of document
  python db_manager.py recommend <type> -> Recommends tools for: portfolio, saas, ecommerce, landing
  python db_manager.py serve [port]     -> Launch local HTTP API & Search Web UI (default: 5050)
    """)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(0)
        
    cmd = sys.argv[1].lower()
    
    if cmd == "init":
        init_database()
    elif cmd == "list":
        articles = list_articles()
        print(f"\n📚 Total Articles in Database: {len(articles)}\n")
        print(f"{'ID':<4} | {'Filename':<32} | {'Category':<28} | {'Size'}")
        print("-" * 80)
        for a in articles:
            size_kb = f"{a['size_bytes'] / 1024:.1f} KB"
            print(f"{a['id']:<4} | {a['filename']:<32} | {a['category']:<28} | {size_kb}")
    elif cmd == "search":
        if len(sys.argv) < 3:
            print("Please provide a search query.")
            sys.exit(1)
        q = " ".join(sys.argv[2:])
        results = search_articles(q)
        print(f"\n🔍 Search Results for '{q}': {len(results)} found\n")
        for r in results:
            print(f"[{r['id']}] {r['title']} ({r['filename']})")
            print(f"    Category: {r['category']}")
            snippet = r.get('matched_snippet', '').replace('\n', ' ')
            print(f"    Snippet:  {snippet[:180]}...\n")
    elif cmd == "section":
        if len(sys.argv) < 3:
            print("Please provide a section query.")
            sys.exit(1)
        q = " ".join(sys.argv[2:])
        results = search_sections(q)
        print(f"\n📑 Section Results for '{q}':\n")
        for r in results:
            print(f"• [{r['filename']}] {r['heading']}")
            preview = r['content'][:150].replace('\n', ' ')
            print(f"  {preview}...\n")
    elif cmd == "get":
        if len(sys.argv) < 3:
            print("Please specify an ID or filename.")
            sys.exit(1)
        art = get_article(sys.argv[2])
        if art:
            print(f"\n==========================================")
            print(f"📄 {art['title']}")
            print(f"📁 {art['filename']} | Category: {art['category']}")
            print(f"🏷️  Tags: {art['tags']}")
            print(f"==========================================\n")
            print(art['content'])
        else:
            print("Document not found.")
    elif cmd == "recommend":
        uc = sys.argv[2] if len(sys.argv) > 2 else "saas"
        rec = recommend(uc)
        print(f"\n🎯 Recommended Stack & Files for: {uc.upper()}\n")
        for fn, why in rec:
            print(f"  • {fn:<32} -> {why}")
        print()
    elif cmd == "serve":
        port = int(sys.argv[2]) if len(sys.argv) > 2 else 5050
        server = HTTPServer(("127.0.0.1", port), KnowledgeServer)
        print(f"\n🚀 Knowledge Base Server running at: http://127.0.0.1:{port}")
        print("Press Ctrl+C to stop.")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server.")
    else:
        print_help()

