import re

css_file = 'style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content = re.sub(
    r'\.webworks-slider-wrapper \{\n  width: 100%;\n  max-width: 100vw;',
    r'.webworks-slider-wrapper {\n  width: 100%;\n  max-width: 1000px;',
    css_content
)

css_content = re.sub(
    r'\.ww-track \{\n  display: flex;\n  align-items: center;\n  position: relative;',
    r'.ww-track {\n  display: flex;\n  align-items: center;',
    css_content
)

css_content = re.sub(
    r'\.ww-slide \{\n  flex: 0 0 65%;\n  max-width: 900px;\n  min-width: unset;\n  padding: 0 1rem;\n  box-sizing: border-box;\n  opacity: 0.4;\n  transform: scale\(0\.85\);\n  transition: all 0\.5s cubic-bezier\(0\.25, 1, 0\.5, 1\);\n  pointer-events: none;\n\}\n\n\.ww-slide\.active \{\n  opacity: 1;\n  transform: scale\(1\);\n  pointer-events: auto;\n  z-index: 2;\n\}',
    r'.ww-slide {\n  min-width: 100%;\n  padding: 0;\n  box-sizing: border-box;\n}',
    css_content
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

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
    r'  const setPositionByIndex = \(\) => \{.*?prevTranslate = currentTranslate;\s*\n\s*track\.style\.transition = \'transform 0\.5s cubic-bezier\(0\.25, 1, 0\.5, 1\)\';\s*\n\s*track\.style\.transform = 	ranslateX\(\$\{\s*currentTranslate\s*\}px\).*?\}\);\s*\};',
    new_setPosition,
    js_content,
    flags=re.DOTALL
)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)
