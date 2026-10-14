import re

# 1. Restore HTML
html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

with open('webworks_temp.html', 'r', encoding='utf-8') as f:
    old_webworks_html = f.read()

html_content = re.sub(
    r'<section class="webworks".*?</section>',
    old_webworks_html,
    html_content,
    flags=re.DOTALL
)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

# 2. Restore CSS
css_file = 'style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

old_css = '''
.webworks-slider-wrapper {
  width: 100%;
  padding: 0;
  position: relative;
  overflow: hidden;
}
.webworks-scroll-container {
  white-space: nowrap;
  cursor: grab;
  scroll-behavior: auto;
  padding: 2rem 4rem 3.5rem;
  display: flex;
  overflow: auto hidden;
  scrollbar-width: none !important;
  -ms-overflow-style: none !important;
}
.webworks-scroll-container::-webkit-scrollbar {
  width: 0 !important;
  height: 0 !important;
  display: none !important;
}
.webworks-scroll-container.dragging {
  cursor: grabbing;
  -webkit-user-select: none;
  user-select: none;
}
.webworks-track {
  gap: 2.5rem;
  display: flex;
}
.webworks-card {
  background: var(--white);
  border: var(--border-subtle);
  border-radius: var(--card-radius);
  width: 420px;
  box-shadow: var(--shadow-soft);
  transition: border-color 0.4s var(--framer-ease), box-shadow 0.4s var(--framer-ease), transform 0.4s var(--framer-ease);
  will-change: transform, box-shadow, border-color;
  flex-direction: column;
  flex: 0 0 420px;
  gap: 1.5rem;
  padding: 1.5rem;
  display: flex;
}
.webworks-card:hover {
  border-color: #ff2e2e40;
  transform: translateY(-8px) scale(1.01);
  box-shadow: 0 25px 50px #0000000d, 0 5px 20px #ff2e2e08;
}
.webworks-mockup {
  aspect-ratio: 16/10;
  background: #0f0f15;
  border: 1px solid #ffffff0d;
  border-radius: 16px;
  width: 100%;
  position: relative;
  overflow: hidden;
  box-shadow: inset 0 1px 1px #ffffff1a;
}
.webworks-mockup-header {
  background: #ffffff08;
  border-bottom: 1px solid #ffffff0d;
  align-items: center;
  gap: 0.35rem;
  height: 28px;
  padding: 0 0.8rem;
  display: flex;
  position: relative;
}
.webworks-mockup-header .dot {
  border-radius: 50%;
  width: 6px;
  height: 6px;
  display: inline-block;
}
.webworks-mockup-header .dot.red { background: #ef4444; }
.webworks-mockup-header .dot.yellow { background: #eab308; }
.webworks-mockup-header .dot.green { background: #22c55e; }
.webworks-mockup-header .mockup-url {
  color: #ffffff59;
  letter-spacing: 0.02em;
  font-family: monospace;
  font-size: 0.62rem;
  font-weight: 500;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.webworks-mockup-body {
  width: 100%;
  height: calc(100% - 28px);
  position: relative;
  overflow: hidden;
}
.webworks-mockup-body img {
  object-fit: cover;
  object-position: top;
  width: 100%;
  height: 100%;
  transition: transform 1.2s cubic-bezier(0.16, 1, 0.3, 1);
}
.webworks-card:hover .webworks-mockup-body img {
  object-position: bottom;
  transform: scale(1.05);
}
.webworks-card-content {
  white-space: normal;
  flex-direction: column;
  gap: 0.75rem;
  display: flex;
}
.webworks-card-title {
  color: var(--text-color);
  letter-spacing: -0.01em;
  font-size: 1.4rem;
  font-weight: 700;
}
.webworks-card-desc {
  color: var(--text-light);
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  height: 72px;
  font-size: 0.9rem;
  line-height: 1.5;
  display: -webkit-box;
  overflow: hidden;
}
.webworks-card-desc p {
  color: var(--text-light);
  margin: 0;
  font-size: 0.9rem;
}
.webworks-card-footer {
  justify-content: flex-end;
  margin-top: 0.5rem;
  display: flex;
}
.webworks-btn {
  background: var(--white);
  color: var(--text-color);
  transition: all 0.3s var(--framer-ease);
  border: 1px solid #00000014;
  border-radius: 12px;
  align-items: center;
  gap: 0.5rem;
  padding: 0.7rem 1.4rem;
  font-size: 0.85rem;
  font-weight: 700;
  display: inline-flex;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 10px #00000005;
  text-decoration: none !important;
}
.webworks-btn:before {
  content: "";
  background: linear-gradient(90deg, #0000, #fff3, #0000);
  width: 100%;
  height: 100%;
  transition: left 0.6s;
  position: absolute;
  top: 0;
  left: -100%;
}
.webworks-btn:hover {
  background: var(--red-gradient);
  border-color: #0000;
  transform: translateY(-2px);
  box-shadow: 0 8px 20px #ff2e2e33;
  color: var(--white) !important;
}
.webworks-btn:hover:before {
  left: 100%;
}
.webworks-btn i {
  font-size: 0.95rem;
  transition: transform 0.3s;
}
.webworks-btn:hover i {
  transform: translate(2px, -2px);
}
.webworks-nav-btn {
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  color: #fff;
  cursor: pointer;
  z-index: 10;
  background: #ffffff1a;
  border: 1px solid #fff3;
  border-radius: 50%;
  justify-content: center;
  align-items: center;
  width: 50px;
  height: 50px;
  font-size: 1.5rem;
  transition: all 0.3s;
  display: flex;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
.webworks-nav-btn:hover {
  background: #ffffff40;
  transform: translateY(-50%) scale(1.1);
}
.webworks-nav-btn.prev-btn { left: 20px; }
.webworks-nav-btn.next-btn { right: 20px; }
@media (max-width: 768px) {
  .webworks-nav-btn {
    width: 40px;
    height: 40px;
    font-size: 1.2rem;
  }
  .webworks-nav-btn.prev-btn { left: 10px; }
  .webworks-nav-btn.next-btn { right: 10px; }
}
'''

css_content = re.sub(
    r'\.webworks-slider-wrapper \{.*?\.ww-nav-btn:active \{\n  transform: translateY\(0\);\n\}',
    old_css,
    css_content,
    flags=re.DOTALL
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

# 3. Restore JS
js_file = 'main.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js_content = f.read()

old_js = '''const initWebWorksScroll = () => {
    const container = document.querySelector('.webworks-scroll-container');
    const track = document.querySelector('.webworks-track');
    const prevBtn = document.querySelector('.webworks-nav-btn.prev-btn');
    const nextBtn = document.querySelector('.webworks-nav-btn.next-btn');

    if (!container || !track) return;

    let isDown = false;
    let startX;
    let scrollLeft;

    container.addEventListener('mousedown', (e) => {
        isDown = true;
        container.classList.add('dragging');
        startX = e.pageX - container.offsetLeft;
        scrollLeft = container.scrollLeft;
    });
    container.addEventListener('mouseleave', () => {
        isDown = false;
        container.classList.remove('dragging');
    });
    container.addEventListener('mouseup', () => {
        isDown = false;
        container.classList.remove('dragging');
    });
    container.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - container.offsetLeft;
        const walk = (x - startX) * 2; 
        container.scrollLeft = scrollLeft - walk;
    });

    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            container.scrollBy({ left: -420, behavior: 'smooth' });
        });
    }
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            container.scrollBy({ left: 420, behavior: 'smooth' });
        });
    }
};
document.addEventListener('DOMContentLoaded', initWebWorksScroll);'''

js_content = re.sub(
    r'const wwSliderInit = \(\) => \{.*?\};\n\ndocument\.addEventListener\(\'DOMContentLoaded\', wwSliderInit\);',
    old_js,
    js_content,
    flags=re.DOTALL
)

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)
