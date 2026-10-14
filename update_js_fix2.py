import re

css_file = 'style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Make ww-track position relative
css_content = re.sub(
    r'\.ww-track \{\n  display: flex;\n  align-items: center;',
    r'.ww-track {\n  display: flex;\n  align-items: center;\n  position: relative;',
    css_content
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

js_file = 'main.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

new_setPosition = '''  const setPositionByIndex = () => {
    updateDots();
    
    if (!slides[currentIndex]) return;
    
    requestAnimationFrame(() => {
      const wrapperWidth = track.parentElement.offsetWidth;
      const slide = slides[currentIndex];
      const slideLeft = slide.offsetLeft;
      const slideWidth = slide.offsetWidth;
      
      currentTranslate = -slideLeft + (wrapperWidth - slideWidth) / 2;
      prevTranslate = currentTranslate;
      
      track.style.transition = 'transform 0.5s cubic-bezier(0.25, 1, 0.5, 1)';
      track.style.transform = 	ranslateX(\px);
    });
  };'''

js_content = re.sub(
    r'  const setPositionByIndex = \(\) => \{.*?prevTranslate = currentTranslate;\s*\}\s*\};',
    lambda m: new_setPosition,
    js_content,
    flags=re.DOTALL
)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)
