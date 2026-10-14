import re

js_file = 'main.js'

with open(js_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_updateDots = '''  const updateDots = () => {
    dots.forEach((dot, index) => {
      dot.classList.toggle('active', index === currentIndex);
    });
    slides.forEach((slide, index) => {
      slide.classList.toggle('active', index === currentIndex);
    });
  };'''

new_setPosition = '''  const setPositionByIndex = () => {
    updateDots();
    if (slides[currentIndex]) {
      const slide = slides[currentIndex];
      const slideWidth = slide.offsetWidth;
      const slideLeft = slide.offsetLeft;
      const wrapperWidth = track.parentElement.offsetWidth;
      currentTranslate = -slideLeft + (wrapperWidth - slideWidth) / 2;
    }
    prevTranslate = currentTranslate;
    track.style.transition = 'transform 0.5s cubic-bezier(0.25, 1, 0.5, 1)';
    setSliderPosition();
  };'''

content = re.sub(
    r'  const updateDots = \(\) => \{.*?  \};',
    new_updateDots,
    content,
    flags=re.DOTALL
)

content = re.sub(
    r'  const setPositionByIndex = \(\) => \{.*?updateDots\(\);\s*\};',
    new_setPosition,
    content,
    flags=re.DOTALL
)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(content)
