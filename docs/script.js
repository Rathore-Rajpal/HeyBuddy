// =============================================
// PROFESSIONAL UI - BUDDY AI ASSISTANT
// =============================================

$(document).ready(function() {
    // Initialize SiriWave
    initSiriWave();
    
    // Initialize Canvas Animation
    initCanvas();
    
    // Smooth scroll for navigation
    setupSmoothScroll();
    
    // Navbar scroll effect
    handleNavbarScroll();
    
    // Scroll animations
    handleScrollAnimations();
});

// =============================================
// SIRIWAVE INITIALIZATION
// =============================================
function initSiriWave() {
    const container = document.getElementById('siri-container');
    if (!container) return;
    
    try {
        const siriWave = new SiriWave({
            container: container,
            width: container.offsetWidth || 600,
            height: 160,
            style: 'ios9',
            amplitude: 1.5,
            speed: 0.20,
            autostart: true,
            color: '#00AAFF',
            frequency: 4,
            cover: true
        });
        
        // Update SiriWave on window resize
        window.addEventListener('resize', function() {
            const newWidth = container.offsetWidth || 600;
            siriWave.setSpeed(0.20);
            siriWave.setAmplitude(1.5);
        });
    } catch (error) {
        console.log('SiriWave library not loaded yet');
    }
}

// =============================================
// CANVAS PARTICLE ANIMATION
// =============================================
function initCanvas() {
    const canvas = document.getElementById('canvasOne');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    let particles = [];
    const particleCount = 80;
    
    // Create particles
    for (let i = 0; i < particleCount; i++) {
        particles.push({
            x: Math.random() * width,
            y: Math.random() * height,
            radius: Math.random() * 2 + 0.5,
            vx: (Math.random() - 0.5) * 0.5,
            vy: (Math.random() - 0.5) * 0.5,
            color: Math.random() > 0.5 ? '#00AAFF' : '#B803F0'
        });
    }
    
    function animate() {
        ctx.clearRect(0, 0, width, height);
        
        particles.forEach((particle, i) => {
            // Update position
            particle.x += particle.vx;
            particle.y += particle.vy;
            
            // Bounce off edges
            if (particle.x < 0 || particle.x > width) particle.vx *= -1;
            if (particle.y < 0 || particle.y > height) particle.vy *= -1;
            
            // Draw particle
            ctx.beginPath();
            ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
            ctx.fillStyle = particle.color;
            ctx.fill();
            
            // Draw connections
            particles.slice(i + 1).forEach(otherParticle => {
                const dx = particle.x - otherParticle.x;
                const dy = particle.y - otherParticle.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 120) {
                    ctx.beginPath();
                    ctx.moveTo(particle.x, particle.y);
                    ctx.lineTo(otherParticle.x, otherParticle.y);
                    ctx.strokeStyle = `rgba(0, 170, 255, ${(1 - distance / 120) * 0.3})`;
                    ctx.lineWidth = 0.5;
                    ctx.stroke();
                }
            });
        });
        
        requestAnimationFrame(animate);
    }
    
    animate();
}

// =============================================
// SMOOTH SCROLL
// =============================================
function setupSmoothScroll() {
    $('a[href^="#"]').on('click', function(e) {
        const href = $(this).attr('href');
        if (href === '#' || href === '#!') return;
        
        e.preventDefault();
        const target = $(href);
        
        if (target.length) {
            const offsetTop = target.offset().top - 70;
            
            $('html, body').animate({
                scrollTop: offsetTop
            }, 800);
            
            // Update active nav link
            $('.nav-link').removeClass('active');
            $(this).addClass('active');
            
            // Close mobile menu if open
            const navbarCollapse = $('.navbar-collapse');
            if (navbarCollapse.hasClass('show')) {
                $('.navbar-toggler').click();
            }
        }
    });
}

// =============================================
// NAVBAR SCROLL EFFECT
// =============================================
function handleNavbarScroll() {
    const navbar = $('.navbar');
    
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 50) {
            navbar.addClass('navbar-scrolled');
        } else {
            navbar.removeClass('navbar-scrolled');
        }
        
        // Update active nav based on scroll position
        updateActiveNav();
    });
}

function updateActiveNav() {
    const scrollPos = $(window).scrollTop() + 100;
    
    $('section').each(function() {
        const section = $(this);
        const sectionTop = section.offset().top;
        const sectionBottom = sectionTop + section.outerHeight();
        const sectionId = section.attr('id');
        
        if (scrollPos >= sectionTop && scrollPos < sectionBottom) {
            $('.nav-link').removeClass('active');
            $(`.nav-link[href="#${sectionId}"]`).addClass('active');
        }
    });
}

// =============================================
// SCROLL ANIMATIONS
// =============================================
function handleScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    // Observe feature cards
    document.querySelectorAll('.feature-card').forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = `all 0.6s ease ${index * 0.1}s`;
        observer.observe(card);
    });
}

// =============================================
// COPY CODE FUNCTION
// =============================================
function copyCode(button) {
    const codeBlock = button.previousElementSibling;
    const code = codeBlock.textContent;
    
    navigator.clipboard.writeText(code).then(() => {
        const originalHTML = button.innerHTML;
        button.innerHTML = '<i class="fas fa-check"></i> Copied!';
        button.style.background = '#00FF88';
        button.style.borderColor = '#00FF88';
        button.style.color = '#000';
        
        setTimeout(() => {
            button.innerHTML = originalHTML;
            button.style.background = '';
            button.style.borderColor = '';
            button.style.color = '';
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy:', err);
    });
}

// =============================================
// FEATURE CARD HOVER EFFECTS
// =============================================
$('.feature-card').hover(
    function() {
        $(this).find('.feature-icon').addClass('animate__animated animate__pulse');
    },
    function() {
        $(this).find('.feature-icon').removeClass('animate__animated animate__pulse');
    }
);

// =============================================
// CONSOLE MESSAGE
// =============================================
console.log('%c🤖 Buddy AI Assistant', 'font-size: 24px; font-weight: bold; background: linear-gradient(135deg, #00AAFF, #B803F0); -webkit-background-clip: text; color: transparent;');
console.log('%cGitHub: https://github.com/Rathore-Rajpal/HeyBuddy', 'font-size: 14px; color: #00AAFF;');
console.log('%cMade with ❤️ by Rajpal Singh Rathore', 'font-size: 12px; color: #B803F0;');