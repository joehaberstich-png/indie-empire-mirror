// FlyToAustralia.com - Main JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
            if (navLinks.style.display === 'flex') {
                navLinks.style.flexDirection = 'column';
                navLinks.style.position = 'absolute';
                navLinks.style.top = '100%';
                navLinks.style.left = '0';
                navLinks.style.right = '0';
                navLinks.style.backgroundColor = 'white';
                navLinks.style.padding = '20px';
                navLinks.style.boxShadow = '0 10px 20px rgba(0,0,0,0.1)';
                navLinks.style.gap = '15px';
            }
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!menuToggle.contains(event.target) && !navLinks.contains(event.target)) {
                if (window.innerWidth <= 768) {
                    navLinks.style.display = 'none';
                }
            }
        });
    }
    
    // Newsletter form submission
    const newsletterForm = document.querySelector('.newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            
            // Simple validation
            if (email && email.includes('@')) {
                // In a real site, this would send to a server
                alert('Thank you for subscribing to Australia travel updates!');
                this.reset();
            } else {
                alert('Please enter a valid email address.');
            }
        });
    }
    
    // Search functionality
    const searchBox = document.querySelector('.search-box');
    if (searchBox) {
        const searchInput = searchBox.querySelector('input');
        const searchButton = searchBox.querySelector('button');
        
        searchButton.addEventListener('click', function() {
            performSearch(searchInput.value);
        });
        
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                performSearch(this.value);
            }
        });
        
        function performSearch(query) {
            if (query.trim()) {
                // In a real site, this would redirect to search results
                alert(`Searching for: "${query}"\n\nThis is a demo site. In a real implementation, this would show search results.`);
                searchInput.value = '';
            }
        }
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add current year to footer
    const currentYear = new Date().getFullYear();
    document.querySelectorAll('.current-year').forEach(element => {
        element.textContent = currentYear;
    });
    
    // Card hover effects
    const cards = document.querySelectorAll('.destination-card, .resource-card, .article-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s ease';
        });
    });
    
    // Initialize any tooltips or popovers
    initializeTooltips();
});

function initializeTooltips() {
    // Simple tooltip implementation for affiliate links
    const affiliateLinks = document.querySelectorAll('a[rel="nofollow"]');
    affiliateLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            // Could add tooltip about affiliate disclosure
        });
    });
}

// Responsive adjustments
window.addEventListener('resize', function() {
    const navLinks = document.querySelector('.nav-links');
    if (window.innerWidth > 768 && navLinks) {
        navLinks.style.display = 'flex';
        navLinks.style.flexDirection = 'row';
        navLinks.style.position = 'static';
        navLinks.style.backgroundColor = 'transparent';
        navLinks.style.padding = '0';
        navLinks.style.boxShadow = 'none';
    } else if (window.innerWidth <= 768 && navLinks) {
        navLinks.style.display = 'none';
    }
});