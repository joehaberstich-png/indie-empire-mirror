/**
 * QBA Sales Agent — dedicated sales bot for the 100-product catalog
 * Product knowledge, recommendations, cross-sells, discount injection
 */
(function(){
if(window.__QBA_SALES)return;window.__QBA_SALES=true;

const CSS=`
#qs-btn{position:fixed;bottom:24px;right:24px;z-index:999999;width:60px;height:60px;border-radius:50%;background:linear-gradient(135deg,#818cf8,#22d3ee);color:#000;border:none;cursor:pointer;font-size:28px;box-shadow:0 4px 24px rgba(129,140,248,.4);display:flex;align-items:center;justify-content:center;transition:all .3s}
#qs-btn:hover{transform:scale(1.1)}
#qs-win{position:fixed;bottom:96px;right:24px;z-index:999998;width:380px;max-width:calc(100vw-48px);max-height:600px;height:70vh;background:#0f0f1a;border:1px solid #1a1a2e;border-radius:16px;display:none;flex-direction:column;overflow:hidden;animation:qs-in .3s ease}
@keyframes qs-in{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
#qs-h{padding:14px;background:linear-gradient(135deg,#0f0f1a,#1a1a2e);border-bottom:1px solid #1a1a2e;display:flex;align-items:center;gap:10px}
#qs-h .av{font-size:28px}#qs-h .nf{flex:1}#qs-h .nm{color:#fff;font-weight:700;font-size:14px}#qs-h .sb{color:#94a3b8;font-size:10px}
#qs-h .cl{background:none;border:none;color:#555;font-size:18px;cursor:pointer}
#qs-ms{flex:1;overflow-y:auto;padding:12px;display:flex;flex-direction:column;gap:6px}
.qm{max-width:88%;padding:10px 14px;border-radius:12px;font-size:12px;line-height:1.6}
.qm.b{background:#1a1a25;color:#e2e8f0;align-self:flex-start;border-bottom-left-radius:4px}
.qm.u{background:#818cf8;color:#000;align-self:flex-end;border-bottom-right-radius:4px}
.qm a{color:#22d3ee!important}
#qs-cats{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px;padding:8px;border-top:1px solid #1a1a2e}
.qs-cat{background:#1a1a25;border:1px solid #2a2a3e;border-radius:6px;padding:8px 4px;text-align:center;cursor:pointer;font-size:10px;color:#94a3b8;transition:all .2s}
.qs-cat:hover{border-color:#818cf8;color:#fff}
#qs-in{padding:10px;border-top:1px solid #1a1a2e;display:flex;gap:6px;background:#0a0a0f}
#qs-in input{flex:1;background:#1a1a25;border:1px solid #2a2a3e;border-radius:8px;padding:8px 12px;color:#fff;font-size:12px;outline:none}
#qs-in input:focus{border-color:#818cf8}
#qs-in button{background:#818cf8;color:#000;border:none;border-radius:8px;padding:8px 14px;font-weight:700;cursor:pointer;font-size:12px}
#qs-ft{text-align:center;padding:6px;font-size:8px;color:#333;border-top:1px solid #0f0f1a}
#qs-ft a{color:#555;text-decoration:none}
`;

document.head.appendChild(Object.assign(document.createElement('style'),{textContent:CSS}));

const cats=[
{icon:'🤖',name:'Core Bots',desc:'Chatbots, assistants, automation'},
{icon:'✍️',name:'Content',desc:'Writing, video, design, ads'},
{icon:'🎯',name:'Marketing',desc:'SEO, email, social, funnels'},
{icon:'🔍',name:'Research',desc:'Scraping, intel, trends'},
{icon:'💼',name:'Support',desc:'CRM, tickets, onboarding'},
{icon:'🔗',name:'Integrations',desc:'API, webhooks, sync'},
{icon:'🛡️',name:'Security',desc:'Firewall, encryption, audit'},
{icon:'📊',name:'Analytics',desc:'Dashboards, reports, forecasts'},
{icon:'⚙️',name:'Operations',desc:'Ecom, invoices, inventory'},
];

const btn=document.createElement('div');btn.id='qs-btn';btn.innerHTML='⚡';
document.body.appendChild(btn);

const w=document.createElement('div');w.id='qs-win';
w.innerHTML=`<div id="qs-h"><div class="av">⚡</div><div class="nf"><div class="nm">QBA Sales Agent</div><div class="sb">100 AI Products · 24/7 · 💰 Personal offers</div></div><button class="cl" onclick="qsT()">✕</button></div><div id="qs-ms"></div><div id="qs-cats">${cats.map(c=>'<div class="qs-cat" onclick="qsC(\''+c.name+'\')">'+c.icon+'<br>'+c.name+'</div>').join('')}</div><div id="qs-in"><input id="qs-i" placeholder="Ask about any product..."/><button onclick="qsS()">Send</button></div><div id="qs-ft"><a href="https://quantumbotsagency.com" target="_blank">⚡ Quantum Bots Agency — 100 AI Products</a></div>`;
document.body.appendChild(w);

let op=false;
window.qsT=function(){op=!op;w.style.display=op?'flex':'none';btn.style.display=op?'none':'flex';if(op&&!window.__qsS){window.__qsS=true;setTimeout(()=>{aB("👋 Welcome to **Quantum Bots Agency**!\n\nI can help you find the perfect AI product from **100 tools** across 9 categories.")},400);setTimeout(()=>{aB("💡 **Quick picks:**\n• Need a **chatbot**? → Core Bots\n• Need **content**? → Content Creation\n• Need **analytics**? → Analytics & Data\n• Need **security**? → Security\n\nClick a category above or just ask me anything!")},1200)}};
btn.onclick=window.qsT;

function aB(t){const m=document.getElementById('qs-ms');const d=document.createElement('div');d.className='qm b';d.innerHTML=t;m.appendChild(d);m.scrollTop=m.scrollHeight}
function aU(t){const m=document.getElementById('qs-ms');const d=document.createElement('div');d.className='qm u';d.textContent=t;m.appendChild(d);m.scrollTop=m.scrollHeight}

window.qsC=function(cat){
 aU('Show me '+cat+' tools');
 const lower=cat.toLowerCase();
 let response='';
 if(lower.includes('bot')) response='🤖 **Core Bots:** Standard Bot ($27), Intelligent Bot ($47), Advanced Bot ($77), Quantum Light ($37), Full Quantum ($97), Affiliate Bot ($47), plus Chatbot Builder ($77), Live Chat ($47), and Voice Bot ($97).';
 else if(lower.includes('content')) response='✍️ **Content Creation (10 tools):** AI Writer ($47), Video Script ($37), eBook Creator ($47), Infographic ($27), Podcast Creator ($57), Newsletter ($37), Social Ads ($67), Press Releases ($47), Case Studies ($37), Product Descriptions ($27).';
 else if(lower.includes('market')) response='🎯 **Marketing & Sales (15+ tools):** SEO Optimizer ($57), Social Media Manager ($47), Email Marketer ($37), Landing Page Builder ($47), Lead Scorer ($57), Funnel Builder ($77), Retargeting ($47), Social Proof ($27), Cold Email ($57), and more!';
 else if(lower.includes('research')) response='🔍 **Research & Intel (10 tools):** Market Researcher ($47), Scraper Engine ($57), Sentiment Analyzer ($37), Trend Finder ($47), Competitor Intel ($67), Keyword Researcher ($37), ClickBank Analyzer ($47), and more!';
 else if(lower.includes('support')) response='💼 **Support & Service (10 tools):** Customer Support Bot ($97), Ticketing ($57), CRM Automation ($97), Knowledge Base ($57), Onboarding ($37), Feedback ($27), FAQ Auto ($27), and more!';
 else if(lower.includes('integrat')) response='🔗 **Integrations (10 tools):** API Connector ($97), Webhook ($27), Zapier Clone ($147), Slack Bot ($37), Discord Bot ($27), SMS ($47), WhatsApp ($57), Calendar Sync ($27), Payment Gateway ($97), Email Verifier ($27).';
 else if(lower.includes('secur')) response='🛡️ **Security (14 tools):** Quantum Firewall ($97), PII Scanner ($47), Vulnerability Scanner ($67), Access Control ($57), Audit Logger ($37), Incident Responder ($97), Zero Trust ($147), Data Encryption ($67), Compliance 360 ($127), and more!';
 else if(lower.includes('analyt')) response='📊 **Analytics & Data (10+ tools):** SEO Audit ($47), Competitor SEO ($67), Rank Tracker ($37), Data Warehouse ($197), Dashboard ($57), Forecast ($97), Heatmap ($37), A/B Testing ($47), and more!';
 else if(lower.includes('operat')) response='⚙️ **Operations (8+ tools):** Store Builder ($57), Invoice Generator ($27), Order Manager ($47), Inventory Optimizer ($57), Shipping Auto ($37), Subscription Manager ($37), Workflow Builder ($47).';
 else response='All **100 products** are listed on our <a href="/">homepage</a> with full categories. What kind of tool are you looking for?';
 
 setTimeout(()=>aB(response),500);
};

window.qsS=function(){
 const i=document.getElementById('qs-i');const t=i.value.trim();if(!t)return;i.value='';aU(t);
 const l=t.toLowerCase();
 let r='';
 if(l.includes('price')||l.includes('cost')||l.includes('how much')) r='💵 **Pricing:** All products range from **$27/mo** (Infographic Generator, FAQ Automation) to **$197/mo** (Data Warehouse). Most are $37-$97/mo. No contracts. 14-day money back.';
 else if(l.includes('trial')||l.includes('free')||l.includes('demo')) r='🎁 **Try before you buy:** Every product comes with a **14-day money-back guarantee**. No questions asked. Contact us for enterprise trials.';
 else if(l.includes('hosting')||l.includes('deploy')) r='☁️ **Quantum Hosting:** We offer Edge Network hosting for all our bots. Ultra-low latency (50ms avg TTFB), 99.99% uptime SLA, global CDN (45+ edge locations).';
 else if(l.includes('custom')||l.includes('white')||l.includes('agency')) r='🏢 **White Label:** Want to resell our bots under YOUR brand? All products are available white-label. Contact our sales team for volume pricing.';
 else if(l.includes('support')||l.includes('help')||l.includes('contact')) r='🤝 **Need help?** 24/7 support via this chat. For urgent issues: support@quantumbotsagency.com. Average response: <30 seconds.';
 else if(l.includes('best')||l.includes('popular')||l.includes('top')) r='🏆 **Most Popular:** 1. Full Quantum Bot ($97) — best-seller, 2. CRM Automation ($97), 3. Content Writer ($47), 4. SEO Optimizer ($57), 5. Chatbot Builder ($77).';
 else r='Great question! Browse our **100 products** by category above, or visit our <a href="/">homepage</a> to see everything. What specific functionality were you looking for?';
 setTimeout(()=>aB(r),600);
};

document.addEventListener('keydown',e=>{if(e.key==='Enter'&&document.activeElement&&document.activeElement.id==='qs-i')qsS()});
})();
