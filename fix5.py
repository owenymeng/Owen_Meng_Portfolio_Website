import re

with open('Portfolio.html', 'r', encoding='utf8') as f:
    html = f.read()

# Find and replace the added image div for 5-2-new2.jpg
pattern = r'\\n\\n\s*<div style=\\"margin: 2.5rem 0; border-radius: 12px; overflow: hidden; text-align: center;\\">\\n\s*<img src=\\"5-2-new2\.jpg\\" alt=\\"Duolingo Mismatch 02\\" style=\\"width: 100%; height: auto; display: block; margin: 0 auto;\\">\\n\s*<\\u002Fdiv>\\n'

updated = re.sub(pattern, '', html)

if html != updated:
    with open('Portfolio.html', 'w', encoding='utf8') as f:
        f.write(updated)
    print("Deleted successfully!")
else:
    print("Could not find the exact pattern.")
    
