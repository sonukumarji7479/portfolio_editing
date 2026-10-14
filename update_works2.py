with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace(
    '<div class="works-grid" style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 0.85rem;">',
    '<div class="works-grid" style="display: flex; gap: 0.85rem;">'
)

# Also add loading="lazy" to the 6 iframes in featured-videos-grid
start_idx = html.find('class="featured-videos-grid')
if start_idx != -1:
    end_idx = html.find('class="thumbnails-section"', start_idx)
    section = html[start_idx:end_idx]
    section = section.replace('<iframe src=', '<iframe loading="lazy" src=')
    html = html[:start_idx] + section + html[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html layout and lazy loading!")
