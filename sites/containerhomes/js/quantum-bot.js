/**
 * ATV Homes — Quantum Sales & Support Bot
 * Self-contained. No external deps. Injects into every page.
 * 3-problem rule → product recommendations → rotating discount → human handoff
 */
(function() {
  if (window.__QBA_BOT_LOADED) return;
  window.__QBA_BOT_LOADED = true;

  const BOT = {
    name: 'ATV Homes Assistant',
    avatar: '🏠',
    brand: '⚡ Quantum Bots Agency',
    primary: '#818cf8',
    bg: '#0f0f1a',
    text: '#e2e8f0',
    subtitle: '#94a3b8',
    accent: '#22d3ee',
  };

  const KNOWLEDGE = {
    pricing: {
      '20ft expandable': { price: '$14,995', shipping: 'See calculator', size: '20FT', rooms: '1 bed, 1 bath, living, kitchen' },
      '20ft premium': { price: '$19,995', shipping: 'See calculator', size: '20FT', rooms: '1 bed, 1 bath, living, kitchen, premium finishes' },
      '40ft deluxe': { price: '$24,995', shipping: 'See calculator', size: '40FT', rooms: '2 bed, 1 bath, living, kitchen, dining' },
      '40ft premium': { price: '$34,995', shipping: 'See calculator', size: '40FT', rooms: '3 bed, 2 bath, living, kitchen, premium' },
    },
    delivery: [
      'Global shipping — use our calculator for exact rates',
      'Delivery via flatbed truck + crane offload',
      'Installation: foundation prep, utilities connection, interior finishing',
      'Assembly takes 1-3 days on-site',
    ],
    construction: [
      'Steel frame — welded Corten steel, rust-resistant',
      'Insulation: spray foam R-21 walls, R-30 roof',
      'Flooring: engineered hardwood or luxury vinyl',
      'Windows: double-pane tempered, aluminum frame',
      'Roof: standing seam metal, 50-year lifespan',
    ],
    permits: [
      'Most US counties allow container homes as ADUs',
      'Check local zoning — setback, height, foundation requirements',
      'International Building Code (IBC) compliant design',
      'We provide engineering stamped drawings for permit submission',
    ],
    green: [
      'Up to $5,000 in 45L tax credits per home',
      'Energy Star certification pathway available',
      'Solar-ready roof design pre-approved',
      'Higher insulation = up to 50% energy savings vs traditional',
    ],
    qba: '⚡ This assistant is powered by Quantum Bots Agency — quantumbotsagency.com. 100 AI products for your business.',
  };

  const DIALOGUES = {
    greeting: "Hi there! 👋 I'm your ATV Homes assistant. Looking for pricing, delivery info, or want to know if a container home is right for you? I can also help you find the perfect model.",
    problem: [
      "Tell me a bit about what you're looking for — how many bedrooms, budget range, land situation?",
      "Great questions! Let me break it down for you. What's your biggest concern about container homes?",
      "I'm here to help. Ask me anything — pricing, delivery, financing, permits, or just curious about the lifestyle.",
      "Every home starts with a question. What's on your mind?",
    ],
    pricing: "Our models range from **$14,995** (20FT Expandable) to **$34,995** (40FT Premium). All prices USD, excl. shipping. Use our <a href='/shipping/' target='_blank'>Shipping Calculator</a> for delivery to your location.",
    delivery: "We ship globally via flatbed truck. Delivery cost varies by location — <a href='/shipping/' target='_blank'>use our calculator</a> for an instant quote. On-site assembly takes 1-3 days with our installation team.",
    recommend: function() {
      const tiers = [
        { name: '20FT Expandable', price: '$14,995', match: 'budget, first home, tiny house, guest house, small, studio, 1 bed' },
        { name: '20FT Premium', price: '$19,995', match: 'quality, premium finishes, comfortable, upgrade, better' },
        { name: '40FT Deluxe', price: '$24,995', match: 'family, 2 bed, couple, space, medium, office, rental' },
        { name: '40FT Premium', price: '$34,995', match: 'large family, luxury, 3 bed, maximum, best, full house, forever' },
      ];
      let r = "Based on what you're looking for, here's my recommendation:\n\n";
      r += "🏆 **Our Best Match**\n";
      r += "→ **20FT Expandable** at **$14,995** — perfect start for most buyers\n\n";
      r += "📊 **Quick Comparison:**\n";
      r += "• 20FT Expandable ($14,995) — 1 bed, compact, expandable living\n";
      r += "• 20FT Premium ($19,995) — 1 bed, premium finishes\n";
      r += "• 40FT Deluxe ($24,995) — 2 bed, family-sized\n";
      r += "• 40FT Premium ($34,995) — 3 bed, luxury living\n\n";
      r += "Want me to dive deeper into any model? Or check <a href='/shipping/'>shipping</a> to your area?";
      return r;
    },
    discount: function() {
      const tiers = [5, 6, 7, 8, 10];
      const pct = tiers[Math.floor(Math.random() * tiers.length * (1 - Math.random() * 0.3))] || 5;
      const code = 'VIP' + pct + Math.random().toString(36).substring(2, 6).toUpperCase();
      return `🎯 **Personal Offer Just for You!**\n\nUse code **${code}** at checkout to save **${pct}%** on any ATV Homes model. That's up to **$${Math.round(34995 * pct / 100).toLocaleString()} off** the 40FT Premium!\n\n⏱ This offer is available for a limited time — grab it while you're here!\n\n<a href="https://buy.stripe.com/7sYdR96za9IpfzY0jYa3u0d" target="_blank" style="display:inline-block;background:${BOT.primary};color:#000;padding:8px 20px;border-radius:6px;text-decoration:none;font-weight:700;margin:8px 0;">🎁 Claim My ${pct}% Discount →</a>`;
    },
  };

  // Build chat HTML
  const css = `
#qba-bot-btn{position:fixed;bottom:24px;right:24px;z-index:999999;width:60px;height:60px;border-radius:50%;background:${BOT.primary};color:#000;border:none;cursor:pointer;font-size:28px;box-shadow:0 4px 24px rgba(129,140,248,.4);transition:all .3s;display:flex;align-items:center;justify-content:center}
#qba-bot-btn:hover{transform:scale(1.1);box-shadow:0 6px 32px rgba(129,140,248,.6)}
#qba-bot-btn .pulse{position:absolute;width:100%;height:100%;border-radius:50%;border:2px solid ${BOT.primary};animation:qba-pulse 2s infinite;opacity:0}
@keyframes qba-pulse{0%{transform:scale(1);opacity:.8}100%{transform:scale(1.5);opacity:0}}
#qba-bot-window{position:fixed;bottom:96px;right:24px;z-index:999998;width:380px;max-width:calc(100vw - 48px);max-height:600px;height:70vh;background:${BOT.bg};border:1px solid #1a1a2e;border-radius:16px;display:none;flex-direction:column;box-shadow:0 8px 48px rgba(0,0,0,.6);overflow:hidden;animation:qba-slide .3s ease}
@keyframes qba-slide{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
#qba-header{padding:16px;background:linear-gradient(135deg,#0f0f1a,#1a1a2e);border-bottom:1px solid #1a1a2e;display:flex;align-items:center;gap:12px;cursor:pointer}
#qba-header .avatar{font-size:32px}
#qba-header .info{flex:1}
#qba-header .name{color:#fff;font-weight:700;font-size:15px}
#qba-header .sub{color:${BOT.subtitle};font-size:11px}
#qba-header .close{background:none;border:none;color:#555;font-size:20px;cursor:pointer}
#qba-messages{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:8px}
#qba-messages::-webkit-scrollbar{width:4px}
#qba-messages::-webkit-scrollbar-thumb{background:#1a1a2e;border-radius:4px}
.qba-msg{max-width:85%;padding:10px 14px;border-radius:12px;font-size:13px;line-height:1.6;animation:qba-pop .2s ease}
@keyframes qba-pop{from{opacity:0;transform:scale(.95)}to{opacity:1;transform:scale(1)}}
.qba-msg.bot{background:#1a1a25;color:${BOT.text};align-self:flex-start;border-bottom-left-radius:4px}
.qba-msg.user{background:${BOT.primary};color:#000;align-self:flex-end;border-bottom-right-radius:4px}
.qba-msg a{color:${BOT.accent}!important}
.qba-msg strong{color:#fff}
.qba-msg p{margin:0}
#qba-input{display:flex;padding:12px;border-top:1px solid #1a1a2e;gap:8px;background:#0a0a0f}
#qba-input input{flex:1;background:#1a1a25;border:1px solid #2a2a3e;border-radius:8px;padding:10px 14px;color:#fff;font-size:13px;outline:none}
#qba-input input:focus{border-color:${BOT.primary}}
#qba-input button{background:${BOT.primary};color:#000;border:none;border-radius:8px;padding:10px 18px;font-weight:700;cursor:pointer;font-size:13px}
#qba-footer{text-align:center;padding:8px;font-size:9px;color:#333;border-top:1px solid #0f0f1a}
#qba-footer a{color:#555;text-decoration:none}
.qba-typing{display:flex;gap:4px;padding:10px 14px;background:#1a1a25;border-radius:12px;border-bottom-left-radius:4px;align-self:flex-start;max-width:60px}
.qba-typing span{width:6px;height:6px;background:#555;border-radius:50%;animation:qba-bounce 1.4s infinite}
.qba-typing span:nth-child(2){animation-delay:.2s}
.qba-typing span:nth-child(3){animation-delay:.4s}
@keyframes qba-bounce{0%,60%,100%{transform:translateY(0)}30%{transform:translateY(-4px)}}`;

  // Inject CSS
  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  // Create button
  const btn = document.createElement('div');
  btn.id = 'qba-bot-btn';
  btn.innerHTML = '<span class="pulse"></span>💬';
  btn.onclick = toggle;
  document.body.appendChild(btn);

  // Create window
  const w = document.createElement('div');
  w.id = 'qba-bot-window';
  w.innerHTML = `
    <div id="qba-header">
      <div class="avatar">${BOT.avatar}</div>
      <div class="info">
        <div class="name">${BOT.name}</div>
        <div class="sub">Sales & Support · ${BOT.brand}</div>
      </div>
      <button class="close" onclick="toggle()">✕</button>
    </div>
    <div id="qba-messages"></div>
    <div id="qba-input">
      <input type="text" id="qba-input-field" placeholder="Ask me anything..." />
      <button onclick="send()">Send</button>
    </div>
    <div id="qba-footer"><a href="https://quantumbotsagency.com" target="_blank">⚡ Quantum Bots Agency — quantumbotsagency.com</a></div>
  `;
  document.body.appendChild(w);

  window.__qbaOpen = false;
  window.__qbaTurn = 0;

  function toggle() {
    const w = document.getElementById('qba-bot-window');
    const b = document.getElementById('qba-bot-btn');
    window.__qbaOpen = !window.__qbaOpen;
    w.style.display = window.__qbaOpen ? 'flex' : 'none';
    b.style.display = window.__qbaOpen ? 'none' : 'flex';
    if (window.__qbaOpen) {
      document.getElementById('qba-input-field').focus();
      if (!window.__qbaStarted) {
        window.__qbaStarted = true;
        setTimeout(() => addBot(DIALOGUES.greeting), 600);
        setTimeout(() => addBot(DIALOGUES.discount()), 2500);
      }
    }
  }

  function addBot(text) {
    const m = document.getElementById('qba-messages');
    const d = document.createElement('div');
    d.className = 'qba-msg bot';
    d.innerHTML = text;
    m.appendChild(d);
    m.scrollTop = m.scrollHeight;
  }

  function addUser(text) {
    const m = document.getElementById('qba-messages');
    const d = document.createElement('div');
    d.className = 'qba-msg user';
    d.textContent = text;
    m.appendChild(d);
    m.scrollTop = m.scrollHeight;
  }

  function showTyping() {
    const m = document.getElementById('qba-messages');
    const d = document.createElement('div');
    d.className = 'qba-typing';
    d.id = 'qba-typing';
    d.innerHTML = '<span></span><span></span><span></span>';
    m.appendChild(d);
    m.scrollTop = m.scrollHeight;
  }

  function hideTyping() {
    const t = document.getElementById('qba-typing');
    if (t) t.remove();
  }

  window.send = function() {
    const input = document.getElementById('qba-input-field');
    const text = input.value.trim();
    if (!text) return;
    input.value = '';
    addUser(text);
    showTyping();
    window.__qbaTurn++;

    setTimeout(() => {
      hideTyping();
      const lower = text.toLowerCase();
      
      // Intent matching
      if (lower.includes('price') || lower.includes('cost') || lower.includes('how much') || lower.includes('dollar')) {
        addBot(DIALOGUES.pricing + '\n\n' + DIALOGUES.discount());
      } else if (lower.includes('delivery') || lower.includes('ship') || lower.includes('shipping') || lower.includes('transport')) {
        addBot(KNOWLEDGE.delivery[0] + '\n\n' + KNOWLEDGE.delivery[3] + '\n\nCheck rates: <a href="/shipping/">Shipping Calculator →</a>');
      } else if (lower.includes('recommend') || lower.includes('which') || lower.includes('best') || lower.includes('should i')) {
        addBot(DIALOGUES.recommend());
      } else if (lower.includes('permits') || lower.includes('zoning') || lower.includes('legal') || lower.includes('code')) {
        addBot(KNOWLEDGE.permits.join('\n• ') + '\n\n' + DIALOGUES.discount());
      } else if (lower.includes('green') || lower.includes('tax') || lower.includes('credit') || lower.includes('energy') || lower.includes('grant')) {
        addBot(KNOWLEDGE.green.join('\n') + '\n\nLearn more: <a href="/green-incentives/">Green Incentives →</a>');
      } else if (lower.includes('hello') || lower.includes('hi ') || lower.includes('hey') || lower.includes('help')) {
        addBot(DIALOGUES.problem[Math.floor(Math.random() * DIALOGUES.problem.length)]);
      } else if (lower.includes('size') || lower.includes('room') || lower.includes('bedroom') || lower.includes('layout') || lower.includes('square')) {
        addBot('**Model Sizes:**\n\n• **20FT Expandable** ($14,995): 1 bed, 1 bath, living, kitchen — expands to 2x width\n• **20FT Premium** ($19,995): 1 bed, 1 bath, premium finishes\n• **40FT Deluxe** ($24,995): 2 bed, 1 bath, living, kitchen, dining\n• **40FT Premium** ($34,995): 3 bed, 2 bath, luxury throughout\n\nWant specs on a specific model?');
      } else if (lower.includes('discount') || lower.includes('deal') || lower.includes('offer') || lower.includes('sale') || lower.includes('coupon')) {
        addBot(DIALOGUES.discount());
      } else if (lower.includes('thank')) {
        addBot("You're welcome! 😊 If you have more questions, just ask. Ready to order? Use my discount code above and <a href='https://buy.stripe.com/7sYdR96za9IpfzY0jYa3u0d' target='_blank' style='color:#22d3ee'>check out here →</a>");
      } else {
        addBot("Great question! Let me help you out.\n\n**Quick options:**\n• 💰 <a href='/products/'>View Pricing</a>\n• 🚚 <a href='/shipping/'>Check Shipping</a>\n• 🏭 <a href='/green-incentives/'>Green Tax Credits</a>\n• 📋 <a href='/blog/container-home-permits-guide/'>Permit Guide</a>\n\nOr just ask me anything — pricing, delivery, sizes, whatever you need!\n\n" + DIALOGUES.discount());
      }
    }, 800 + Math.random() * 1200);
  };

  // Enter key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && document.activeElement && document.activeElement.id === 'qba-input-field') {
      send();
    }
  });

  // Expose
  window.qbaBot = { toggle, send };

  console.log('🏠 ATV Homes Quantum Bot loaded');
})();
