// SIMPLE Itinerary Builder - Guaranteed to work
document.addEventListener('DOMContentLoaded', function() {
    console.log('Itinerary builder loaded - SIMPLE VERSION');
    
    // State
    let selections = {
        duration: null,
        budget: null,
        interests: [],
        style: null
    };
    
    // Button click handlers
    document.querySelectorAll('.duration-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.duration-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            selections.duration = this.dataset.days;
            checkAllSelected();
        });
    });
    
    document.querySelectorAll('.budget-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.budget-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            selections.budget = this.dataset.budget;
            checkAllSelected();
        });
    });
    
    document.querySelectorAll('.interest-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const interest = this.dataset.interest;
            if (this.classList.contains('active')) {
                this.classList.remove('active');
                selections.interests = selections.interests.filter(i => i !== interest);
            } else {
                this.classList.add('active');
                selections.interests.push(interest);
            }
            checkAllSelected();
        });
    });
    
    document.querySelectorAll('.style-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.style-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            selections.style = this.dataset.style;
            checkAllSelected();
        });
    });
    
    function checkAllSelected() {
        if (selections.duration && selections.budget && selections.interests.length > 0 && selections.style) {
            generateItinerary();
        }
    }
    
    function generateItinerary() {
        const resultDiv = document.getElementById('itineraryResult');
        const dayByDayDiv = document.getElementById('dayByDay');
        
        if (!resultDiv || !dayByDayDiv) return;
        
        // Update summary
        document.getElementById('resultDuration').textContent = selections.duration + ' days';
        document.getElementById('resultBudget').textContent = selections.budget;
        document.getElementById('resultInterests').textContent = selections.interests.join(', ');
        document.getElementById('resultStyle').textContent = selections.style;
        
        // Generate content
        let html = '<h4>Your Australian Adventure</h4>';
        const days = parseInt(selections.duration);
        
        for (let day = 1; day <= days; day++) {
            html += `
                <div class="day-card">
                    <div class="day-header">
                        <h5>Day ${day}</h5>
                    </div>
                    <div class="day-content">
                        <p>Explore Australia's ${selections.interests[0]} with a ${selections.style} pace on a ${selections.budget} budget.</p>
                    </div>
                </div>
            `;
        }
        
        dayByDayDiv.innerHTML = html;
        resultDiv.style.display = 'block';
        resultDiv.scrollIntoView({ behavior: 'smooth' });
    }
    
    // GLOBAL FUNCTION for quick select
    window.selectQuickTrip = function(tripType) {
        console.log('QUICK TRIP SELECTED:', tripType);
        
        // Reset
        selections = { duration: null, budget: null, interests: [], style: null };
        document.querySelectorAll('.duration-btn, .budget-btn, .interest-btn, .style-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        
        // Helper to click buttons
        function clickBtn(selector) {
            const btn = document.querySelector(selector);
            if (btn) btn.click();
        }
        
        // Pre-fill based on trip type
        switch(tripType) {
            case 'east-coast':
                clickBtn('.duration-btn[data-days="14"]');
                clickBtn('.budget-btn[data-budget="mid"]');
                clickBtn('.interest-btn[data-interest="beaches"]');
                clickBtn('.interest-btn[data-interest="cities"]');
                clickBtn('.style-btn[data-style="moderate"]');
                break;
            case 'outback':
                clickBtn('.duration-btn[data-days="7"]');
                clickBtn('.budget-btn[data-budget="mid"]');
                clickBtn('.interest-btn[data-interest="nature"]');
                clickBtn('.interest-btn[data-interest="adventure"]');
                clickBtn('.style-btn[data-style="moderate"]');
                break;
            case 'family':
                clickBtn('.duration-btn[data-days="14"]');
                clickBtn('.budget-btn[data-budget="mid"]');
                clickBtn('.interest-btn[data-interest="beaches"]');
                clickBtn('.interest-btn[data-interest="nature"]');
                clickBtn('.style-btn[data-style="relaxed"]');
                break;
            case 'working-holiday':
                clickBtn('.duration-btn[data-days="35"]');
                clickBtn('.budget-btn[data-budget="budget"]');
                clickBtn('.interest-btn[data-interest="beaches"]');
                clickBtn('.interest-btn[data-interest="cities"]');
                clickBtn('.interest-btn[data-interest="adventure"]');
                clickBtn('.style-btn[data-style="moderate"]');
                break;
            case 'luxury':
                clickBtn('.duration-btn[data-days="14"]');
                clickBtn('.budget-btn[data-budget="luxury"]');
                clickBtn('.interest-btn[data-interest="beaches"]');
                clickBtn('.interest-btn[data-interest="food"]');
                clickBtn('.style-btn[data-style="relaxed"]');
                break;
            case 'budget':
                clickBtn('.duration-btn[data-days="21"]');
                clickBtn('.budget-btn[data-budget="budget"]');
                clickBtn('.interest-btn[data-interest="beaches"]');
                clickBtn('.interest-btn[data-interest="nature"]');
                clickBtn('.style-btn[data-style="fast"]');
                break;
        }
        
        // Scroll and alert
        const builder = document.querySelector('.itinerary-builder');
        if (builder) builder.scrollIntoView({ behavior: 'smooth' });
        
        const names = {
            'east-coast': 'East Coast',
            'outback': 'Outback',
            'family': 'Family Trip',
            'working-holiday': 'Working Holiday',
            'luxury': 'Luxury',
            'budget': 'Budget'
        };
        
        alert(names[tripType] + ' trip selected! Builder pre-filled.');
    };
    
    console.log('selectQuickTrip function available:', typeof window.selectQuickTrip);
});