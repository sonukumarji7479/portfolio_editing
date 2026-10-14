import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'<!-- Custom Cursor -->\s*<div class="custom-cursor figma-cursor">.*?<div class="cursor-label">You</div>\s*</div>'

if re.search(pattern, html, re.DOTALL):
    html = re.sub(pattern, '', html, flags=re.DOTALL)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Removed cursor successfully')
else:
    print('Pattern not found')
