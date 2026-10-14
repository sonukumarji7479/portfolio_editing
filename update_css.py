import re

css_file = 'style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_css = '''
.webworks-slider-wrapper {
  width: 100%;
  max-width: 1000px;
  margin: 0 auto;
  overflow: hidden;
  position: relative;
  border-radius: 24px;
}

.ww-track {
  display: flex;
  transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1);
  cursor: grab;
}

.ww-track:active {
  cursor: grabbing;
}

.ww-slide {
  min-width: 100%;
  padding: 0;
  box-sizing: border-box;
}

.ww-card {
  background: #fff;
  border-radius: 24px;
  padding: 1.5rem;
  box-shadow: 0 20px 40px rgba(0,0,0,0.08);
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.ww-mockup {
  width: 100%;
  aspect-ratio: 16/10;
  border-radius: 16px;
  overflow: hidden;
  background: #0f0f15;
  position: relative;
}

.ww-drag-tooltip {
  position: absolute;
  top: 1.5rem;
  left: 1.5rem;
  background: #333a45;
  color: #fff;
  padding: 0.5rem 1.2rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  display: flex;
  align-items: center;
  gap: 0.7rem;
  z-index: 10;
  pointer-events: none;
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}

.ww-mockup img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top;
}

.ww-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 0.5rem;
}

.ww-title-area {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.ww-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.ww-title-area h3 {
  font-size: 1.6rem;
  font-weight: 800;
  color: #1a1a2e;
  margin: 0;
  letter-spacing: -0.03em;
}

.ww-tags {
  display: flex;
  gap: 0.6rem;
}

.ww-pill {
  padding: 0.4rem 1rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  white-space: nowrap;
}

a.ww-pill {
  background: #fff0eb;
  color: #ff5722;
  transition: background 0.3s;
}

a.ww-pill:hover {
  background: #ffd6c9;
}

span.ww-pill.outline {
  border: 1px solid #e2e8f0;
  color: #64748b;
}

/* Controls */
.ww-controls {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  margin-top: 2rem;
}

.ww-pagination {
  display: flex;
  gap: 0.6rem;
}

.ww-pagination .ww-dot {
  width: 28px;
  height: 6px;
  border-radius: 6px;
  background: #89b4f8;
  opacity: 0.6;
  transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
  cursor: pointer;
}

.ww-pagination .ww-dot:hover {
  opacity: 0.9;
}

.ww-pagination .ww-dot.active {
  background: #ff3d00;
  opacity: 1;
  width: 40px;
}

.ww-nav-buttons {
  display: flex;
  gap: 1rem;
}

.ww-nav-btn {
  width: 56px;
  height: 56px;
  border-radius: 20px;
  background: #fff;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  color: #1a1a2e;
  cursor: pointer;
  box-shadow: 0 8px 24px rgba(0,0,0,0.06);
  transition: all 0.2s cubic-bezier(0.25, 1, 0.5, 1);
}

.ww-nav-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.1);
}

.ww-nav-btn:active {
  transform: translateY(0);
}
'''

# Delete lines 3515 to 3751 and replace with new_css
del lines[3515:3752]
lines.insert(3515, new_css + '\n')

with open(css_file, 'w', encoding='utf-8') as f:
    f.writelines(lines)
