import re

with open('Portfolio.html', 'r', encoding='utf8') as f:
    html = f.read()

# We need to find the exact end of that paragraph.
para_start = "Duolingo's leaderboard places users in competitive tiers against strangers."
para_match = re.search(r'(<p class=\\"body-text\\" style=\\"max-width: none;\\"><span class=\\"i18n-en\\">Duolingo\'s leaderboard places users in competitive tiers against strangers\..*?<\\u002Fp>)', html, re.DOTALL)

if para_match:
    found_para = para_match.group(1)
    
    # We will insert the new 5-2-new.jpg div right after found_para
    # The user asked for "图片比例参考5-2.jpg 图片要居中". 
    # Let's use:
    # <div style="margin: 2.5rem 0; border-radius: 12px; overflow: hidden; text-align: center;">
    #   <img src="5-2-new.jpg" style="width: 100%; height: auto; display: block; margin: 0 auto;">
    # </div>
    
    img_div = r'''\n\n          <div style=\"margin: 2.5rem 0; border-radius: 12px; overflow: hidden; text-align: center;\">\n            <img src=\"5-2-new.jpg\" alt=\"Duolingo Mismatch 02\" style=\"width: 100%; height: auto; display: block; margin: 0 auto;\">\n          <\u002Fdiv>\n'''
    
    new_text = found_para + img_div
    updated = html.replace(found_para, new_text)
    
    if html != updated:
        with open('Portfolio.html', 'w', encoding='utf8') as f:
            f.write(updated)
        print("Updated!")
    else:
        print("Replacement did not change anything.")
else:
    print("Paragraph not found.")

