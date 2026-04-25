/* Quantum Live Chat — 24/7 Quantum Bot */
(function() {
  const CHAT_WELCOME_MSGS = [
    "👋 Welcome to Quantum Bots! I'm your 24/7 AI assistant. How can I help?",
    "⚛ Quantum Bots live. Ask me about our 100 products, hosting, or white label.",
    "🔐 Secure connection active. I'm here 24/7. What are you looking for?",
  ];

  const QUANTUM_RESPONSES = {
    'default': [
      "Great question! Our Full Quantum Bot features a true quantum decision engine with entanglement-based optimization. Would you like to see a demo?",
      "I can help with that. Our products range from $47/mo (Affiliate Bot) to $2,497/mo (Full Quantum). What's your budget?",
      "All our hosting plans include post-quantum cryptography (PQC) and a free domain. Which tier interests you?",
      "Our white label service lets you launch your own AI agency with 70-85% margins. Want to learn more?",
      "We have 100+ products and 500 SEO blog posts generated daily. Let me know what you need.",
    ],
    'pricing': "Our pricing is transparent: Standard Bot $97/mo, Advanced $197, Intelligent $497, Quantum-Light $997, Full Quantum $2,497. Multi-unit discounts up to 40% off. Hosting starts at $9/mo with a free domain.",
    'hosting': "9 quantum-grade hosting tiers from $9-$4,999/mo. All include PQC TLS 1.3, DDoS protection, and a free domain. Enterprise plans get SIEM monitoring, and Military tier includes permanent free domains + HSM key management.",
    'demo': "I can arrange a live demo of any product. Which one interests you? Our Full Quantum Bot demo showcases the entanglement-based decision engine in real-time.",
    'contact': "You can reach our quantum sales team 24/7 right here in chat, or book a call for high-ticket plans ($999+/mo).",
  };

  function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }

  const btn = document.getElementById('quantum-chat-button');
  const win = document.getElementById('quantum-chat-window');
  const msgs = document.getElementById('chat-messages');
  const input = document.getElementById('chat-input');
  const sendBtn = document.getElementById('chat-send-btn');
  let isOpen = false;

  function toggleChat() {
    isOpen = !isOpen;
    win.classList.toggle('open', isOpen);
    if (isOpen && msgs.children.length === 0) {
      setTimeout(() => addBotMsg(pick(CHAT_WELCOME_MSGS)), 500);
    }
  }

  function addBotMsg(text) {
    const div = document.createElement('div');
    div.className = 'chat-msg bot';
    div.innerHTML = text + '<span class="msg-time">' + new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) + '</span>';
    msgs.appendChild(div);
    msgs.scrollTop = msgs.scrollHeight;
  }

  function addUserMsg(text) {
    const div = document.createElement('div');
    div.className = 'chat-msg user';
    div.innerHTML = text + '<span class="msg-time">' + new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) + '</span>';
    msgs.appendChild(div);
    msgs.scrollTop = msgs.scrollHeight;
  }

  function showTyping() {
    const typing = document.createElement('div');
    typing.className = 'chat-typing';
    typing.id = 'chat-typing';
    typing.innerHTML = '<span></span><span></span><span></span>';
    msgs.appendChild(typing);
    msgs.scrollTop = msgs.scrollHeight;
  }

  function hideTyping() {
    const el = document.getElementById('chat-typing');
    if (el) el.remove();
  }

  function getResponse(userMsg) {
    const lower = userMsg.toLowerCase();
    if (lower.includes('pric') || lower.includes('cost') || lower.includes('how much') || lower.includes('dollar') || lower.includes('$')) {
      return QUANTUM_RESPONSES.pricing;
    }
    if (lower.includes('host') || lower.includes('server') || lower.includes('domain') || lower.includes('free domain')) {
      return QUANTUM_RESPONSES.hosting;
    }
    if (lower.includes('demo') || lower.includes('see') || lower.includes('show')) {
      return QUANTUM_RESPONSES.demo;
    }
    if (lower.includes('contact') || lower.includes('call') || lower.includes('talk') || lower.includes('speak') || lower.includes('human')) {
      return QUANTUM_RESPONSES.contact;
    }
    if (lower.includes('quantum bot') || lower.includes('full quantum') || lower.includes('featured') || lower.includes('best')) {
      return "The Full Quantum Bot is our flagship product ($2,497/mo). It features a true quantum decision engine with CRYSTALS-Kyber PQC security, unlimited API integrations, autonomous strategy deployment, and includes a FREE enterprise license for all 100 products. Would you like to see a demo?";
    }
    return pick(QUANTUM_RESPONSES.default);
  }

  function sendMessage() {
    const text = input.value.trim();
    if (!text) return;
    addUserMsg(text);
    input.value = '';
    input.focus();
    showTyping();
    const delay = Math.random() * 800 + 400; // 400-1200ms
    setTimeout(() => {
      hideTyping();
      addBotMsg(getResponse(text));
    }, delay);
  }

  btn.addEventListener('click', toggleChat);
  document.querySelector('.chat-close').addEventListener('click', toggleChat);
  sendBtn.addEventListener('click', sendMessage);
  input.addEventListener('keydown', e => { if (e.key === 'Enter') sendMessage(); });
})();
