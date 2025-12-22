// =============================================
// BUDDY AI ASSISTANT - GITHUB PAGES
// Using same animations as main app
// =============================================

$(document).ready(function() {
    // Initialize text animations
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            delay: 50
        },
        out: {
            effect: "fadeOutUp",
            delay: 50
        }
    });

    // Initialize SiriWave
    if (document.getElementById('siri-container')) {
        var siriWave = new SiriWave({
            container: document.getElementById('siri-container'),
            width: 880,
            height: 200,
            style: 'ios9',
            amplitude: 1,
            speed: 0.30,
            autoStart: true,
            color: '#00AAFF'
        });
    }

    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeIn",
            delay: 50
        },
        out: {
            effect: "fadeOut",
            delay: 50
        }
    });

    // Smooth scroll for anchor links
    $('a[href^="#"]').on('click', function(e) {
        const href = $(this).attr('href');
        if (href !== '#') {
            e.preventDefault();
            const target = $(href);
            if (target.length) {
                $('html, body').animate({
                    scrollTop: target.offset().top - 50
                }, 800);
            }
        }
    });

    // Canvas animation (similar to main app)
    initCanvas();

    // Hide Start section after delay and show oval, then SiriWave
    setTimeout(function() {
        $('#Start').fadeOut(1000, function() {
            $('#oval').fadeIn(1000);
            setTimeout(function() {
                $('#oval').fadeOut(1000, function() {
                    $('#siriwave').fadeIn(1000);
                });
            }, 5000);
        });
    }, 4000);
});

// =============================================
// CANVAS ANIMATION (From Main App)
// =============================================
function initCanvas() {
    const canvas = document.getElementById('canvasOne');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    let particles = [];
    const particleCount = 100;
    
    // Create particles
    for (let i = 0; i < particleCount; i++) {
        particles.push({
            x: Math.random() * width,
            y: Math.random() * height,
            radius: Math.random() * 2,
            vx: (Math.random() - 0.5) * 0.5,
            vy: (Math.random() - 0.5) * 0.5,
            color: Math.random() > 0.5 ? '#00AAFF' : '#B803F0'
        });
    }
    
    function drawParticles() {
        ctx.clearRect(0, 0, width, height);
        
        particles.forEach(particle => {
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
            particles.forEach(otherParticle => {
                const dx = particle.x - otherParticle.x;
                const dy = particle.y - otherParticle.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 100) {
                    ctx.beginPath();
                    ctx.moveTo(particle.x, particle.y);
                    ctx.lineTo(otherParticle.x, otherParticle.y);
                    ctx.strokeStyle = `rgba(0, 170, 255, ${1 - distance / 100})`;
                    ctx.lineWidth = 0.5;
                    ctx.stroke();
                }
            });
        });
        
        requestAnimationFrame(drawParticles);
    }
    
    drawParticles();
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
        
        setTimeout(() => {
            button.innerHTML = originalHTML;
            button.style.background = '';
            button.style.borderColor = '';
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy:', err);
        alert('Failed to copy. Please select and copy manually.');
    });
}

// =============================================
// FEATURE BOX HOVER EFFECTS
// =============================================
$('.feature-box').hover(
    function() {
        $(this).find('i').addClass('animate__animated animate__bounce');
    },
    function() {
        $(this).find('i').removeClass('animate__animated animate__bounce');
    }
);

// =============================================
// SCROLL REVEAL ANIMATIONS
// =============================================
function revealOnScroll() {
    const reveals = document.querySelectorAll('.feature-box, .setup-step');
    
    reveals.forEach(element => {
        const windowHeight = window.innerHeight;
        const elementTop = element.getBoundingClientRect().top;
        const elementVisible = 150;
        
        if (elementTop < windowHeight - elementVisible) {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }
    });
}

// Set initial state
document.querySelectorAll('.feature-box, .setup-step').forEach(element => {
    element.style.opacity = '0';
    element.style.transform = 'translateY(30px)';
    element.style.transition = 'all 0.6s ease';
});

window.addEventListener('scroll', revealOnScroll);
revealOnScroll(); // Initial check

// =============================================
// CONSOLE MESSAGE
// =============================================
console.log('%c🤖 Buddy AI Assistant', 'font-size: 24px; font-weight: bold; background: linear-gradient(135deg, #00AAFF, #B803F0); -webkit-background-clip: text; color: transparent;');
console.log('%cGitHub: https://github.com/Rathore-Rajpal/HeyBuddy', 'font-size: 14px; color: #00AAFF;');
console.log('%cMade with ❤️ by Rajpal Singh Rathore', 'font-size: 12px; color: #B803F0;');