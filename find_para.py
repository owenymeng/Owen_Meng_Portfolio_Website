import re

with open('index.html', 'r', encoding='utf8') as f:
    html = f.read()

# Let's find 5-2.jpg to see how it was styled
match_52 = re.search(r'.{0,150}5-2\.jpg.{0,150}', html)
if match_52:
    print("Found 5-2.jpg:")
    print(match_52.group(0))

# Let's find the paragraph
para_text = "Duolingo's leaderboard places users in competitive tiers against strangers."
match_para = re.search(r'.{0,150}' + re.escape(para_text) + r'.{0,300}', html, re.DOTALL)
if match_para:
    print("\nFound paragraph:")
    print(repr(match_para.group(0)))
