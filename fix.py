import re

with open('Portfolio.html', 'r', encoding='utf8') as f:
    html = f.read()

match = re.search(r'Mismatch 02.*?<\\u002Fdiv>', html, re.DOTALL)
if match:
    found_text = match.group(0)
    
    # We want to replace " · Figure A2" through the end of the <div class="m-screens"> block
    # so we just match " · Figure A2" to the end
    
    new_text = re.sub(
        r' · Figure A2<\\u002Fspan><span class=\\"i18n-zh\\">失配 02 · 排行榜 · 附图 A2<\\u002Fspan><\\u002Fspan>.*?<div class=\\"m-screens\\">.*?<\\u002Fdiv>',
        r'<\\u002Fspan><span class=\\"i18n-zh\\">失配 02 · 排行榜<\\u002Fspan><\\u002Fspan>',
        found_text,
        flags=re.DOTALL
    )
    
    if new_text != found_text:
        updated = html.replace(found_text, new_text)
        with open('Portfolio.html', 'w', encoding='utf8') as f:
            f.write(updated)
        print("Updated successfully!")
    else:
        print("Did not match the inner sub pattern.")
        print(found_text)
else:
    print("Could not find the block via regex.")
