// FIXED Itinerary Builder - Actually generates real itineraries
document.addEventListener('DOMContentLoaded', function() {
    console.log('FIXED Itinerary builder loaded');
    
    // State
    let selections = {
        duration: null,
        budget: null,
        interests: [],
        style: null
    };
    
    // Make ALL steps visible (remove greyed out look)
    document.querySelectorAll('.step').forEach(step => {
        step.classList.add('active'); // Make all steps active/visible
    });
    
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
        console.log('Current selections:', selections);
        if (selections.duration && selections.budget && selections.interests.length > 0 && selections.style) {
            console.log('All selections made, generating REAL itinerary');
            generateRealItinerary();
        }
    }
    
    function generateRealItinerary() {
        const resultDiv = document.getElementById('itineraryResult');
        const dayByDayDiv = document.getElementById('dayByDay');
        
        if (!resultDiv || !dayByDayDiv) {
            console.error('Missing result elements');
            return;
        }
        
        // Update summary with formatted text
        document.getElementById('resultDuration').textContent = selections.duration + ' days';
        document.getElementById('resultBudget').textContent = formatBudget(selections.budget);
        document.getElementById('resultInterests').textContent = formatInterests(selections.interests);
        document.getElementById('resultStyle').textContent = formatStyle(selections.style);
        
        // Generate REAL day-by-day content
        const days = parseInt(selections.duration);
        let html = '<h4>Your Personalized Australia Itinerary</h4>';
        
        // Generate actual itinerary based on selections
        const itinerary = generateItineraryDetails(days, selections.budget, selections.interests, selections.style);
        
        for (let day = 1; day <= days; day++) {
            const dayContent = getDayContent(day, days, selections.budget, selections.interests, selections.style);
            html += `
                <div class="day-card">
                    <div class="day-header">
                        <h5>Day ${day}: ${getDayTitle(day, days, selections.interests)}</h5>
                    </div>
                    <div class="day-content">
                        ${dayContent}
                        <div class="day-cost">
                            <strong>Estimated cost:</strong> ${getDailyCost(selections.budget)}
                        </div>
                    </div>
                </div>
            `;
        }
        
        // Add booking section
        html += `
            <div class="booking-section mt-4">
                <h5>Ready to Book Your Trip?</h5>
                <p>This itinerary is ready to book with our trusted partners:</p>
                <div class="booking-links">
                    <a href="https://www.skyscanner.com" target="_blank" class="btn-primary" rel="nofollow">
                        <i class="fas fa-plane"></i> Find Flights
                    </a>
                    <a href="https://www.booking.com" target="_blank" class="btn-secondary" rel="nofollow">
                        <i class="fas fa-hotel"></i> Book Accommodation
                    </a>
                    <a href="https://www.viator.com" target="_blank" class="btn-primary" rel="nofollow">
                        <i class="fas fa-ticket-alt"></i> Reserve Tours
                    </a>
                </div>
            </div>
        `;
        
        dayByDayDiv.innerHTML = html;
        resultDiv.style.display = 'block';
        resultDiv.scrollIntoView({ behavior: 'smooth' });
        
        console.log('Real itinerary generated successfully');
    }
    
    function formatBudget(budget) {
        const budgets = {
            'budget': 'Budget ($80-150/day)',
            'mid': 'Mid-Range ($150-300/day)',
            'luxury': 'Luxury ($300+/day)'
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
            'fast': 'Fast-paced (packed schedule)',
            'moderate': 'Moderate (balanced)',
            'relaxed': 'Relaxed (leisurely)'
        };
        return styles[style] || style;
    }
    
    function getDayTitle(day, totalDays, interests) {
        // Special titles for first and last days
        if (day === 1) return 'Arrival in Australia';
        if (day === totalDays) return 'Departure';
        
        // Titles based on interests
        const primaryInterest = interests[0] || 'beaches';
        const titles = {
            'beaches': ['Coastal Exploration', 'Beach Day', 'Island Adventure', 'Marine Discovery', 'Surf & Sun'],
            'nature': ['Wildlife Encounter', 'National Park Hike', 'Rainforest Walk', 'Mountain Views', 'Conservation Experience'],
            'cities': ['City Tour', 'Cultural Immersion', 'Museum Day', 'Urban Exploration', 'Local Markets'],
            'adventure': ['Outback Adventure', 'Water Sports', 'Mountain Biking', 'Scenic Flight', 'Extreme Sports'],
            'food': ['Wine Tasting', 'Food Tour', 'Market Visit', 'Cooking Class', 'Fine Dining']
        };
        
        const dayTitles = titles[primaryInterest] || titles['beaches'];
        return dayTitles[(day - 2) % dayTitles.length];
    }
    
    function getDayContent(day, totalDays, budget, interests, style) {
        const primaryInterest = interests[0] || 'beaches';
        
        // Different content for each interest
        const content = {
            'beaches': [
                'Start with a morning surf lesson at Bondi Beach, followed by the famous Bondi to Coogee coastal walk. Enjoy lunch at a beachfront cafe.',
                'Take a day trip to the Whitsunday Islands. Sail around the islands, snorkel in the Great Barrier Reef, and relax on Whitehaven Beach.',
                'Explore Rottnest Island by bicycle. Meet the famous quokkas, snorkel in crystal clear waters, and enjoy island life.',
                'Visit Phillip Island for the penguin parade. During the day, explore the Nobbies and seal rocks, then watch penguins return at dusk.',
                'Spend a day at Wineglass Bay in Freycinet National Park. Hike to the lookout, then relax on one of the world\'s best beaches.'
            ],
            'nature': [
                'Experience Uluru at sunrise, then complete the base walk around this sacred monolith. Learn about Aboriginal culture from local guides.',
                'Explore the Blue Mountains. See the Three Sisters, ride the scenic railway, and hike through ancient rainforest.',
                'Visit Kangaroo Island for wildlife spotting. See sea lions at Seal Bay, kangaroos, koalas, and the Remarkable Rocks.',
                'Take a guided tour of the Daintree Rainforest, the world\'s oldest tropical rainforest. Look for cassowaries and cruise the Daintree River.',
                'Hike the Dove Lake circuit at Cradle Mountain. This 6km walk offers stunning views of the mountain and surrounding wilderness.'
            ],
            'cities': [
                'Tour the Sydney Opera House, then climb the Harbour Bridge for panoramic views. Finish with dinner at Circular Quay.',
                'Explore Melbourne\'s famous laneways. Discover street art in Hosier Lane, coffee in Degraves Street, and boutiques in Centre Place.',
                'Visit Brisbane\'s South Bank. Enjoy the man-made beach, Queensland Museum, and Gallery of Modern Art, then take a CityCat ferry ride.',
                'Discover Perth\'s Kings Park with views over the city and Swan River. Then explore Fremantle\'s historic port and markets.',
                'Experience Hobart\'s MONA museum, then visit Salamanca Market (Saturday) and climb Mount Wellington for city views.'
            ],
            'adventure': [
                'Scuba dive on the Great Barrier Reef. Explore coral gardens and see tropical fish, turtles, and maybe even reef sharks.',
                'Go skydiving over Mission Beach. Experience freefall with views of the reef and rainforest before landing on the beach.',
                'Take a 4WD tour through the Australian Outback. Visit remote stations, see ancient landscapes, and experience true wilderness.',
                'Try white water rafting on the Tully River in Queensland. Navigate grade 3-4 rapids through rainforest surroundings.',
                'Take a helicopter flight over the Twelve Apostles. See these iconic limestone stacks from the air along the Great Ocean Road.'
            ],
            'food': [
                'Tour the Sydney Fish Market. Enjoy fresh seafood, then take a cooking class to learn Australian seafood preparation.',
                'Explore Melbourne\'s coffee culture. Visit specialty roasters, learn about coffee brewing, and enjoy laneway cafes.',
                'Spend a day in the Barossa Valley. Visit wineries like Penfolds and Jacob\'s Creek, and enjoy local produce at the farmers market.',
                'Discover the Margaret River region. Taste premium wines, visit artisan cheese producers, and enjoy farm-to-table dining.',
                'Tour Tasmania\'s whisky distilleries and cheese makers. Sample cool-climate wines and fresh seafood from local waters.'
            ]
        };
        
        const dayContent = content[primaryInterest] || content['beaches'];
        return `<p>${dayContent[(day - 1) % dayContent.length]}</p>`;
    }
    
    function getDailyCost(budget) {
        const costs = {
            'budget': 'AUD $80-150 (hostels, public transport, self-catering)',
            'mid': 'AUD $150-300 (hotels, some tours, restaurant meals)',
            'luxury': 'AUD $300+ (premium hotels, private tours, fine dining)'
        };
        return costs[budget] || 'AUD $150-250';
    }
    
    function generateItineraryDetails(days, budget, interests, style) {
        // This would generate a complete itinerary structure
        return {
            title: `${formatInterests(interests)} Australia Adventure`,
            summary: `${days}-day ${formatBudget(budget)} trip focusing on ${formatInterests(interests)} at a ${formatStyle(style)} pace.`,
            dailyActivities: []
        };
    }
    
    // GLOBAL FUNCTION for quick select
    window.selectQuickTrip = function(tripType) {
        console.log('QUICK TRIP SELECTED:', tripType);
        
        // Reset all
        selections = { duration: null, budget: null, interests: [], style: null };
        document.querySelectorAll('.duration-btn, .budget-btn, .interest-btn, .style-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        
        // Helper
        function clickBtn(selector) {
            const btn = document.querySelector(selector);
            if (btn) {
                btn.click();
                console.log('Clicked:', selector);
            } else {
                console.warn('Button not found:', selector);
            }
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
        
        // Scroll to builder
        const builder = document.querySelector('.itinerary-builder');
        if (builder) builder.scrollIntoView({ behavior: 'smooth' });
        
        // Show confirmation
        const tripNames = {
            'east-coast': 'East Coast Adventure',
            'outback': 'Outback Explorer',
            'family': 'Family Australia Trip',
            'working-holiday': 'Working Holiday Experience',
            'luxury': 'Luxury Australian Getaway',
            'budget': 'Budget Backpacker Adventure'
        };
        
        alert(`${tripNames[tripType]} selected! Builder pre-filled. Make any adjustments and click generate.`);
    };
    
    console.log('FIXED itinerary builder ready');
});