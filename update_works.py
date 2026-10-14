import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find the works-grid
start_idx = html.find('<div class="works-grid"')
end_idx = html.find('<!-- Featured Videos', start_idx)

works_grid_html = html[start_idx:end_idx]

# Find all iframes
def replace_iframe(match):
    src = match.group(1)
    # Extract video ID
    vid_match = re.search(r'embed/([^?]+)', src)
    if not vid_match:
        return match.group(0)
    vid_id = vid_match.group(1)
    
    img_url = f"https://i.ytimg.com/vi/{vid_id}/maxresdefault.jpg"
    
    return f'''<div class="yt-thumb-container" style="width: 100%; height: 100%; position: absolute; top: 0; left: 0; background-color: #111;">
            <img src="{img_url}" alt="Short Thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s;">
            <div class="yt-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 48px; height: 48px; background: rgba(0,0,0,0.6); border-radius: 50%; display: flex; justify-content: center; align-items: center; border: 1px solid rgba(255,255,255,0.2); backdrop-filter: blur(4px);">
              <i class="ph-fill ph-play" style="color: white; font-size: 1.5rem; margin-left: 3px;"></i>
            </div>
          </div>'''

new_works_grid = re.sub(r'<iframe\s+src="([^"]+)"[^>]*></iframe>', replace_iframe, works_grid_html)

html = html[:start_idx] + new_works_grid + html[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html!")
