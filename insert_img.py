import re

with open('index.html', 'r', encoding='utf8') as f:
    html = f.read()

pattern = r'(<span class=\\"i18n-zh\\">多邻国的排行榜将用户置于与陌生人的竞争层级中。设计初衷是提供社交激励——看到他人学习应能激励你学得更多。但对于许多用户来说，实际情感结果是竞争焦虑：被迫与那些学习步调、目标和时间表完全不同的陌生人赛跑。<\\u002Fspan><\\u002Fp>)'

replacement = r'\1\\n\\n          <div style=\\"margin: 2.5rem 0; border-radius: 12px; overflow: hidden; background-color: #fafafa; padding: 2rem;\\">\\n            <img src=\\"5-2-new.jpg\\" alt=\\"Duolingo Leaderboard Mismatch\\" style=\\"width: 100%; height: auto; display: block;\\">\\n          <\\u002Fdiv>'

new_html = re.sub(pattern, replacement, html)

if new_html != html:
    with open('index.html', 'w', encoding='utf8') as f:
        f.write(new_html)
    print("Inserted successfully!")
else:
    print("Could not find paragraph!")
