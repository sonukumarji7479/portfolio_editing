import re

js_file = 'main.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

new_setPosition = '''  const setPositionByIndex = () => {
    updateDots();
    currentTranslate = currentIndex * -track.offsetWidth;
    prevTranslate = currentTranslate;
    track.style.transition = 'transform 0.5s cubic-bezier(0.25, 1, 0.5, 1)';
    setSliderPosition();
  };'''

js_content = re.sub(
    r'  const setPositionByIndex = \(\) => \{.*?setSliderPosition\(\);\s*\}\s*\};\s*\}\);',
    lambda m: new_setPosition,
    js_content,
    flags=re.DOTALL
)

# And let's fix the CSS regex too, just in case
css_file = 'style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content = re.sub(
    r'\.ww-slide \{\s*flex: 0 0 65%;.*?z-index: 2;\s*\}',
    r'.ww-slide {\n  min-width: 100%;\n  padding: 0;\n  box-sizing: border-box;\n}',
    css_content,
    flags=re.DOTALL
)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)
    
with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)
