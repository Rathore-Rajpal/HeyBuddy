// ============================================
// BUDDY AI ASSISTANT - WEBSITE INTERACTIONS
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS (Animate On Scroll)
    AOS.init({
        duration: 1000,
        once: true,
        offset: 100
    });

    // Initialize SiriWave Voice Visualization
    initSiriWave();

    // Smooth scroll for navigation links
    setupSmoothScroll();

    // Navbar transparency on scroll
    handleNavbarScroll();
});

// ============================================
// SIRIWAVE VOICE VISUALIZATION
// ============================================
function initSiriWave() {
    const canvas = document.getElementById('siriwave');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    let phase = 0;
    let amplitude = 30;
    
    function drawWave() {
        ctx.clearRect(0, 0, width, height);
        
        // Draw multiple waves with different colors
        drawSingleWave(ctx, width, height, phase, amplitude, 'rgba(0, 170, 255, 0.8)', 1);
        drawSingleWave(ctx, width, height, phase + Math.PI / 2, amplitude * 0.8, 'rgba(184, 3, 240, 0.6)', 0.8);
        drawSingleWave(ctx, width, height, phase + Math.PI, amplitude * 0.6, 'rgba(0, 255, 136, 0.4)', 0.6);
        
        phase += 0.05;
        requestAnimationFrame(drawWave);
    }
    
    function drawSingleWave(ctx, width, height, phase, amplitude, color, lineWidth) {
        ctx.beginPath();
        ctx.strokeStyle = color;
        ctx.lineWidth = lineWidth * 2;
        ctx.lineCap = 'round';
        
        const centerY = height / 2;
        const frequency = 0.015;
        
        for (let x = 0; x < width; x++) {
            const y = centerY + Math.sin(x * frequency + phase) * amplitude * Math.sin(x / width * Math.PI);
            
            if (x === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        }
        
        ctx.stroke();
    }
    
    // Start animation
    drawWave();
    
    // Pulse amplitude effect
    setInterval(() => {
        amplitude = 20 + Math.random() * 20;
    }, 2000);
}

// ============================================
// SMOOTH SCROLL NAVIGATION
// ============================================
function setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            e.preventDefault();
            const target = document.querySelector(href);
            
            if (target) {
                const offsetTop = target.offsetTop - 70;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                const navbarCollapse = document.querySelector('.navbar-collapse');
                if (navbarCollapse.classList.contains('show')) {
                    const toggler = document.querySelector('.navbar-toggler');
                    toggler.click();
                }
            }
        });
    });
}

// ============================================
// NAVBAR SCROLL EFFECT
// ============================================
function handleNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(0, 0, 0, 0.98)';
            navbar.style.boxShadow = '0 2px 10px rgba(0, 170, 255, 0.1)';
        } else {
            navbar.style.background = 'rgba(0, 0, 0, 0.95)';
            navbar.style.boxShadow = 'none';
        }
    });
}

// ============================================
// COPY CODE TO CLIPBOARD
// ============================================
function copyCode(button) {
    const codeBlock = button.previousElementSibling;
    const code = codeBlock.textContent;
    
    navigator.clipboard.writeText(code).then(() => {
        const originalHTML = button.innerHTML;
        button.innerHTML = '<i class="fas fa-check"></i> Copied!';
        button.style.background = '#00FF88';
        
        setTimeout(() => {
            button.innerHTML = originalHTML;
            button.style.background = '';
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy:', err);
    });
}

// ============================================
// FLOATING ORB MOUSE INTERACTION
// ============================================
document.addEventListener('mousemove', (e) => {
    const orbs = document.querySelectorAll('.floating-orb');
    const mouseX = e.clientX / window.innerWidth;
    const mouseY = e.clientY / window.innerHeight;
    
    orbs.forEach((orb, index) => {
        const speed = (index + 1) * 0.05;
        const x = (mouseX - 0.5) * 100 * speed;
        const y = (mouseY - 0.5) * 100 * speed;
        
        orb.style.transform = `translate(${x}px, ${y}px)`;
    });
});

// ============================================
// FEATURE CARD TILT EFFECT
// ============================================
document.querySelectorAll('.feature-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = (y - centerY) / 10;
        const rotateY = (centerX - x) / 10;
        
        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-10px)`;
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transform = '';
    });
});

// ============================================
// DOWNLOAD BUTTON CLICK TRACKING
// ============================================
document.querySelectorAll('.btn-primary-custom').forEach(btn => {
    btn.addEventListener('click', (e) => {
        // Add ripple effect
        const ripple = document.createElement('span');
        ripple.classList.add('ripple');
        
        const rect = btn.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;
        
        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        
        btn.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
    });
});

// ============================================
// CAROUSEL AUTO-PLAY WITH PAUSE ON HOVER
// ============================================
const carousel = document.querySelector('#screenshotCarousel');
if (carousel) {
    let carouselInstance = new bootstrap.Carousel(carousel, {
        interval: 4000,
        wrap: true
    });
    
    carousel.addEventListener('mouseenter', () => {
        carouselInstance.pause();
    });
    
    carousel.addEventListener('mouseleave', () => {
        carouselInstance.cycle();
    });
}

// ============================================
// STATS COUNTER ANIMATION
// ============================================
function animateCounter(element, target, duration) {
    let current = 0;
    const increment = target / (duration / 16);
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target + '+';
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(current) + '+';
        }
    }, 16);
}

// Trigger counter animation when stats come into view
const observerOptions = {
    threshold: 0.5
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const statNumbers = entry.target.querySelectorAll('.stat-number');
            statNumbers.forEach(stat => {
                const text = stat.textContent;
                if (text.includes('+')) {
                    const number = parseInt(text);
                    if (!isNaN(number)) {
                        stat.textContent = '0+';
                        animateCounter(stat, number, 2000);
                    }
                }
            });
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

const statsRow = document.querySelector('.stats-row');
if (statsRow) {
    observer.observe(statsRow);
}

// ============================================
// CONSOLE EASTER EGG
// ============================================
console.log('%c🤖 Buddy AI Assistant', 'font-size: 24px; font-weight: bold; background: linear-gradient(135deg, #00AAFF, #B803F0); -webkit-background-clip: text; color: transparent;');
console.log('%cInterested in the code? Check out: https://github.com/Rathore-Rajpal/HeyBuddy', 'font-size: 14px; color: #00AAFF;');
console.log('%cMade with ❤️ by Rajpal Singh Rathore', 'font-size: 12px; color: #B803F0;');