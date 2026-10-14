import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_html = '''    <div class="offerings-row overlapping-phones-layout">
      <!-- Card 2 (Left): Instagram Reels -->
      <div class="offer-box tall-box phone-left">
        <div class="phone-popup popup-left">
          <i class="ph-fill ph-heart" style="color: #FE2C55;"></i> 3M+ Views
        </div>
        <img src="https://images.unsplash.com/photo-1618244972963-dbee1a7edc95?q=80&w=800&auto=format&fit=crop" alt="Instagram Edit" class="phone-bg-img">
        <div class="offer-icon-large" style="position: relative; z-index: 2;">
          <svg width="60" height="60" viewBox="0 0 100 100">
            <defs>
              <linearGradient id="ig-gradient2" x1="0%" y1="100%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#FFD600" />
                <stop offset="50%" stop-color="#FF0069" />
                <stop offset="100%" stop-color="#7638FA" />
              </linearGradient>
            </defs>
            <rect x="15" y="25" width="70" height="50" rx="15" fill="url(#ig-gradient2)" />
            <rect x="15" y="25" width="70" height="15" rx="5" fill="#ffffff" fill-opacity="0.3" />
            <polygon points="43,40 43,60 62,50" fill="#ffffff" />
          </svg>
        </div>
        <div class="offer-text-bottom" style="position: relative; z-index: 2; color: white;">
          <h4 style="color: white;">Instagram</h4>
          <p style="color: white;">Reels</p>
        </div>
      </div>

      <!-- Card 1 (Center): YouTube Shorts -->
      <div class="offer-box tall-box phone-center">
        <div class="phone-popup popup-center">
          <i class="ph-fill ph-fire" style="color: #FF5722;"></i> Trending
        </div>
        <img src="https://images.unsplash.com/photo-1542204165-65bf26472b9b?q=80&w=800&auto=format&fit=crop" alt="YouTube Edit" class="phone-bg-img">
        <div class="offer-icon-large" style="position: relative; z-index: 2;">
          <img src="https://upload.wikimedia.org/wikipedia/commons/f/fc/Youtube_shorts_icon.svg" alt="YouTube Shorts" style="width: 60px; height: 60px;">
        </div>
        <div class="offer-text-bottom" style="position: relative; z-index: 2; color: white;">
          <h4 style="color: white;">YouTube</h4>
          <p style="color: white;">Shorts</p>
        </div>
      </div>

      <!-- Card 3 (Right): TikTok Videos -->
      <div class="offer-box tall-box phone-right">
        <div class="phone-popup popup-right">
          <i class="ph-fill ph-eye" style="color: #25F4EE;"></i> 2.5M+ Views
        </div>
        <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=800&auto=format&fit=crop" alt="TikTok Edit" class="phone-bg-img">
        <div class="offer-icon-large" style="position: relative; z-index: 2;">
          <svg width="60" height="60" viewBox="0 0 100 100">
            <g transform="translate(10, 5)">
              <path d="M45,5 V35 A15,15 0 1 1 30,20 h5 v-10 h-5 A25,25 0 1 0 55,60 V25 A25,25 0 0 0 70,30 V20 A15,15 0 0 1 55,10 V5 Z" fill="#25F4EE" transform="translate(-2, -2)" />
              <path d="M45,5 V35 A15,15 0 1 1 30,20 h5 v-10 h-5 A25,25 0 1 0 55,60 V25 A25,25 0 0 0 70,30 V20 A15,15 0 0 1 55,10 V5 Z" fill="#FE2C55" transform="translate(2, 2)" />
              <path d="M45,5 V35 A15,15 0 1 1 30,20 h5 v-10 h-5 A25,25 0 1 0 55,60 V25 A25,25 0 0 0 70,30 V20 A15,15 0 0 1 55,10 V5 Z" fill="#ffffff" />
            </g>
          </svg>
        </div>
        <div class="offer-text-bottom" style="position: relative; z-index: 2; color: white;">
          <h4 style="color: white;">TikTok</h4>
          <p style="color: white;">Videos</p>
        </div>
      </div>
    </div>'''

# We will replace from <div class="offerings-row"> to the end of that div.
pattern = re.compile(r'<div class="offerings-row">.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
html = pattern.sub(new_html, html, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
