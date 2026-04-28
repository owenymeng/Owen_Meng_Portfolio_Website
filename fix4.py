import re

with open('Portfolio.html', 'r', encoding='utf8') as f:
    html = f.read()

para_match = re.search(r'(<p class=\\"body-text\\" style=\\"max-width: none;\\"><span class=\\"i18n-en\\">Duolingo\'s leaderboard places users in competitive tiers against strangers\..*?<\\u002Fp>)', html, re.DOTALL)

if para_match:
    found_para = para_match.group(1)
    
    img_div = r'''\n\n          <div style=\"margin: 2.5rem 0; border-radius: 12px; overflow: hidden; text-align: center;\">\n            <img src=\"5-2-new2.jpg\" alt=\"Duolingo Mismatch 02\" style=\"width: 100%; height: auto; display: block; margin: 0 auto;\">\n          <\u002Fdiv>\n'''
    
    new_text = found_para + img_div
    updated = html.replace(found_para, new_text)
    
    if html != updated:
        with open('Portfolio.html', 'w', encoding='utf8') as f:
            f.write(updated)
        print("Updated successfully!")
    else:
        print("Replacement did not change anything.")
else:
    print("Paragraph not found.")

