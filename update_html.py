import re

html_file = 'index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Only keep the first 3 slides. Find all slides and keep only the first 3.
# The slides are within <div class="ww-track"> ... </div>
track_pattern = re.compile(r'<div class="ww-track">(.*?)</div>\s*</div>\s*<div class="ww-controls">', re.DOTALL)
track_match = track_pattern.search(content)

if track_match:
    track_content = track_match.group(1)
    
    # Split the track content by slide
    slides = re.split(r'<div class="ww-slide">', track_content)
    # The first element will be empty space before the first slide
    # Keep the first element (empty space) + the first 3 actual slides
    if len(slides) > 4:
        new_track_content = slides[0] + '<div class="ww-slide">' + '<div class="ww-slide">'.join(slides[1:4])
        
        # Replace the old track content with the new one
        new_content = content[:track_match.start(1)] + new_track_content + content[track_match.end(1):]
        
        # We also need to update the pagination dots to match (only 3 dots)
        new_content = re.sub(
            r'<div class="ww-pagination">\s*<span class="ww-dot active"></span>\s*<span class="ww-dot"></span>\s*<span class="ww-dot"></span>\s*<span class="ww-dot"></span>\s*<span class="ww-dot"></span>\s*<span class="ww-dot"></span>\s*</div>',
            r'<div class="ww-pagination">\n          <span class="ww-dot active"></span>\n          <span class="ww-dot"></span>\n          <span class="ww-dot"></span>\n        </div>',
            new_content
        )
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
