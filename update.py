import re

html_file = 'index.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new slider HTML structure
new_slider = '''      <div class="webworks-slider-wrapper">
        <div class="ww-track">
          
          <div class="ww-slide">
            <div class="ww-card">
              <div class="ww-drag-tooltip"><i class="ph-bold ph-caret-left"></i> DRAG <i class="ph-bold ph-caret-right"></i></div>
              <div class="ww-mockup">
                <img src="/webwork-dr-angaj.png" alt="Dr Angaj Skandh Preview" loading="lazy" />
              </div>
              <div class="ww-bottom">
                <div class="ww-title-area">
                  <span class="ww-dot" style="background:#ef4444;"></span>
                  <h3>Dr Angaj Skandh</h3>
                </div>
                <div class="ww-tags">
                  <a href="https://dr-angaj-skandh.vercel.app/" target="_blank" class="ww-pill">LIVE PREVIEW</a>
                  <span class="ww-pill outline">MEDICAL</span>
                  <span class="ww-pill outline">RESPONSIVE</span>
                </div>
              </div>
            </div>
          </div>
          
          <div class="ww-slide">
            <div class="ww-card">
              <div class="ww-drag-tooltip"><i class="ph-bold ph-caret-left"></i> DRAG <i class="ph-bold ph-caret-right"></i></div>
              <div class="ww-mockup">
                <img src="/webwork-sonu-portfolio.png" alt="Sonu Portfolio Preview" loading="lazy" />
              </div>
              <div class="ww-bottom">
                <div class="ww-title-area">
                  <span class="ww-dot" style="background:#eab308;"></span>
                  <h3>Sonu Portfolio</h3>
                </div>
                <div class="ww-tags">
                  <a href="https://sonuportfolioooo.netlify.app/" target="_blank" class="ww-pill">LIVE PREVIEW</a>
                  <span class="ww-pill outline">CREATIVE</span>
                  <span class="ww-pill outline">GSAP</span>
                </div>
              </div>
            </div>
          </div>
          
          <div class="ww-slide">
            <div class="ww-card">
              <div class="ww-drag-tooltip"><i class="ph-bold ph-caret-left"></i> DRAG <i class="ph-bold ph-caret-right"></i></div>
              <div class="ww-mockup">
                <img src="/webwork-dairy-farm.png" alt="Swami Swad Dairy Farm Preview" loading="lazy" />
              </div>
              <div class="ww-bottom">
                <div class="ww-title-area">
                  <span class="ww-dot" style="background:#22c55e;"></span>
                  <h3>Swami Swad Dairy Farm</h3>
                </div>
                <div class="ww-tags">
                  <a href="https://swamiswaddairyfarm.netlify.app/" target="_blank" class="ww-pill">LIVE PREVIEW</a>
                  <span class="ww-pill outline">E-COMMERCE</span>
                  <span class="ww-pill outline">BRANDING</span>
                </div>
              </div>
            </div>
          </div>
          
          <div class="ww-slide">
            <div class="ww-card">
              <div class="ww-drag-tooltip"><i class="ph-bold ph-caret-left"></i> DRAG <i class="ph-bold ph-caret-right"></i></div>
              <div class="ww-mockup">
                <img src="/webwork-toolsvillage.png" alt="ToolsVillage Preview" loading="lazy" />
              </div>
              <div class="ww-bottom">
                <div class="ww-title-area">
                  <span class="ww-dot" style="background:#3b82f6;"></span>
                  <h3>ToolsVillage</h3>
                </div>
                <div class="ww-tags">
                  <a href="https://toolvillage-6802c.web.app/" target="_blank" class="ww-pill">LIVE PREVIEW</a>
                  <span class="ww-pill outline">AI TOOL</span>
                  <span class="ww-pill outline">SAAS</span>
                </div>
              </div>
            </div>
          </div>

          <div class="ww-slide">
            <div class="ww-card">
              <div class="ww-drag-tooltip"><i class="ph-bold ph-caret-left"></i> DRAG <i class="ph-bold ph-caret-right"></i></div>
              <div class="ww-mockup">
                <img src="/webwork-personal.png" alt="Personal Website Preview" loading="lazy" />
              </div>
              <div class="ww-bottom">
                <div class="ww-title-area">
                  <span class="ww-dot" style="background:#8b5cf6;"></span>
                  <h3>Personal Website</h3>
                </div>
                <div class="ww-tags">
                  <a href="https://sonukumar07.netlify.app/" target="_blank" class="ww-pill">LIVE PREVIEW</a>
                  <span class="ww-pill outline">PORTFOLIO</span>
                  <span class="ww-pill outline">DARK THEME</span>
                </div>
              </div>
            </div>
          </div>

          <div class="ww-slide">
            <div class="ww-card">
              <div class="ww-drag-tooltip"><i class="ph-bold ph-caret-left"></i> DRAG <i class="ph-bold ph-caret-right"></i></div>
              <div class="ww-mockup">
                <img src="/webwork-ai-student.png" alt="AI Student Partner Preview" loading="lazy" />
              </div>
              <div class="ww-bottom">
                <div class="ww-title-area">
                  <span class="ww-dot" style="background:#f43f5e;"></span>
                  <h3>AI Student Partner</h3>
                </div>
                <div class="ww-tags">
                  <a href="https://aistudentpartner.netlify.app/" target="_blank" class="ww-pill">LIVE PREVIEW</a>
                  <span class="ww-pill outline">DASHBOARD</span>
                  <span class="ww-pill outline">AI APP</span>
                </div>
              </div>
            </div>
          </div>
          
        </div>
      </div>
      
      <div class="ww-controls">
        <div class="ww-pagination">
          <span class="ww-dot active"></span>
          <span class="ww-dot"></span>
          <span class="ww-dot"></span>
          <span class="ww-dot"></span>
          <span class="ww-dot"></span>
          <span class="ww-dot"></span>
        </div>
        <div class="ww-nav-buttons">
          <button class="ww-nav-btn prev"><i class="ph-bold ph-caret-left"></i></button>
          <button class="ww-nav-btn next"><i class="ph-bold ph-caret-right"></i></button>
        </div>
      </div>'''

# Replace from <div class="webworks-slider-wrapper"> to the end of the webworks container
pattern = re.compile(r'<div class="webworks-slider-wrapper">.*?(?=    </div>\s*</section>)', re.DOTALL)
new_content = pattern.sub(new_slider, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)
