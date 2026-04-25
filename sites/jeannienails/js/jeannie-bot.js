/**
 * Jeannie Nails — Quantum Sales & Scheduling Bot
 * Browser-based chat widget with full service knowledge.
 * Injected on every page.
 */
(function() {
    'use strict';
    
    const CONFIG = {
        siteName: 'Jeannie Nails',
        phone: '(902) 885-7896',
        phoneLink: 'tel:+19028857896',
        timezone: 'Atlantic Canada',
        facebook: 'https://www.facebook.com/jeanniesnails17',
        branding: '⚡ Powered by Quantum Bots Agency → quantumbotsagency.com'
    };

    const SCHEDULE = {
        1: { day: 'Monday',    status: 'closed' },
        2: { day: 'Tuesday',   status: 'open',  hours: '10:00 AM – 5:00 PM' },
        3: { day: 'Wednesday', status: 'open',  hours: '10:00 AM – 6:00 PM' },
        4: { day: 'Thursday',  status: 'open',  hours: '10:00 AM – 6:00 PM' },
        5: { day: 'Friday',    status: 'open',  hours: '10:00 AM – 4:00 PM' },
        6: { day: 'Saturday',  status: 'closed' },
        7: { day: 'Sunday',    status: 'closed' }
    };

    const DAYS_DISPLAY = 'Tue 10-5 • Wed/Thu 10-6 • Fri 10-4';

    const SERVICES = {
        ingrown_toenail: { name: '🦶 Ingrown Toenail Correction', desc: 'Professional Onyx treatment — fast relief & lasting results. ★ Specialty!', duration: '30 min', category: 'specialty' },
        manicure: { name: '💅 Manicure', desc: 'Classic and spa manicure — shape, cuticle care, polish.', duration: '30 min', category: 'nails' },
        pedicure: { name: '🦶 Pedicure', desc: 'Relaxing foot care — classic, spa, or deluxe.', duration: '45 min', category: 'nails' },
        gel_nails: { name: '✨ Gel Nails', desc: 'Long-lasting high-gloss color. Lasts 2-3 weeks.', duration: '45 min', category: 'nails' },
        extensions: { name: '💎 Nail Extensions', desc: 'Custom length, shape & design — gel or acrylic.', duration: '60 min', category: 'nails' },
        waxing: { name: '🪒 Waxing', desc: 'Professional hair removal — brows, lip, face, body.', duration: '15-30 min', category: 'waxing' },
        piercings: { name: '💎 Ear Piercings', desc: 'Safe, sterile, professional. Single or double lobe.', duration: '15 min', category: 'piercing' },
        nail_art: { name: '🎨 Nail Art', desc: 'Custom designs for any occasion.', duration: '30-60 min', category: 'nails' }
    };

    // ─── Intent Detection ───
    function detectIntent(msg) {
        const m = msg.toLowerCase().trim();
        if (/book|appointment|schedule|reserve|when can|available/.test(m)) return 'booking';
        if (/ingrown|toenail|onyx|nail pain|infected toe/.test(m)) return 'ingrown';
        if (/hours|open|close|time|when are|today/.test(m)) return 'hours';
        if (/service|price|cost|how much|list|what do|offer|menu/.test(m)) return 'services';
        if (/piercing|pierce|earring|stud/.test(m)) return 'piercing';
        if (/wax|waxing|hair removal/.test(m)) return 'waxing';
        if (/gel|extension|acrylic/.test(m)) return 'gel_extensions';
        if (/address|location|where|direction|phone|contact|call/.test(m)) return 'contact';
        if (/hi|hello|hey|start|help/.test(m)) return 'greeting';
        return 'general';
    }

    function getQuickReplies(intent) {
        const qr = {
            greeting: ['Book Appointment 📅', 'Services & Pricing 💅', 'Hours 🕐', 'Ingrown Toenail 🦶'],
            hours: ['Book Now 📞', 'Services 📋', 'Contact 📍'],
            services: ['Book Appointment 📅', 'Ingrown Toenail 🦶', 'Hours 🕐'],
            booking: ['Ingrown Toenail 🦶', 'Pedicure 🦶', 'Gel Nails ✨', 'Waxing 🪒', 'Piercing 💎'],
            ingrown: ['Book Now 📞', 'Pedicure 🦶', 'Services 📋'],
            piercing: ['Book Now 📞', 'Services 📋', 'Hours 🕐'],
            waxing: ['Book Now 📞', 'Services 📋', 'Contact 📍'],
            gel_extensions: ['Book Now 📞', 'Nail Art 🎨', 'Manicure 💅'],
            contact: ['Book Now 📞', 'Hours 🕐', 'Services 📋'],
            general: ['Book Now 📞', 'Services 💅', 'Hours 🕐', 'Ingrown Toenail 🦶']
        };
        return qr[intent] || qr.general;
    }

    function generateResponse(intent) {
        const r = {
            greeting: {
                text: `✨ Welcome to <strong>${CONFIG.siteName}</strong>! ✨<br><br>I specialize in ingrown toenail correction (Onyx treatment) plus full nail services — manicures, pedicures, gel nails, extensions, waxing, and ear piercings.<br><br>What can I help you with today?`,
                type: 'greeting'
            },
            hours: {
                text: `🕐 <strong>Hours</strong> (${CONFIG.timezone})<br><br>` +
                    Object.values(SCHEDULE).map(s => 
                        `<span style="${s.status==='closed'?'color:#c0392b':''}">${s.day}</span> ${s.status==='open' ? s.hours : '— Closed'}</span>`
                    ).join('<br>') +
                    `<br><br>📞 Call <a href="${CONFIG.phoneLink}" style="color:#d4a0a0;font-weight:700">${CONFIG.phone}</a> to book!<br><em>Walk-ins welcome — call ahead to check.</em>`,
                type: 'info'
            },
            services: {
                text: `<strong>Our Services</strong><br><br>` +
                    Object.values(SERVICES).map(s => 
                        `<span style="${s.category==='specialty'?'color:#c0392b;font-weight:700':''}">${s.name}</span> — ${s.desc}`
                    ).join('<br><br>') +
                    `<br><br>📞 Call <a href="${CONFIG.phoneLink}" style="color:#d4a0a0;font-weight:700">${CONFIG.phone}</a> for pricing & booking!`,
                type: 'info'
            },
            booking: {
                text: `📅 <strong>Book an Appointment</strong><br><br>Jeannie is available:<br><strong>${DAYS_DISPLAY}</strong> (${CONFIG.timezone})<br><br>📞 <strong>Call or text: <a href="${CONFIG.phoneLink}" style="color:#d4a0a0;font-weight:700">${CONFIG.phone}</a></strong><br><br>Or stop by during business hours — walk-ins welcome!<br><br><em>What service are you looking for?</em>`,
                type: 'booking'
            },
            ingrown: {
                text: `🦶 <strong>Ingrown Toenail Correction</strong><br><br><span style="background:#c0392b;color:#fff;padding:3px 10px;border-radius:100px;font-size:11px;font-weight:700">★ SPECIALTY SERVICE</span><br><br>Suffering from ingrown toenail pain? Jeannie provides professional Onyx treatment for fast, lasting relief.<br><br>✅ Quick procedure (30 min)<br>✅ Minimal discomfort<br>✅ Long-lasting results<br>✅ Professional care<br><br><strong>Walk-ins welcome</strong> for consultations — or call <a href="${CONFIG.phoneLink}" style="color:#d4a0a0;font-weight:700">${CONFIG.phone}</a>.`,
                type: 'specialty'
            },
            piercing: {
                text: `💎 <strong>Ear Piercings</strong><br><br>Professional ear piercing in a clean, sterile environment.<br><br>✅ Single or double lobe<br>✅ Hypoallergenic starter studs<br>✅ Quick & painless<br>✅ Aftercare guidance included<br><br>📞 Call <a href="${CONFIG.phoneLink}" style="color:#d4a0a0;font-weight:700">${CONFIG.phone}</a> to book!`,
                type: 'info'
            },
            waxing: {
                text: `🪒 <strong>Waxing Services</strong><br><br>Professional hair removal — gentle and effective.<br><br>👁️ Brows & lip<br>🦵 Arms & legs<br>🧴 Face<br><br>📞 Call <a href="${CONFIG.phoneLink}" style="color:#d4a0a0;font-weight:700">${CONFIG.phone}</a> for pricing & booking!`,
                type: 'info'
            },
            gel_extensions: {
                text: `✨ <strong>Gel Nails & Extensions</strong><br><br><strong>Gel Nails:</strong> Long-lasting high-gloss color. Lasts 2-3 weeks without chipping.<br><br><strong>Nail Extensions:</strong> Custom length, shape, and design.<br><br>📞 Call <a href="${CONFIG.phoneLink}" style="color:#d4a0a0;font-weight:700">${CONFIG.phone}</a> to book!`,
                type: 'info'
            },
            contact: {
                text: `📞 <strong>Contact & Location</strong><br><br><strong>Phone:</strong> <a href="${CONFIG.phoneLink}" style="color:#d4a0a0;font-weight:700">${CONFIG.phone}</a><br><strong>Hours:</strong> ${DAYS_DISPLAY} (${CONFIG.timezone})<br><br>📱 <a href="${CONFIG.facebook}" target="_blank" style="color:#d4a0a0">Find us on Facebook →</a><br><br><em>Call for address and directions — we'll help you find us!</em>`,
                type: 'contact'
            },
            general: {
                text: `Hi! Thanks for reaching out to <strong>${CONFIG.siteName}</strong> 🎉<br><br>I'm happy to help with:<br>🦶 Ingrown toenail correction <strong>(our specialty!)</strong><br>💅 Manicures & pedicures<br>✨ Gel nails & extensions<br>🪒 Waxing<br>💎 Ear piercings<br>🎨 Custom nail art<br><br>How can I help?`,
                type: 'general'
            }
        };
        return r[intent] || r.general;
    }

    // ─── Chat Widget UI ───
    function injectWidget() {
        if (document.getElementById('jn-chat-widget')) return;

        const css = document.createElement('style');
        css.textContent = `
            #jn-chat-btn{position:fixed;bottom:24px;right:24px;z-index:99999;width:60px;height:60px;border-radius:50%;background:linear-gradient(135deg,#2d1b14,#4a2c2c);border:none;cursor:pointer;box-shadow:0 4px 20px rgba(0,0,0,.25);display:flex;align-items:center;justify-content:center;transition:all .2s}
            #jn-chat-btn:hover{transform:scale(1.05);box-shadow:0 6px 24px rgba(0,0,0,.3)}
            #jn-chat-btn svg{width:28px;height:28px;fill:#fff}
            #jn-chat-panel{position:fixed;bottom:96px;right:24px;z-index:99999;width:360px;max-width:calc(100vw - 48px);height:520px;max-height:calc(100vh - 120px);border-radius:16px;background:#fff;box-shadow:0 8px 40px rgba(0,0,0,.18);display:none;flex-direction:column;overflow:hidden;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
            #jn-chat-header{background:linear-gradient(135deg,#2d1b14,#4a2c2c);color:#fff;padding:14px 16px;display:flex;align-items:center;gap:10px;flex-shrink:0}
            #jn-chat-header-avatar{width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,#d4a0a0,#c0392b);display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0}
            #jn-chat-header-info{flex:1}
            #jn-chat-header-name{font-weight:700;font-size:14px}
            #jn-chat-header-status{font-size:11px;color:#d4b0b0}
            #jn-chat-close{background:none;border:none;color:#d4b0b0;cursor:pointer;font-size:20px;padding:0 4px;line-height:1}
            #jn-chat-messages{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:10px;background:#fdf6f0}
            #jn-chat-messages::-webkit-scrollbar{width:4px}
            #jn-chat-messages::-webkit-scrollbar-thumb{background:#d4a0a0;border-radius:2px}
            .jn-msg{max-width:85%;padding:10px 14px;border-radius:14px;font-size:13.5px;line-height:1.5;animation:jnFadeIn .25s ease}
            .jn-msg.bot{align-self:flex-start;background:#fff;border:1px solid #e8d5d0;border-bottom-left-radius:4px;color:#2d1b14}
            .jn-msg.user{align-self:flex-end;background:linear-gradient(135deg,#2d1b14,#4a2c2c);color:#fff;border-bottom-right-radius:4px}
            .jn-msg.bot a{color:#c0392b;font-weight:600;text-decoration:none}
            .jn-msg.bot a:hover{text-decoration:underline}
            .jn-msg.bot strong{color:#2d1b14}
            .jn-msg.bot em{color:#6b4040;font-size:12px}
            .jn-msg .jn-brand{font-size:10px;color:#d4b0b0;margin-top:8px;text-align:left;opacity:.8}
            @keyframes jnFadeIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
            #jn-chat-input-area{display:flex;gap:8px;padding:10px 12px;border-top:1px solid #e8d5d0;background:#fff;flex-shrink:0}
            #jn-chat-input{flex:1;border:1px solid #e8d5d0;border-radius:20px;padding:8px 14px;font-size:13px;outline:none;font-family:inherit}
            #jn-chat-input:focus{border-color:#d4a0a0}
            #jn-chat-send{background:#2d1b14;border:none;color:#fff;border-radius:50%;width:36px;height:36px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:all .2s}
            #jn-chat-send:hover{background:#4a2c2c}
            #jn-chat-send svg{width:16px;height:16px;fill:#fff}
            .jn-quick-reply{display:flex;flex-wrap:wrap;gap:6px;padding:4px 0}
            .jn-quick-reply button{background:rgba(45,27,20,.08);border:1px solid #e8d5d0;border-radius:100px;padding:5px 12px;font-size:12px;color:#2d1b14;cursor:pointer;transition:all .15s;font-family:inherit}
            .jn-quick-reply button:hover{background:#2d1b14;color:#fff;border-color:#2d1b14}
            .jn-typing{padding:10px 14px;background:#fff;border:1px solid #e8d5d0;border-radius:14px;border-bottom-left-radius:4px;align-self:flex-start;display:flex;gap:4px;align-items:center}
            .jn-typing span{width:6px;height:6px;border-radius:50%;background:#d4a0a0;animation:jnTyping 1.4s infinite both}
            .jn-typing span:nth-child(2){animation-delay:.2s}
            .jn-typing span:nth-child(3){animation-delay:.4s}
            @keyframes jnTyping{0%,80%,100%{opacity:.3;transform:scale(.8)}40%{opacity:1;transform:scale(1)}}
            @media(max-width:500px){
                #jn-chat-panel{right:12px;bottom:84px;width:calc(100vw - 24px);height:calc(100vh - 100px);max-height:none;border-radius:12px}
                #jn-chat-btn{right:16px;bottom:16px;width:52px;height:52px}
            }
        `;
        document.head.appendChild(css);

        // Chat button
        const btn = document.createElement('div');
        btn.id = 'jn-chat-btn';
        btn.innerHTML = `<svg viewBox="0 0 24 24"><path d="M12 2C6.477 2 2 6.477 2 12c0 1.89.525 3.67 1.438 5.2L2 22l4.8-1.438A9.956 9.956 0 0012 22c5.523 0 10-4.477 10-10S17.523 2 12 2z"/></svg>`;
        document.body.appendChild(btn);

        // Chat panel
        const panel = document.createElement('div');
        panel.id = 'jn-chat-panel';
        let state = { messageCount: 0, hasGreeted: false };

        panel.innerHTML = `
            <div id="jn-chat-header">
                <div id="jn-chat-header-avatar">💅</div>
                <div id="jn-chat-header-info">
                    <div id="jn-chat-header-name">Jeannie Nails Bot</div>
                    <div id="jn-chat-header-status">● Online — Ask me anything!</div>
                </div>
                <button id="jn-chat-close">✕</button>
            </div>
            <div id="jn-chat-messages">
                <div class="jn-msg bot">
                    <strong>✨ ${CONFIG.siteName}</strong><br><br>
                    Hi! I'm the Jeannie Nails bot. I can help you:<br>
                    🦶 Book appointments & check availability<br>
                    💅 Learn about our services & pricing<br>
                    🕐 Check hours & location<br><br>
                    <em>What can I help you with?</em>
                    <div class="jn-brand">${CONFIG.branding}</div>
                </div>
                <div class="jn-quick-reply">
                    <button onclick="window.__jnChat('Book Appointment 📅')">📅 Book Now</button>
                    <button onclick="window.__jnChat('Services & Pricing 💅')">💅 Services</button>
                    <button onclick="window.__jnChat('Hours 🕐')">🕐 Hours</button>
                    <button onclick="window.__jnChat('Ingrown Toenail 🦶')">🦶 Ingrown</button>
                </div>
            </div>
            <div id="jn-chat-input-area">
                <input id="jn-chat-input" type="text" placeholder="Type your message..." autocomplete="off">
                <button id="jn-chat-send">
                    <svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
                </button>
            </div>
        `;
        document.body.appendChild(panel);

        // ─── Controls ───
        const messagesEl = document.getElementById('jn-chat-messages');
        const inputEl = document.getElementById('jn-chat-input');
        const sendEl = document.getElementById('jn-chat-send');
        const closeEl = document.getElementById('jn-chat-close');

        window.__jnChat = function(text) {
            addMessage(text, 'user');
            setTimeout(() => respond(text), 400 + Math.random() * 400);
        };

        function addMessage(text, sender, options = {}) {
            const div = document.createElement('div');
            div.className = `jn-msg ${sender}`;
            div.innerHTML = text;
            if (options.branding) {
                const brand = document.createElement('div');
                brand.className = 'jn-brand';
                brand.textContent = CONFIG.branding;
                div.appendChild(brand);
            }
            messagesEl.appendChild(div);
            messagesEl.scrollTop = messagesEl.scrollHeight;
        }

        function showTyping() {
            const div = document.createElement('div');
            div.className = 'jn-typing';
            div.id = 'jn-typing-indicator';
            div.innerHTML = '<span></span><span></span><span></span>';
            messagesEl.appendChild(div);
            messagesEl.scrollTop = messagesEl.scrollHeight;
        }

        function hideTyping() {
            const el = document.getElementById('jn-typing-indicator');
            if (el) el.remove();
        }

        function showQuickReplies(replies) {
            const div = document.createElement('div');
            div.className = 'jn-quick-reply';
            replies.forEach(r => {
                const btn = document.createElement('button');
                btn.textContent = r;
                btn.onclick = () => window.__jnChat(r);
                div.appendChild(btn);
            });
            messagesEl.appendChild(div);
            messagesEl.scrollTop = messagesEl.scrollHeight;
        }

        function respond(msg) {
            showTyping();
            const intent = detectIntent(msg);
            
            setTimeout(() => {
                hideTyping();
                const resp = generateResponse(intent);
                addMessage(resp.text, 'bot', { branding: true });
                
                // Show quick replies
                const replies = getQuickReplies(intent);
                showQuickReplies(replies);
                
                state.messageCount++;
            }, 800 + Math.random() * 600);
        }

        // Event listeners
        function sendMessage() {
            const text = inputEl.value.trim();
            if (!text) return;
            inputEl.value = '';
            window.__jnChat(text);
        }

        sendEl.addEventListener('click', sendMessage);
        inputEl.addEventListener('keypress', e => { if (e.key === 'Enter') sendMessage(); });
        closeEl.addEventListener('click', () => { panel.style.display = 'none'; });
        btn.addEventListener('click', () => {
            panel.style.display = panel.style.display === 'flex' ? 'none' : 'flex';
        });
    }

    // Inject when DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', injectWidget);
    } else {
        injectWidget();
    }
})();
