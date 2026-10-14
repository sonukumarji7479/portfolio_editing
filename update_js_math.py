import re

js_file = 'main.js'

with open(js_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_setPosition = '''  const setPositionByIndex = () => {
    updateDots();
    
    // Using percentage math for perfectly centered coverflow (65% slide width)
    const slidePercent = 65;
    const centerOffset = (100 - slidePercent) / 2;
    const translatePercent = -(currentIndex * slidePercent) + centerOffset;
    
    track.style.transition = 'transform 0.5s cubic-bezier(0.25, 1, 0.5, 1)';
    track.style.transform = 	ranslateX(\%);
    
    // Also keep the pixel vars updated in case dragging is used
    if (track.parentElement) {
      const wrapperWidth = track.parentElement.offsetWidth;
      currentTranslate = (translatePercent / 100) * wrapperWidth;
      prevTranslate = currentTranslate;
    }
  };'''

content = re.sub(
    r'  const setPositionByIndex = \(\) => \{.*?setSliderPosition\(\);\s*\};',
    new_setPosition,
    content,
    flags=re.DOTALL
)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(content)
