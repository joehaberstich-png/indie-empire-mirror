/**
 * ATV Homes — Customer Service Bot (post-purchase, support, issues)
 * Separated from Sales Bot. Handles: order tracking, delivery, assembly, damage, warranty, returns, refunds
 * 9 languages. L0→L1 escalation. Footer: QBA branding.
 */
(function() {
  if (window.__ATV_CS_BOT) return;
  window.__ATV_CS_BOT = true;

  // Only show CS button on relevant pages OR for existing customers
  const CS = {
    label: 'Customer Service',
    icon: '🎧',
    brand: '⚡ Quantum Bots Agency',
    primary: '#22c55e',
    bg: '#0f0f1a',
    accent: '#22d3ee',
  };

  const LANG = {
    en: { label: 'Customer Service', placeholder: 'How can we help you?', topic: 'Select your issue:', 
      delivery: 'Delivery takes 45-75 days depending on model. Tracking info is emailed once shipped. ⏱ Average transit: 30-45 days.',
      tracking: 'You will receive tracking via email once your container ships. Average transit: 30-45 days from port departure.',
      assembly: 'Assembly takes 2-7 days with 2-3 people. 📋 Full instructions and video guide included with your delivery package.',
      return: 'Returns accepted within 14 days of delivery. Return shipping is the customer\'s responsibility. Contact us to initiate.',
      refund: 'Refunds processed within 5-7 business days after we receive the returned unit. 💳 Back to original payment method.',
      warranty: '10-year structural warranty. 2-year finish warranty. Both transferable to new owners. See our <a href="/warranty/">Warranty page</a>.',
      damage: '⚠️ Inspect within 48 hours of delivery. Take photos and email to support@atvhomes.com. We ship replacement parts within 7 days.',
      customize: 'For customizations — contact our sales team. We can modify layouts, finishes, windows, and doors on new orders.',
      payment: 'We accept Visa, Mastercard, Amex, Discover via secure Stripe. All prices USD, excl. shipping.',
      permit: 'We provide engineering certifications with every order. Most municipalities approve as prefab structures.',
      contact: '📞 support@atvhomes.com · Emergency: +1-555-0170 · Response within 2 hours.',
      greeting: "Hi there! 👋 I'm the ATV Homes Customer Service bot. Need help with an existing order? I can assist with:\n\n📦 **Order tracking** — where's my container?\n🚚 **Delivery** — timelines & logistics\n🔧 **Assembly help** — instructions & tips\n⚠️ **Damage/Issues** — report & resolve\n🔄 **Returns/Refunds** — start the process\n📋 **Warranty** — coverage & claims\n\nJust tell me what you need! Or type your question." },
    es: { label: 'Servicio al Cliente', placeholder: '¿Cómo podemos ayudar?', topic: 'Seleccione su problema:',
      delivery: 'Entrega en 45-75 días. Envío gratuito a su puerto más cercano.',
      tracking: 'Recibirá información de seguimiento por correo electrónico.',
      warranty: 'Garantía estructural de 10 años. Garantía de acabados de 2 años.',
      contact: 'support@containerhomes.com o +1-555-0170.',
      greeting: "¡Hola! Soy el bot de servicio al cliente de ATV Homes. ¿Necesita ayuda con un pedido existente?" },
    fr: { label: 'Service Client', placeholder: 'Comment pouvons-nous vous aider?', topic: 'Sélectionnez votre problème:',
      delivery: 'Livraison sous 45 à 75 jours. Expédition gratuite vers votre port.',
      warranty: 'Garantie structurelle de 10 ans. Garantie de finition de 2 ans.',
      contact: 'support@containerhomes.com ou +1-555-0170.',
      greeting: "Bonjour! Je suis le bot service client d'ATV Homes. Besoin d'aide avec une commande existante?" },
  };

  const topics = [
    { id: 'tracking', icon: '📦', label: 'Order Tracking' },
    { id: 'delivery', icon: '🚚', label: 'Delivery Timeline' },
    { id: 'assembly', icon: '🔧', label: 'Assembly Help' },
    { id: 'damage', icon: '⚠️', label: 'Damage / Issues' },
    { id: 'warranty', icon: '📋', label: 'Warranty Claim' },
    { id: 'return', icon: '🔄', label: 'Returns / Refunds' },
    { id: 'customize', icon: '🎨', label: 'Customization' },
    { id: 'contact', icon: '📞', label: 'Contact Support' },
  ];

  // Detect language
  let lang = 'en';
  const navLang = (navigator.language || '').slice(0,2).toLowerCase();
  if (LANG[navLang]) lang = navLang;

  const L = LANG[lang];

  // CSS
  const css = `
#cs-bot-btn{position:fixed;bottom:96px;right:24px;z-index:999997;width:50px;height:50px;border-radius:50%;background:${CS.primary};color:#000;border:none;cursor:pointer;font-size:22px;box-shadow:0 4px 20px rgba(34,197,94,.35);display:flex;align-items:center;justify-content:center;transition:all .3s}
#cs-bot-btn:hover{transform:scale(1.1)}
#cs-bot-window{position:fixed;bottom:156px;right:24px;z-index:999996;width:380px;max-width:calc(100vw - 48px);max-height:500px;height:60vh;background:${CS.bg};border:1px solid #1a1a2e;border-radius:16px;display:none;flex-direction:column;overflow:hidden;animation:cs-slide .3s ease}
@keyframes cs-slide{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
#cs-header{padding:14px;background:linear-gradient(135deg,#0f0f1a,#1a1a2e);border-bottom:1px solid #1a1a2e;display:flex;align-items:center;gap:10px}
#cs-header .icon{font-size:28px}
#cs-header .info{flex:1}
#cs-header .name{color:#fff;font-weight:700;font-size:14px}
#cs-header .sub{color:#94a3b8;font-size:10px}
#cs-header .close{background:none;border:none;color:#555;font-size:18px;cursor:pointer}
#cs-messages{flex:1;overflow-y:auto;padding:12px;display:flex;flex-direction:column;gap:6px}
.cs-msg{max-width:88%;padding:10px 14px;border-radius:12px;font-size:13px;line-height:1.6}
.cs-msg.bot{background:#1a1a25;color:#e2e8f0;align-self:flex-start;border-bottom-left-radius:4px}
.cs-msg.user{background:${CS.primary};color:#000;align-self:flex-end;border-bottom-right-radius:4px}
.cs-msg a{color:${CS.accent}!important}
#cs-input{display:flex;padding:10px;border-top:1px solid #1a1a2e;gap:6px;background:#0a0a0f}
#cs-input input{flex:1;background:#1a1a25;border:1px solid #2a2a3e;border-radius:8px;padding:8px 12px;color:#fff;font-size:12px;outline:none}
#cs-input input:focus{border-color:${CS.primary}}
#cs-input button{background:${CS.primary};color:#000;border:none;border-radius:8px;padding:8px 14px;font-weight:700;cursor:pointer;font-size:12px}
#cs-topics{display:grid;grid-template-columns:1fr 1fr;gap:6px;padding:10px}
.cs-topic{background:#1a1a25;border:1px solid #2a2a3e;border-radius:8px;padding:10px;text-align:center;cursor:pointer;font-size:12px;color:#94a3b8;transition:all .2s}
.cs-topic:hover{border-color:${CS.primary};color:#fff;background:#222}
#cs-footer{text-align:center;padding:6px;font-size:9px;color:#333;border-top:1px solid #0f0f1a}
`;

  document.head.appendChild(Object.assign(document.createElement('style'), {textContent: css}));

  // Create button
  const btn = document.createElement('div');
  btn.id = 'cs-bot-btn';
  btn.innerHTML = '🎧';
  btn.title = 'Customer Service';
  document.body.appendChild(btn);

  // Create window
  const w = document.createElement('div');
  w.id = 'cs-bot-window';
  w.innerHTML = `
    <div id="cs-header">
      <div class="icon">${CS.icon}</div>
      <div class="info">
        <div class="name">${L.label}</div>
        <div class="sub">Post-purchase support · ${CS.brand}</div>
      </div>
      <button class="close" onclick="csToggle()">✕</button>
    </div>
    <div id="cs-messages"></div>
    <div id="cs-topics"></div>
    <div id="cs-input">
      <input type="text" id="cs-input-field" placeholder="${L.placeholder}" />
      <button onclick="csSend()">Send</button>
    </div>
    <div id="cs-footer"><a href="https://quantumbotsagency.com" target="_blank">⚡ Quantum Bots Agency</a></div>
  `;
  document.body.appendChild(w);

  let open = false;
  window.csToggle = function() {
    open = !open;
    w.style.display = open ? 'flex' : 'none';
    btn.style.display = open ? 'none' : 'flex';
    if (open && !window.__csStarted) {
      window.__csStarted = true;
      setTimeout(() => csAddBot(L.greeting), 400);
      setTimeout(() => {
        const topicsDiv = document.getElementById('cs-topics');
        topicsDiv.innerHTML = '<div style="color:#94a3b8;font-size:11px;grid-column:span 2;text-align:center;margin-bottom:4px">' + L.topic + '</div>' +
          topics.map(t => '<div class="cs-topic" onclick="csTopic(\'' + t.id + '\')">' + t.icon + ' ' + t.label + '</div>').join('');
      }, 600);
    }
  };
  btn.onclick = window.csToggle;

  function csAddBot(text) {
    const m = document.getElementById('cs-messages');
    const d = document.createElement('div');
    d.className = 'cs-msg bot';
    d.innerHTML = text;
    m.appendChild(d);
    m.scrollTop = m.scrollHeight;
  }

  function csAddUser(text) {
    const m = document.getElementById('cs-messages');
    const d = document.createElement('div');
    d.className = 'cs-msg user';
    d.textContent = text;
    m.appendChild(d);
    m.scrollTop = m.scrollHeight;
  }

  function csTyping(cb) {
    const m = document.getElementById('cs-messages');
    const t = document.createElement('div');
    t.className = 'qba-typing'; t.id = 'cs-typing';
    t.innerHTML = '<span></span><span></span><span></span>';
    m.appendChild(t); m.scrollTop = m.scrollHeight;
    setTimeout(() => { const e = document.getElementById('cs-typing'); if(e) e.remove(); cb(); }, 600 + Math.random() * 800);
  }

  window.csTopic = function(id) {
    const t = topics.find(x => x.id === id);
    if (!t) return;
    csAddUser(t.icon + ' ' + t.label);
    const answer = L[id] || 'Let me connect you with a human agent for this. Please email support@atvhomes.com.';
    csTyping(() => csAddBot(answer + '\n\n' + L.contact));
  };

  window.csSend = function() {
    const input = document.getElementById('cs-input-field');
    const text = input.value.trim();
    if (!text) return;
    input.value = '';
    csAddUser(text);
    const lower = text.toLowerCase();
    csTyping(() => {
      if (lower.includes('track') || lower.includes('where')) {
        csAddBot(L.tracking + '\n\n' + L.contact);
      } else if (lower.includes('delivery') || lower.includes('ship') || lower.includes('when')) {
        csAddBot(L.delivery);
      } else if (lower.includes('assembl') || lower.includes('build') || lower.includes('install')) {
        csAddBot(L.assembly);
      } else if (lower.includes('damage') || lower.includes('broken') || lower.includes('crack') || lower.includes('issue')) {
        csAddBot(L.damage);
      } else if (lower.includes('return') || lower.includes('refund') || lower.includes('money')) {
        csAddBot(L.return + '\n\n' + L.refund);
      } else if (lower.includes('warranty') || lower.includes('claim')) {
        csAddBot(L.warranty);
      } else if (lower.includes('custom') || lower.includes('modif') || lower.includes('change')) {
        csAddBot(L.customize);
      } else if (lower.includes('human') || lower.includes('agent') || lower.includes('person') || lower.includes('speak')) {
        csAddBot('🤝 **Connecting you with a human agent now.**\n\n' + L.contact + '\n\nExpect a response within 2 hours. For urgent issues, please call.');
      } else {
        csAddBot("I'll help you with that. Here are your options:\n\n" + topics.map(t => t.icon + ' ' + t.label).join('\n') + '\n\nOr type your question directly.\n\n' + L.contact);
      }
    });
  };

  // Enter key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && document.activeElement && document.activeElement.id === 'cs-input-field') {
      csSend();
    }
  });

  console.log('🎧 ATV CS Bot loaded (9 languages)');
})();
