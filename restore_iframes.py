import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace thumbnails back with lazy-loaded iframes
def replace_thumb(match):
    # match.group(0) is the whole <a class="work-grid-item"...>...</a>
    # we need to extract the youtube video ID from the href
    a_tag = match.group(0)
    vid_match = re.search(r'youtube\.com/shorts/([^"]+)', a_tag)
    if not vid_match:
        return a_tag
    vid_id = vid_match.group(1)
    
    # Reconstruct the iframe
    iframe_html = f'''<iframe loading="lazy" src="https://www.youtube.com/embed/{vid_id}?autoplay=1&mute=1&loop=1&playlist={vid_id}&controls=0&rel=0&playsinline=1" title="YouTube Short player" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            style="width: 100%; height: 100%; position: absolute; top: 0; left: 0; pointer-events: none; border: none; transform: scale(1.02);"></iframe>'''
            
    # Replace the inner content of the <a> tag
    new_a_tag = re.sub(r'<div class="yt-thumb-container".*?</div>\s*</div>', iframe_html, a_tag, flags=re.DOTALL)
    
    # If the regex didn't match the inner div for some reason, fallback to basic replacement
    if new_a_tag == a_tag:
        # Just completely rebuild the a tag
        return f'''<a href="https://www.youtube.com/shorts/{vid_id}" target="_blank" class="work-grid-item" style="border-radius: 10px; overflow: hidden; position: relative; aspect-ratio: 9/16; display: block; border: 1px solid #e5e7eb; max-height: 340px;">
          {iframe_html}
        </a>'''
        
    return new_a_tag

# Match all work-grid-item anchor tags
html = re.sub(r'<a[^>]+class="work-grid-item"[^>]*>.*?</a>', replace_thumb, html, flags=re.DOTALL)

# Ensure ALL iframes in the document have loading="lazy"
html = html.replace('<iframe src="', '<iframe loading="lazy" src="')
# Fix any double loading="lazy" if it happened
html = html.replace('loading="lazy" loading="lazy"', 'loading="lazy"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Restored iframes with lazy loading!")
