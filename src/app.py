# -*- coding: utf-8 -*-
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>My Sample Webapp</title>
    <style>
      :root {
        --bg: #0e0f14;
        --bg2: #141725;
        --card: #1a1f32;
        --text: #e7e9f0;
        --muted: #a5adc6;
        --accent: #7ee787;
        --accent2: #7ab0ff;
      }
      * { box-sizing: border-box; }
      body {
        margin: 0;
        font-family: "Space Grotesk", "Segoe UI", sans-serif;
        color: var(--text);
        background: radial-gradient(1200px 600px at 10% -10%, #1b2340 0%, transparent 60%),
                    radial-gradient(900px 500px at 90% 10%, #102a2a 0%, transparent 55%),
                    linear-gradient(180deg, var(--bg), var(--bg2));
      }
      .wrap { max-width: 980px; margin: 0 auto; padding: 48px 24px 80px; position: relative; }
      .corner-img { position: absolute; top: 24px; right: 24px; width: 180px; height: auto; opacity: 0.95; z-index: 2; filter: drop-shadow(0 10px 24px rgba(0,0,0,0.35)); }
      header { display: flex; flex-direction: column; gap: 16px; }
      .badge { color: var(--accent); font-weight: 600; letter-spacing: .08em; text-transform: uppercase; font-size: 12px; }
      h1 { font-size: clamp(36px, 6vw, 64px); margin: 0; line-height: 1.05; }
      .subtitle { color: var(--muted); font-size: 18px; max-width: 720px; }
      .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-top: 32px; }
      .card { background: var(--card); border: 1px solid #262c45; padding: 20px; border-radius: 14px; }
      .card h3 { margin: 0 0 8px; font-size: 18px; }
      .card p { margin: 0; color: var(--muted); }
      .section { margin-top: 48px; }
      .section h2 { margin: 0 0 12px; font-size: 22px; }
      .pill { display: inline-block; padding: 6px 10px; background: #232a44; border-radius: 999px; font-size: 12px; color: var(--muted); margin: 6px 6px 0 0; }
      .cta { display: inline-block; margin-top: 16px; padding: 10px 14px; background: var(--accent2); color: #0e0f14; border-radius: 10px; text-decoration: none; font-weight: 600; }
      .gallery { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; }
      .gallery img { width: 100%; height: 160px; object-fit: cover; border-radius: 12px; border: 1px solid #262c45; background: #0b1320; }
      footer { margin-top: 64px; color: var(--muted); font-size: 12px; }
    </style>
  </head>
  <body>
    <div class="wrap">
      <header>\r\n        <img class="corner-img" src="/static/images/mountain-ridge.svg" alt="Mountain ridge" />\r\n        <div class="badge">Personal website</div>
        <h1>My Sample Webapp</h1>
        <div class="subtitle">
          A dark, modern home for our work, ideas, and collaborations.
        </div>
      </header>

      <div class="grid">
        <div class="card">
          <h3>About</h3>
          <p>Two builders focused on thoughtful products, clean code, and meaningful outcomes.</p>
        </div>
        <div class="card">
          <h3>Projects</h3>
          <p>Selected work across web, automation, and cloud-native systems.</p>
        </div>
        <div class="card">
          <h3>Writing</h3>
          <p>Notes on engineering, design, and the craft of shipping.</p>
        </div>
        <div class="card">
          <h3>Contact</h3>
          <p>Open to collaborations, speaking, and thoughtful problem solving.</p>
        </div>
      </div>

      <div class="section">
        <h2>Focus Areas</h2>
        <span class="pill">Backend & APIs</span>
        <span class="pill">Cloud & DevOps</span>
        <span class="pill">Data & Automation</span>
        <span class="pill">Product Design</span>
      </div>

      <div class="section">
        <h2>Latest</h2>
        <p class="subtitle">Add short updates here: launches, new posts, or milestones.</p>
        <a class="cta" href="#">See what we're building</a>
      </div>

      <div class="section">
        <h2>Nature Gallery</h2>
        <div class="gallery">
          <img src="/static/images/mountain-lake.svg" alt="Mountain lake" />
          <img src="/static/images/mountain-ridge.svg" alt="Mountain ridge" />
          <img src="/static/images/mountain-dawn.svg" alt="Mountain dawn" />
          <img src="/static/images/mountain-night.svg" alt="Mountain night" />
        </div>
      </div>

      <footer>
        (c) 2026 My Sample Webapp. All rights reserved.
      </footer>
    </div>
  </body>
</html>
"""

@app.get("/")
def index():
    return render_template_string(HTML)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
















