import re

# 1. Restore JS
with open('main.js', 'r', encoding='utf-8') as f:
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

js_content = re.sub(r'const wwSliderInit = \(\) => \{.*?\};\n\n(?:document\.addEventListener\(\'DOMContentLoaded\', wwSliderInit\);)?', old_js, js_content, flags=re.DOTALL)
with open('main.js', 'w', encoding='utf-8') as f:
    f.write(js_content)


# 2. Restore CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

with open('restore_full.py', 'r', encoding='utf-8') as f:
    restore_content = f.read()

old_css = restore_content.split("old_css = '''")[1].split("'''")[0]

css_content = re.sub(r'\.webworks-slider-wrapper \{.*?\.ww-nav-btn:active \{\n  transform: translateY\(0\);\n\}', old_css, css_content, flags=re.DOTALL)
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Restored JS and CSS")
