import Lenis from 'lenis';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

// Custom Framer Easing
const framerEase = "power4.out"; // Close to cubic-bezier(0.16, 1, 0.3, 1)

// Initialize Lenis for buttery smooth scrolling
const lenis = new Lenis({
  duration: 1.5, // slightly slower for a more cinematic feel
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), 
  direction: 'vertical',
  gestureDirection: 'vertical',
  smooth: true,
  smoothTouch: false,
  touchMultiplier: 2,
});

// Integrate Lenis with GSAP ScrollTrigger
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
});
gsap.ticker.lagSmoothing(0);

// Navbar Scroll Effect
const navbar = document.querySelector('.navbar');
const navContainer = document.querySelector('.nav-container');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    navContainer.style.background = 'rgba(255, 255, 255, 0.85)';
    navContainer.style.boxShadow = '0 10px 30px rgba(0,0,0,0.08)';
    navContainer.style.padding = '0.5rem 1rem 0.5rem 1.5rem';
  } else {
    navContainer.style.background = 'rgba(255, 255, 255, 0.7)';
    navContainer.style.boxShadow = '0 20px 40px rgba(0,0,0,0.03)';
    navContainer.style.padding = '0.75rem 1rem 0.75rem 1.5rem';
  }
});

// Mobile Hamburger Menu
const navToggle = document.getElementById('navToggle');
const navLinks = document.querySelector('.nav-links');

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('active');
    navLinks.classList.toggle('active');
    document.body.classList.toggle('nav-open');
  });

  // Auto-close on link click
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navToggle.classList.remove('active');
      navLinks.classList.remove('active');
      document.body.classList.remove('nav-open');
    });
  });

  // Close on scroll
  window.addEventListener('scroll', () => {
    if (navLinks.classList.contains('active')) {
      navToggle.classList.remove('active');
      navLinks.classList.remove('active');
      document.body.classList.remove('nav-open');
    }
  });
}

// FAQ Accordion
const faqItems = document.querySelectorAll('.faq-item');
faqItems.forEach(item => {
  const question = item.querySelector('.faq-q');
  question.addEventListener('click', () => {
    const isActive = item.classList.contains('active');
    faqItems.forEach(faq => faq.classList.remove('active'));
    if (!isActive) item.classList.add('active');
  });
});

// Pricing Toggle
const pricingToggle = document.getElementById('priceToggle');
if (pricingToggle) {
  const container = pricingToggle.closest('.toggle-container');
  const labels = container.querySelectorAll('.toggle-label');
  const amounts = document.querySelectorAll('.p-price .amount:not(.custom)');
  const periods = document.querySelectorAll('.p-price .period');
  
  // Create inline style for dynamic toggle
  const style = document.createElement('style');
  style.innerHTML = `
    .toggle-knob {
      transform: translateX(var(--toggle-pos, 0px));
    }
  `;
  document.head.appendChild(style);

  pricingToggle.addEventListener('click', () => {
    const isMonthly = labels[0].classList.contains('active');
    
    if (isMonthly) {
      labels[0].classList.remove('active');
      labels[1].classList.add('active');
      pricingToggle.style.setProperty('--toggle-pos', '34px');
      amounts[0].textContent = '599';
      amounts[1].textContent = '1,899';
      periods.forEach(p => p.textContent = '/project');
    } else {
      labels[0].classList.add('active');
      labels[1].classList.remove('active');
      pricingToggle.style.setProperty('--toggle-pos', '0px');
      amounts[0].textContent = '249';
      amounts[1].textContent = '799';
      periods.forEach(p => p.textContent = '/mo');
    }
  });
}

// ==========================================
// GSAP Framer-Style Animations
// ==========================================

// Initial Hero Reveal
const tlHero = gsap.timeline();

tlHero.from('.hero-top-badge', {
  y: 30, opacity: 0, duration: 1, ease: framerEase, delay: 0.2
})
.from('.hero-title', {
  y: 40, opacity: 0, duration: 1.2, ease: framerEase
}, '-=0.8')
.from('.hero-subtitle', {
  y: 30, opacity: 0, duration: 1, ease: framerEase
}, '-=0.9')
.from('.hero-cta', {
  y: 30, opacity: 0, duration: 1, ease: framerEase
}, '-=0.8')
.from('.hero-image-wrapper', {
  y: 100, scale: 0.95, opacity: 0, duration: 1.5, ease: framerEase
}, '-=0.6')
.from('.orbit-container', {
  opacity: 0, scale: 0.8, duration: 1.5, ease: "back.out(1.2)"
}, '-=1.2');

// Image Parallax
gsap.to('.hero-img', {
  yPercent: 15,
  ease: 'none',
  scrollTrigger: {
    trigger: '.hero-image-wrapper',
    start: 'top bottom',
    end: 'bottom top',
    scrub: true
  }
});

// Generic Section Headers
gsap.utils.toArray('.section-heading').forEach(heading => {
  gsap.from(heading.children, {
    y: 40, opacity: 0, duration: 1.2, stagger: 0.2, ease: framerEase,
    scrollTrigger: { trigger: heading, start: 'top 85%' }
  });
});

// Logos Strip
gsap.from('.logos-title', {
  y: 20, opacity: 0, duration: 1, ease: framerEase,
  scrollTrigger: { trigger: '.logos-section', start: 'top 90%' }
});

gsap.from('.logo-item', {
  y: 20, opacity: 0, duration: 0.8, stagger: 0.1, ease: framerEase,
  scrollTrigger: { trigger: '.logos-track', start: 'top 90%' }
});

// Services Bento Grid
gsap.from('.sb-card', {
  y: 60, opacity: 0, duration: 1.2, stagger: 0.15, ease: framerEase,
  scrollTrigger: { trigger: '.services-bento', start: 'top 80%' }
});

// Works Track Cards (Reveal)
gsap.from('.work-grid-item', {
  y: 50, opacity: 0, duration: 1, stagger: 0.1, ease: framerEase,
  scrollTrigger: { trigger: '.works-grid', start: 'top 80%' }
});

// Stats Section
gsap.from('.stat-box', {
  y: 40, opacity: 0, duration: 1, stagger: 0.2, ease: framerEase,
  scrollTrigger: { trigger: '.stats-row', start: 'top 85%' }
});

// Core Offerings
gsap.from('.offer-box', {
  y: 40, opacity: 0, scale: 0.95, duration: 1, stagger: 0.1, ease: framerEase,
  scrollTrigger: { trigger: '.offerings-row', start: 'top 80%' }
});

// Guarantee Banner Elements
gsap.from('.guarantee-red-bg', {
  y: 60, scale: 0.98, opacity: 0, duration: 1.2, ease: framerEase,
  scrollTrigger: { trigger: '.guarantee-wrapper', start: 'top 85%' }
});

gsap.from('.g-card', {
  y: 40, opacity: 0, duration: 1, stagger: 0.15, ease: framerEase,
  scrollTrigger: { trigger: '.g-right', start: 'top 80%' }
});

// Testimonials
gsap.from('.review-card', {
  y: 50, opacity: 0, duration: 1.2, stagger: 0.2, ease: framerEase,
  scrollTrigger: { trigger: '.reviews-track', start: 'top 80%' }
});

// Reviews Carousel Controls
const reviewsTrack = document.querySelector('.reviews-track');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');

if (reviewsTrack && prevBtn && nextBtn) {
  prevBtn.addEventListener('click', () => {
    reviewsTrack.scrollBy({ left: -350, behavior: 'smooth' });
  });
  nextBtn.addEventListener('click', () => {
    reviewsTrack.scrollBy({ left: 350, behavior: 'smooth' });
  });
}

// Works Carousel Controls
const worksTrack = document.querySelector('.works-track');
const prevBtnWorks = document.querySelector('.prev-btn-works');
const nextBtnWorks = document.querySelector('.next-btn-works');

if (worksTrack && prevBtnWorks && nextBtnWorks) {
  prevBtnWorks.addEventListener('click', () => {
    worksTrack.scrollBy({ left: -490, behavior: 'smooth' });
  });
  nextBtnWorks.addEventListener('click', () => {
    worksTrack.scrollBy({ left: 490, behavior: 'smooth' });
  });
}

// Pricing (Always 100% fully visible, only slide up slightly on scroll)
gsap.from('.p-card', {
  y: 30, duration: 1, stagger: 0.1, ease: framerEase,
  scrollTrigger: { trigger: '.pricing-cards', start: 'top 95%', toggleActions: 'play none none none' }
});

// FAQs
gsap.from('.faq-item', {
  y: 30, opacity: 0, duration: 0.8, stagger: 0.1, ease: framerEase,
  scrollTrigger: { trigger: '.faq-list', start: 'top 85%' }
});

// Brutalist Section Animations
gsap.from('.brutal-hero-content > *', {
  y: 40, opacity: 0, duration: 1.2, stagger: 0.2, ease: framerEase,
  scrollTrigger: { trigger: '.brutal-hero', start: 'top 80%' }
});

gsap.from('.brutal-card', {
  y: 60, opacity: 0, duration: 1.2, stagger: 0.15, ease: framerEase,
  scrollTrigger: { trigger: '.brutal-grid', start: 'top 80%' }
});

// Footer
gsap.from('.footer-cta-section', {
  y: 40, opacity: 0, duration: 1, stagger: 0.15, ease: framerEase,
  scrollTrigger: { trigger: '.footer-dark', start: 'top 85%' }
});

gsap.from('.footer-white-card', {
  y: 50, opacity: 0, duration: 1.2, ease: framerEase,
  scrollTrigger: { trigger: '.footer-white-card', start: 'top 90%' }
});

// Parallax for Footer Background Icons
gsap.to('.f-icon', {
  y: -100,
  ease: 'none',
  scrollTrigger: {
    trigger: '.footer-dark',
    start: 'top bottom',
    end: 'bottom top',
    scrub: true
  }
});

// --- Premium Video Lightbox Modal Controller ---
const videoModal = document.getElementById('videoModal');
const modalIframe = document.getElementById('modalIframe');
const modalContent = videoModal ? videoModal.querySelector('.modal-content') : null;
const modalClose = videoModal ? videoModal.querySelector('.modal-close') : null;
const modalBackdrop = videoModal ? videoModal.querySelector('.modal-backdrop') : null;
const workSlides = document.querySelectorAll('.work-slide');

if (videoModal && modalIframe && modalContent) {
  // Open modal on card click
  workSlides.forEach(slide => {
    slide.addEventListener('click', () => {
      const videoUrl = slide.getAttribute('data-video-url');
      const ratio = slide.getAttribute('data-ratio');
      
      if (videoUrl) {
        // Set ratio format
        if (ratio === 'vertical') {
          modalContent.classList.add('vertical-modal');
        } else {
          modalContent.classList.remove('vertical-modal');
        }
        
        // Set dynamic URL and activate modal
        modalIframe.setAttribute('src', videoUrl);
        videoModal.classList.add('active');
        
        // Pause Lenis smooth scroll
        if (typeof lenis !== 'undefined') {
          lenis.stop();
        }
      }
    });
  });

  // Close modal function
  const closeModal = () => {
    videoModal.classList.remove('active');
    // Set timeout to clear iframe src after animation finishes to prevent sudden flash
    setTimeout(() => {
      modalIframe.setAttribute('src', '');
    }, 400);
    
    // Resume Lenis smooth scroll
    if (typeof lenis !== 'undefined') {
      lenis.start();
    }
  };

  // Bind close triggers
  if (modalClose) modalClose.addEventListener('click', closeModal);
  if (modalBackdrop) modalBackdrop.addEventListener('click', closeModal);
  
  // Close on Escape key press
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && videoModal.classList.contains('active')) {
      closeModal();
    }
  });
}

// Safety fallback: ensure all GSAP-animated elements become visible
// even if ScrollTrigger doesn't fire (e.g., fast scroll, page refresh at section)
setTimeout(() => {
  const animatedElements = document.querySelectorAll(
    '.faq-item, .stat-box, .offer-box, .sb-card, .g-card, .review-card, .work-slide, .guarantee-red-bg, .footer-cta-section, .footer-white-card'
  );
  animatedElements.forEach(el => {
    if (getComputedStyle(el).opacity === '0') {
      gsap.to(el, { opacity: 1, y: 0, x: 0, duration: 0.5, ease: 'power2.out' });
    }
  });
}, 3000);

// ==========================================
// Web Works Premium Featured Slider
// ==========================================

const initWebWorksScroll = () => {
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
document.addEventListener('DOMContentLoaded', initWebWorksScroll);
function initThumbnailsAnimations() {
  const cards = document.querySelectorAll('.photo-card');
  if (cards.length === 0) return;
  
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

  cards.forEach((card, index) => {
    // Random rotation for the scattered paper effect
    const randomRot = (Math.random() * 10) - 5; 
    card.dataset.rotation = randomRot;
    
    // Initial Entrance Animation
    gsap.to(card, {
      scrollTrigger: {
        trigger: '.thumbnails-gallery-container',
        start: 'top 80%',
        toggleActions: 'play none none none'
      },
      y: 0,
      opacity: 1,
      rotation: randomRot,
      duration: 1.2,
      delay: index * 0.2,
      ease: "back.out(1.2)"
    });

    // Interactive Hover Animation
    card.addEventListener('mouseenter', () => {
      if (typeof cursor !== 'undefined' && cursor) cursor.classList.add('hover');
      gsap.to(card, {
        rotation: 0,
        scale: 1.05,
        y: -20,
        boxShadow: "0 30px 60px rgba(0,0,0,0.15), 0 10px 20px rgba(0,0,0,0.1)",
        duration: 0.4,
        ease: "power2.out",
        zIndex: 10
      });
    });

    card.addEventListener('mouseleave', () => {
      if (typeof cursor !== 'undefined' && cursor) cursor.classList.remove('hover');
      gsap.to(card, {
        rotation: randomRot,
        scale: 1,
        y: 0,
        boxShadow: "0 15px 35px rgba(0,0,0,0.1), 0 5px 15px rgba(0,0,0,0.05)",
        duration: 0.4,
        ease: "power2.out",
        zIndex: 1
      });
    });
  });
}

document.addEventListener('DOMContentLoaded', initThumbnailsAnimations);

// Interactive Footer Dot Grid
const initFooterDots = () => {
  const canvas = document.getElementById('footer-dots-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const footer = document.querySelector('.footer-dark');
  
  let width, height;
  let dots = [];
  const spacing = 35; // Space between dots
  const baseRadius = 1;
  const maxRadius = 3;
  const hoverDistance = 150; // Distance of the spotlight effect

  let mouse = { x: -1000, y: -1000 };

  const resize = () => {
    width = footer.offsetWidth;
    height = footer.offsetHeight;
    canvas.width = width;
    canvas.height = height;
    createDots();
  };

  const createDots = () => {
    dots = [];
    for (let x = 0; x < width; x += spacing) {
      for (let y = 0; y < height; y += spacing) {
        dots.push({ x, y });
      }
    }
  };

  const draw = () => {
    ctx.clearRect(0, 0, width, height);
    
    dots.forEach(dot => {
      const dx = mouse.x - dot.x;
      const dy = mouse.y - dot.y;
      const distance = Math.sqrt(dx * dx + dy * dy);
      
      let radius = baseRadius;
      let opacity = 0.15; // Base opacity
      
      if (distance < hoverDistance) {
        const factor = 1 - (distance / hoverDistance);
        radius = baseRadius + (maxRadius - baseRadius) * factor;
        opacity = 0.15 + (0.5 * factor); // Max opacity 0.65
      }
      
      ctx.beginPath();
      ctx.arc(dot.x, dot.y, radius, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255, 255, 255, ${opacity})`;
      ctx.fill();
    });
    
    requestAnimationFrame(draw);
  };

  footer.addEventListener('mousemove', (e) => {
    const rect = footer.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
  });

  footer.addEventListener('mouseleave', () => {
    mouse.x = -1000;
    mouse.y = -1000;
  });

  window.addEventListener('resize', resize);
  resize();
  draw();
};

initFooterDots();

// ==========================================
// Works Brands Carousel (Horizontal Scroll)
// ==========================================
const brandsScrollTrack = document.getElementById('worksScrollTrack');
const worksPrevBtn = document.getElementById('worksPrev');
const worksNextBtn = document.getElementById('worksNext');

if (brandsScrollTrack && worksPrevBtn && worksNextBtn) {
  const scrollAmount = 240; // px per button click

  worksPrevBtn.addEventListener('click', () => {
    brandsScrollTrack.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
  });

  worksNextBtn.addEventListener('click', () => {
    brandsScrollTrack.scrollBy({ left: scrollAmount, behavior: 'smooth' });
  });

  // Hide/show buttons based on scroll position
  const updateBrandsButtons = () => {
    worksPrevBtn.style.opacity = brandsScrollTrack.scrollLeft <= 10 ? '0.4' : '1';
    worksNextBtn.style.opacity =
      brandsScrollTrack.scrollLeft + brandsScrollTrack.clientWidth >= brandsScrollTrack.scrollWidth - 10
        ? '0.4' : '1';
  };

  brandsScrollTrack.addEventListener('scroll', updateBrandsButtons, { passive: true });
  updateBrandsButtons(); // initial state
}

// ==========================================
// Scroll Timeline Logic — Full Implementation
// ==========================================
(function () {
  const scrollTimeline  = document.getElementById('scrollTimeline');
  const timelineTrack   = document.getElementById('timelineTrack');
  const ticksContainer  = document.getElementById('timelineTicks');
  const playheadWrapper = document.getElementById('playheadWrapper');
  const playheadBadge   = document.getElementById('playheadBadge');
  const clockEl         = document.getElementById('timelineClock');

  const timelineProgress = document.getElementById('timelineProgress');

  if (!scrollTimeline || !timelineTrack || !ticksContainer || !playheadWrapper || !playheadBadge) return;

  // ── 1. Generate ruler ticks ──────────────────────────────────────────────
  function buildTicks() {
    ticksContainer.innerHTML = '';
    const numMajor = 12; // 0 → 1200

    for (let i = 0; i <= numMajor; i++) {
      const pct   = (i / numMajor) * 100;
      const value = i * 100;

      // Major tick
      const major = document.createElement('div');
      major.className = 'timeline-tick major';
      major.style.left = pct + '%';
      ticksContainer.appendChild(major);

      // Label (skip 0)
      if (value > 0 && value <= 1100) {
        const label = document.createElement('span');
        label.className = 'timeline-tick-label';
        label.style.left = pct + '%';
        label.textContent = value;
        ticksContainer.appendChild(label);
      }

      // 4 minor ticks between each major
      if (i < numMajor) {
        for (let m = 1; m <= 4; m++) {
          const minorPct = pct + (m / (numMajor * 5)) * 100;
          const minor = document.createElement('div');
          minor.className = 'timeline-tick minor';
          minor.style.left = minorPct + '%';
          ticksContainer.appendChild(minor);
        }
      }
    }
  }

  buildTicks();
  window.addEventListener('resize', buildTicks);

  // ── 2. Live clock ────────────────────────────────────────────────────────
  if (clockEl) {
    function updateClock() {
      const now  = new Date();
      const h    = now.getHours();
      const m    = String(now.getMinutes()).padStart(2, '0');
      const s    = String(now.getSeconds()).padStart(2, '0');
      const ampm = h >= 12 ? 'PM' : 'AM';
      const h12  = ((h % 12) || 12);
      clockEl.textContent = String(h12).padStart(2, '0') + ':' + m + ':' + s + ' ' + ampm;
    }
    updateClock();
    setInterval(updateClock, 1000);
  }

  // ── 3. Playhead movement on scroll ──────────────────────────────────────
  let shipped = false;

  function updatePlayhead() {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPct = docHeight > 0 ? Math.min(1, Math.max(0, scrollTop / docHeight)) : 0;
    const trackW    = timelineTrack.offsetWidth;
    const xPos      = scrollPct * trackW;

    // Move the playhead
    playheadWrapper.style.transform = 'translateX(' + xPos + 'px)';

    // Update progress fill width
    if (timelineProgress) {
      timelineProgress.style.width = (scrollPct * 100) + '%';
    }

    const pctInt = Math.round(scrollPct * 100);
    
    // Toggle SHIPPED state at 100%
    if (scrollPct >= 0.99) {
      if (!shipped) {
        shipped = true;
        scrollTimeline.classList.add('is-shipped');
        playheadBadge.textContent = 'SHIPPED';
      }
    } else {
      if (shipped) {
        shipped = false;
        scrollTimeline.classList.remove('is-shipped');
      }
      playheadBadge.textContent = pctInt + '%';
    }
  }

  window.addEventListener('scroll', updatePlayhead, { passive: true });
  window.addEventListener('resize', updatePlayhead);
  updatePlayhead();
})();

// ==========================================
// Custom Figma Cursor Logic
// ==========================================
const customCursor = document.querySelector('.custom-cursor.figma-cursor');

if (customCursor) {
  document.addEventListener('mousemove', (e) => {
    if (typeof gsap !== 'undefined') {
      gsap.to(customCursor, {
        x: e.clientX,
        y: e.clientY,
        duration: 0.1,
        ease: "power2.out"
      });
    } else {
      customCursor.style.transform = `translate3d(${e.clientX}px, ${e.clientY}px, 0)`;
    }
  });

  const interactables = document.querySelectorAll('a, button, .faq-q, .webworks-card, .toggle-container');
  interactables.forEach(el => {
    el.addEventListener('mouseenter', () => customCursor.classList.add('hover'));
    el.addEventListener('mouseleave', () => customCursor.classList.remove('hover'));
  });
}

// =========================================
// Stats Hover Counting Animation
// =========================================
document.addEventListener('DOMContentLoaded', () => {
  const storyStats = document.querySelectorAll('.story-stat');
  
  storyStats.forEach(stat => {
    const h3 = stat.querySelector('h3');
    if (!h3) return;
    
    // Store original text on the element so we don't parse it multiple times
    if (!h3.dataset.original) {
      h3.dataset.original = h3.innerText.trim();
    }
    
    const originalText = h3.dataset.original;
    // Extract number and suffix (e.g. "250K+" -> "250" and "K+")
    const match = originalText.match(/^([0-9\.]+)(.*)$/);
    if (!match) return; 
    
    const targetValue = parseFloat(match[1]);
    const suffix = match[2];
    
    let animationObj = { val: targetValue };
    let tween = null;
    
    stat.addEventListener('mouseenter', () => {
      if (typeof gsap === 'undefined') return;
      
      if (tween) tween.kill();
      
      animationObj.val = 0;
      h3.innerText = '0' + suffix;
      
      tween = gsap.to(animationObj, {
        val: targetValue,
        duration: 1.2,
        ease: "power2.out",
        onUpdate: () => {
          h3.innerText = Math.floor(animationObj.val) + suffix;
        },
        onComplete: () => {
          h3.innerText = originalText;
        }
      });
    });
  });
});

// Custom Multiplayer Cursor Logic
document.addEventListener("DOMContentLoaded", () => {
  const cursor = document.getElementById("custom-cursor");
  if (!cursor) return;

  // Track mouse movement
  document.addEventListener("mousemove", (e) => {
    // We use requestAnimationFrame for smooth movement without stutter
    requestAnimationFrame(() => {
      cursor.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
    });
  });

  // Hide cursor when leaving the window
  document.addEventListener("mouseleave", () => {
    cursor.style.display = "none";
  });
  
  // Show cursor when entering the window
  document.addEventListener("mouseenter", () => {
    cursor.style.display = "flex";
  });
});

