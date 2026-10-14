import re

js_file = 'main.js'

with open(js_file, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'// ==========================================\s*// Web Works Premium Showcase Scroller.*?(?=function initThumbnailsAnimations\(\) \{)', re.DOTALL)

new_js = '''// ==========================================
// Web Works Premium Featured Slider
// ==========================================

const wwSliderInit = () => {
  const track = document.querySelector('.ww-track');
  const slides = document.querySelectorAll('.ww-slide');
  const dots = document.querySelectorAll('.ww-pagination .ww-dot');
  const prevBtn = document.querySelector('.ww-nav-btn.prev');
  const nextBtn = document.querySelector('.ww-nav-btn.next');
  
  if (!track || slides.length === 0) return;

  let currentIndex = 0;
  const totalSlides = slides.length;
  let isDragging = false;
  let startPos = 0;
  let currentTranslate = 0;
  let prevTranslate = 0;
  let animationID = 0;

  const updateDots = () => {
    dots.forEach((dot, index) => {
      dot.classList.toggle('active', index === currentIndex);
    });
  };

  const setSliderPosition = () => {
    track.style.transform = 	ranslateX(\px);
  };

  const getPositionX = (event) => {
    return event.type.includes('mouse') ? event.pageX : event.touches[0].clientX;
  };

  const animation = () => {
    setSliderPosition();
    if (isDragging) requestAnimationFrame(animation);
  };

  const touchStart = (index) => {
    return function(event) {
      isDragging = true;
      currentIndex = index;
      startPos = getPositionX(event);
      animationID = requestAnimationFrame(animation);
      track.style.transition = 'none';
    }
  };

  const touchMove = (event) => {
    if (isDragging) {
      const currentPosition = getPositionX(event);
      currentTranslate = prevTranslate + currentPosition - startPos;
    }
  };

  const setPositionByIndex = () => {
    currentTranslate = currentIndex * -track.offsetWidth;
    prevTranslate = currentTranslate;
    track.style.transition = 'transform 0.5s cubic-bezier(0.25, 1, 0.5, 1)';
    setSliderPosition();
    updateDots();
  };

  const touchEnd = () => {
    isDragging = false;
    cancelAnimationFrame(animationID);
    
    const movedBy = currentTranslate - prevTranslate;
    
    if (movedBy < -100 && currentIndex < totalSlides - 1) currentIndex += 1;
    if (movedBy > 100 && currentIndex > 0) currentIndex -= 1;
    
    setPositionByIndex();
  };

  const goNext = () => {
    if (currentIndex < totalSlides - 1) {
      currentIndex++;
      setPositionByIndex();
    }
  };

  const goPrev = () => {
    if (currentIndex > 0) {
      currentIndex--;
      setPositionByIndex();
    }
  };

  slides.forEach((slide, index) => {
    // Touch events
    slide.addEventListener('touchstart', touchStart(index));
    slide.addEventListener('touchend', touchEnd);
    slide.addEventListener('touchmove', touchMove);
    
    // Mouse events
    slide.addEventListener('mousedown', touchStart(index));
    slide.addEventListener('mouseup', touchEnd);
    slide.addEventListener('mouseleave', () => { if (isDragging) touchEnd() });
    slide.addEventListener('mousemove', touchMove);
  });

  if (nextBtn) nextBtn.addEventListener('click', goNext);
  if (prevBtn) prevBtn.addEventListener('click', goPrev);
  
  dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
      currentIndex = index;
      setPositionByIndex();
    });
  });

  window.addEventListener('resize', setPositionByIndex);
  setTimeout(setPositionByIndex, 100);

  // GSAP Reveal
  gsap.from('.ww-card', {
    y: 60,
    opacity: 0,
    duration: 1.2,
    ease: "power4.out",
    scrollTrigger: {
      trigger: '.webworks-slider-wrapper',
      start: 'top 85%',
    }
  });
};

document.addEventListener('DOMContentLoaded', wwSliderInit);

'''

new_content = pattern.sub(lambda m: new_js, content)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(new_content)
