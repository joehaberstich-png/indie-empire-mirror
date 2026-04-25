// Itinerary Builder - Fixed and Working
document.addEventListener('DOMContentLoaded', function() {
    console.log('Itinerary builder loaded');
    
    // Get all buttons
    const durationBtns = document.querySelectorAll('.duration-btn');
    const budgetBtns = document.querySelectorAll('.budget-btn');
    const interestBtns = document.querySelectorAll('.interest-btn');
    const styleBtns = document.querySelectorAll('.style-btn');
    const resultDiv = document.getElementById('itineraryResult');
    const dayByDayDiv = document.getElementById('dayByDay');
    const printBtn = document.getElementById('printItinerary');
    const saveBtn = document.getElementById('saveItinerary');
    
    // State
    let selections = {
        duration: null,
        budget: null,
        interests: [],
        style: null
    };
    
    // Add click handlers to duration buttons
    durationBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            console.log('Duration clicked:', this.dataset.days);
            durationBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            selections.duration = this.dataset.days;
            checkAllSelected();
        });
    });
    
    // Add click handlers to budget buttons
    budgetBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            console.log('Budget clicked:', this.dataset.budget);
            budgetBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            selections.budget = this.dataset.budget;
            checkAllSelected();
        });
    });
    
    // Add click handlers to interest buttons (multiple selection)
    interestBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            console.log('Interest clicked:', this.dataset.interest);
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
    
    // Add click handlers to style buttons
    styleBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            console.log('Style clicked:', this.dataset.style);
            styleBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            selections.style = this.dataset.style;
            checkAllSelected();
        });
    });
    
    // Print button handler
    if (printBtn) {
        printBtn.addEventListener('click', function() {
            window.print();
        });
    }
    
    // Save button handler
    if (saveBtn) {
        saveBtn.addEventListener('click', function() {
            alert('Itinerary saved! (This would normally save to your account)');
        });
    }
    
    function checkAllSelected() {
        console.log('Checking selections:', selections);
        
        // Check if all required fields are selected
        if (selections.duration && selections.budget && selections.interests.length > 0 && selections.style) {
            console.log('All selections made, generating itinerary');
            generateItinerary();
        }
    }
    
    function generateItinerary() {
        console.log('Generating itinerary with:', selections);
        
        // Update result summary
        document.getElementById('resultDuration').textContent = selections.duration + ' days';
        document.getElementById('resultBudget').textContent = formatBudget(selections.budget);
        document.getElementById('resultInterests').textContent = formatInterests(selections.interests);
        document.getElementById('resultStyle').textContent = formatStyle(selections.style);
        
        // Generate day-by-day content
        const daysContent = generateDayContent();
        dayByDayDiv.innerHTML = daysContent;
        
        // Show result section
        resultDiv.style.display = 'block';
        
        // Scroll to results
        resultDiv.scrollIntoView({ behavior: 'smooth' });
    }
    
    function formatBudget(budget) {
        const budgets = {
            'budget': 'Budget (Backpacker)',
            'mid': 'Mid-Range',
            'luxury': 'Luxury'
        };
        return budgets[budget] || budget;
    }
    
    function formatInterests(interests) {
        const interestNames = {
            'beaches': 'Beaches & Coast',
            'nature': 'Nature & Wildlife',
            'cities': 'Cities & Culture',
            'adventure': 'Adventure & Outdoors',
            'food': 'Food & Wine'
        };
        return interests.map(i => interestNames[i] || i).join(', ');
    }
    
    function formatStyle(style) {
        const styles = {
            'fast': 'Fast-paced',
            'moderate': 'Moderate pace',
            'relaxed': 'Relaxed pace'
        };
        return styles[style] || style;
    }
    
    function generateDayContent() {
        const days = parseInt(selections.duration);
        const budget = selections.budget;
        const interests = selections.interests;
        const style = selections.style;
        
        // Create unique tour name
        const tourNames = {
            'beaches-budget-fast': 'East Coast Surf Adventure',
            'beaches-mid-moderate': 'Coastal Explorer', 
            'beaches-luxury-relaxed': 'Luxury Beach Retreat',
            'nature-budget-moderate': 'National Parks Explorer',
            'nature-mid-relaxed': 'Wildlife & Wilderness',
            'nature-luxury-moderate': 'Premium Nature Experience',
            'cities-budget-fast': 'City Highlights Express',
            'cities-mid-moderate': 'Urban Culture Explorer',
            'cities-luxury-relaxed': 'Luxury City Break',
            'adventure-budget-fast': 'Outback Adventure Rush',
            'adventure-mid-relaxed': 'Active Australia',
            'food-mid-moderate': 'Foodie Trail'
        };
        
        const key = `${interests[0] || 'beaches'}-${budget}-${style}`;
        const tourName = tourNames[key] || `${formatBudget(budget)} ${formatInterests([interests[0] || 'beaches'])} Tour`;
        
        let html = `<h4>${tourName}</h4>`;
        
        // Generate day-by-day itinerary based on selections
        for (let day = 1; day <= days; day++) {
            html += generateDay(day, days, budget, interests, style);
        }
        
        // Add booking section
        html += `
            <div class="booking-section">
                <h5>Ready to Book?</h5>
                <p>This itinerary includes estimated costs and booking links:</p>
                <div class="booking-links">
                    <a href="https://www.booking.com" target="_blank" class="btn-primary" rel="nofollow">
                        <i class="fas fa-hotel"></i> Book Accommodation
                    </a>
                    <a href="https://www.skyscanner.com" target="_blank" class="btn-secondary" rel="nofollow">
                        <i class="fas fa-plane"></i> Find Flights
                    </a>
                    <a href="https://www.viator.com" target="_blank" class="btn-primary" rel="nofollow">
                        <i class="fas fa-ticket-alt"></i> Book Tours
                    </a>
                </div>
            </div>
        `;
        
        return html;
    }
    
    function generateDay(day, totalDays, budget, interests, style) {
        // Different content based on interests
        let dayContent = '';
        
        if (interests.includes('beaches')) {
            dayContent = getBeachDay(day, totalDays, budget, style);
        } else if (interests.includes('nature')) {
            dayContent = getNatureDay(day, totalDays, budget, style);
        } else if (interests.includes('cities')) {
            dayContent = getCityDay(day, totalDays, budget, style);
        } else if (interests.includes('adventure')) {
            dayContent = getAdventureDay(day, totalDays, budget, style);
        } else if (interests.includes('food')) {
            dayContent = getFoodDay(day, totalDays, budget, style);
        } else {
            dayContent = getDefaultDay(day, totalDays, budget, style);
        }
        
        // Add budget-specific notes
        let budgetNote = '';
        if (budget === 'budget') {
            budgetNote = '<p><em>Budget tip: Hostels and public transport recommended</em></p>';
        } else if (budget === 'mid') {
            budgetNote = '<p><em>Mid-range: Comfortable hotels and some guided tours</em></p>';
        } else {
            budgetNote = '<p><em>Luxury: Premium hotels and private experiences</em></p>';
        }
        
        // Add style-specific notes
        let styleNote = '';
        if (style === 'fast') {
            styleNote = '<p><strong>Fast-paced:</strong> Packed schedule with multiple activities</p>';
        } else if (style === 'moderate') {
            styleNote = '<p><strong>Moderate pace:</strong> Balanced mix of activities and relaxation</p>';
        } else {
            styleNote = '<p><strong>Relaxed pace:</strong> Leisurely schedule with downtime</p>';
        }
        
        return `
            <div class="day-card">
                <div class="day-header">
                    <h5>Day ${day}: ${getDayTitle(day, totalDays, interests)}</h5>
                </div>
                <div class="day-content">
                    ${dayContent}
                    ${budgetNote}
                    ${styleNote}
                    <div class="day-cost">
                        <strong>Estimated daily cost:</strong> ${getDailyCost(budget)}
                    </div>
                </div>
            </div>
        `;
    }
    
    function getDayTitle(day, totalDays, interests) {
        const titles = {
            1: 'Arrival & Orientation',
            2: 'Exploring the Region',
            [totalDays]: 'Departure Day'
        };
        
        if (titles[day]) return titles[day];
        
        if (interests.includes('beaches')) {
            const beachTitles = ['Coastal Drive', 'Beach Day', 'Island Hopping', 'Surf Lesson', 'Marine Exploration'];
            return beachTitles[(day - 2) % beachTitles.length];
        } else if (interests.includes('nature')) {
            const natureTitles = ['National Park Visit', 'Wildlife Spotting', 'Rainforest Walk', 'Mountain Hike', 'Conservation Experience'];
            return natureTitles[(day - 2) % natureTitles.length];
        } else if (interests.includes('cities')) {
            const cityTitles = ['City Tour', 'Museum Day', 'Cultural Experience', 'Shopping & Dining', 'Local Neighborhoods'];
            return cityTitles[(day - 2) % cityTitles.length];
        }
        
        return 'Exploring Australia';
    }
    
    function getBeachDay(day, totalDays, budget, style) {
        const activities = [
            'Morning surf lesson at Bondi Beach',
            'Great Barrier Reef snorkeling tour',
            'Whitehaven Beach day trip in the Whitsundays',
            'Coastal walk from Bondi to Coogee',
            'Phillip Island penguin parade',
            'Byron Bay lighthouse walk and beach time',
            'Rottnest Island cycling and quokka spotting',
            'Wineglass Bay hike in Freycinet National Park'
        ];
        
        return `<p>${activities[(day - 1) % activities.length]}. Enjoy Australia\'s stunning coastline with crystal clear waters and golden sands.</p>`;
    }
    
    function getNatureDay(day, totalDays, budget, style) {
        const activities = [
            'Uluru sunrise viewing and base walk',
            'Blue Mountains Three Sisters and scenic world',
            'Kangaroo Island wildlife experience',
            'Daintree Rainforest guided tour',
            'Cradle Mountain Dove Lake circuit',
            'Kakadu National Park wetlands cruise',
            'Grampians National Park hiking',
            'Great Ocean Road and Twelve Apostles'
        ];
        
        return `<p>${activities[(day - 1) % activities.length]}. Experience Australia\'s unique wildlife and breathtaking natural landscapes.</p>`;
    }
    
    function getCityDay(day, totalDays, budget, style) {
        const activities = [
            'Sydney Opera House tour and Harbour Bridge climb',
            'Melbourne laneways and street art exploration',
            'Brisbane South Bank and cultural precinct',
            'Perth Kings Park and Swan River cruise',
            'Adelaide Central Market and wine regions',
            'Canberra Parliament House and national museums',
            'Hobart MONA museum and Salamanca Market',
            'Darwin waterfront and Mindil Beach markets'
        ];
        
        return `<p>${activities[(day - 1) % activities.length]}. Discover Australia\'s vibrant cities with rich culture and history.</p>`;
    }
    
    function getAdventureDay(day, totalDays, budget, style) {
        const activities = [
            'Scuba diving on the Great Barrier Reef',
            'Skydiving over Mission Beach',
            '4WD tour in the Australian Outback',
            'Hot air balloon ride over the Yarra Valley',
            'White water rafting on the Tully River',
            'Helicopter flight over the Twelve Apostles',
            'Bungee jumping in Cairns',
            'Mountain biking in the Blue Mountains'
        ];
        
        return `<p>${activities[(day - 1) % activities.length]}. Get your adrenaline pumping with Australian adventure activities.</p>`;
    }
    
    function getFoodDay(day, totalDays, budget, style) {
        const activities = [
            'Sydney Fish Market seafood experience',
            'Melbourne coffee culture and laneway dining',
            'Barossa Valley wine tasting tour',
            'Margaret River food and wine trail',
            'Hunter Valley gourmet experience',
            'Tasmanian whisky and cheese tasting',
            'Adelaide Central Market food tour',
            'Byron Bay farm-to-table dining'
        ];
        
        return `<p>${activities[(day - 1) % activities.length]}. Savor Australia\'s world-class food and wine scene.</p>`;
    }
    
    function getDefaultDay(day, totalDays, budget, style) {
        const activities = [
            'Explore local attractions and landmarks',
            'Guided tour of the area',
            'Free time for personal exploration',
            'Cultural and historical sites',
            'Relaxation and leisure activities',
            'Shopping and local markets',
            'Evening entertainment and dining'
        ];
        
        return `<p>${activities[(day - 1) % activities.length]}. Enjoy your Australian adventure at your own pace.</p>`;
    }
    
    function getDailyCost(budget) {
        const costs = {
            'budget': 'AUD $80-150 per person',
            'mid': 'AUD $200-350 per person',
            'luxury': 'AUD $500+ per person'
        };
        return costs[budget] || 'AUD $150-300 per person';
    }
    
    // Quick trip selection function - GLOBAL SCOPE
    window.selectQuickTrip = function(tripType) {
        console.log('Quick trip selected:', tripType);
        
        // Reset all selections
        selections = {
            duration: null,
            budget: null,
            interests: [],
            style: null
        };
        
        // Remove active classes from all buttons
        document.querySelectorAll('.duration-btn, .budget-btn, .interest-btn, .style-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        
        // Helper function to click buttons
        function clickButton(selector) {
            const button = document.querySelector(selector);
            if (button) {
                button.click();
            }
        }
        
        // Set selections based on trip type
        switch(tripType) {
            case 'east-coast':
                clickButton('.duration-btn[data-days="14"]');
                clickButton('.budget-btn[data-budget="mid"]');
                clickButton('.interest-btn[data-interest="beaches"]');
                clickButton('.interest-btn[data-interest="cities"]');
                clickButton('.style-btn[data-style="moderate"]');
                break;
            case 'outback':
                clickButton('.duration-btn[data-days="7"]');
                clickButton('.budget-btn[data-budget="mid"]');
                clickButton('.interest-btn[data-interest="nature"]');
                clickButton('.interest-btn[data-interest="adventure"]');
                clickButton('.style-btn[data-style="moderate"]');
                break;
            case 'family':
                clickButton('.duration-btn[data-days="14"]');
                clickButton('.budget-btn[data-budget="mid"]');
                clickButton('.interest-btn[data-interest="beaches"]');
                clickButton('.interest-btn[data-interest="nature"]');
                clickButton('.style-btn[data-style="relaxed"]');
                break;
            case 'working-holiday':
                clickButton('.duration-btn[data-days="35"]');
                clickButton('.budget-btn[data-budget="budget"]');
                clickButton('.interest-btn[data-interest="beaches"]');
                clickButton('.interest-btn[data-interest="cities"]');
                clickButton('.interest-btn[data-interest="adventure"]');
                clickButton('.style-btn[data-style="moderate"]');
                break;
            case 'luxury':
                clickButton('.duration-btn[data-days="14"]');
                clickButton('.budget-btn[data-budget="luxury"]');
                clickButton('.interest-btn[data-interest="beaches"]');
                clickButton('.interest-btn[data-interest="food"]');
                clickButton('.style-btn[data-style="relaxed"]');
                break;
            case 'budget':
                clickButton('.duration-btn[data-days="21"]');
                clickButton('.budget-btn[data-budget="budget"]');
                clickButton('.interest-btn[data-interest="beaches"]');
                clickButton('.interest-btn[data-interest="nature"]');
                clickButton('.style-btn[data-style="