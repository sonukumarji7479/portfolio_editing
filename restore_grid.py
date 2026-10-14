with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace(
    '<div class="works-grid" style="display: flex; gap: 0.85rem;">',
    '<div class="works-grid" style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 0.85rem;">'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Restored inline grid style for desktop!")
