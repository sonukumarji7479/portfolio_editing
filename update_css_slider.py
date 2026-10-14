import re

css_file = 'style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Update CSS
content = re.sub(
    r'\.webworks-slider-wrapper \{\s*width: 100%;\s*max-width: 1000px;',
    r'.webworks-slider-wrapper {\n  width: 100%;\n  max-width: 100vw;',
    content
)

content = re.sub(
    r'\.ww-track \{\s*display: flex;',
    r'.ww-track {\n  display: flex;\n  align-items: center;',
    content
)

content = re.sub(
    r'\.ww-slide \{\s*min-width: 100%;\s*padding: 0;\s*box-sizing: border-box;\s*\}',
    r'.ww-slide {\n  flex: 0 0 65%;\n  max-width: 900px;\n  min-width: unset;\n  padding: 0 1rem;\n  box-sizing: border-box;\n  opacity: 0.4;\n  transform: scale(0.85);\n  transition: all 0.5s cubic-bezier(0.25, 1, 0.5, 1);\n  pointer-events: none;\n}\n\n.ww-slide.active {\n  opacity: 1;\n  transform: scale(1);\n  pointer-events: auto;\n  z-index: 2;\n}',
    content
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(content)
