import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the end of the webworks section that is missing closing tags
old_str = '''                      <a href="https://sonuportfolioooo.netlify.app/" target="_blank" rel="noopener noreferrer" class="webworks-btn">
                        <span>Live Preview</span>
                        <i class="ph ph-arrow-up-right"></i>
                      </a>
                    </div>
  
  
  
  
    <!-- Footer -->'''

new_str = '''                      <a href="https://sonuportfolioooo.netlify.app/" target="_blank" rel="noopener noreferrer" class="webworks-btn">
                        <span>Live Preview</span>
                        <i class="ph ph-arrow-up-right"></i>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->'''

# Wait, we need to match it correctly, let's just use re.sub with a flexible whitespace regex
content = re.sub(
    r'<span>Live Preview</span>\s*<i class="ph ph-arrow-up-right"></i>\s*</a>\s*</div>\s*<!-- Footer -->',
    r'<span>Live Preview</span>\n                        <i class="ph ph-arrow-up-right"></i>\n                      </a>\n                    </div>\n                  </div>\n                </div>\n              </div>\n            </div>\n          </div>\n        </div>\n      </div>\n    </section>\n\n    <!-- Footer -->',
    content
)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

