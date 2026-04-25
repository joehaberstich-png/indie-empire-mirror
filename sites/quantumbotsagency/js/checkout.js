// Auto-generated checkout from live Stripe products
// DO NOT EDIT — Regenerate with generate_checkout.py

const STRIPE_PK = "[REDACTED_STRIPE_PK]";

const PRODUCTS = {
  QBA_BOT_STANDARD_MONTHLY: { price_id: "price_1TPZelE0iuyRsYRxFZtyX0yp", name: "QBA Bot Standard Monthly", amount: 29.0, currency: "USD", interval: "month" },
  QBA_BOT_PRO_MONTHLY: { price_id: "price_1TPZelE0iuyRsYRxqUdbdYIf", name: "QBA Bot Pro Monthly", amount: 99.0, currency: "USD", interval: "month" },
  QBA_BOT_ELITE_MONTHLY: { price_id: "price_1TPZemE0iuyRsYRxLN0CQJXJ", name: "QBA Bot Elite Monthly", amount: 299.0, currency: "USD", interval: "month" },
  QBA_BOT_ENTERPRISE_MONTHLY: { price_id: "price_1TPZemE0iuyRsYRxiFIhGXry", name: "QBA Bot Enterprise Monthly", amount: 499.0, currency: "USD", interval: "month" },
  QBA_WHITE_LABEL_MONTHLY: { price_id: "price_1TPZenE0iuyRsYRx0u6s5PvP", name: "QBA White Label Monthly", amount: 999.0, currency: "USD", interval: "month" },
  QBA_BOT_STANDARD_YEARLY: { price_id: "price_1TPZenE0iuyRsYRxEt1xoIEc", name: "QBA Bot Standard Yearly", amount: 299.0, currency: "USD", interval: "year" },
  QBA_BOT_PRO_YEARLY: { price_id: "price_1TPZeoE0iuyRsYRxB3lf4IRV", name: "QBA Bot Pro Yearly", amount: 999.0, currency: "USD", interval: "year" },
  QBA_BOT_ELITE_YEARLY: { price_id: "price_1TPZeoE0iuyRsYRxJifMMKCN", name: "QBA Bot Elite Yearly", amount: 2990.0, currency: "USD", interval: "year" },
  QBA_BOT_ENTERPRISE_YEARLY: { price_id: "price_1TPZepE0iuyRsYRxRQUSDdHf", name: "QBA Bot Enterprise Yearly", amount: 4990.0, currency: "USD", interval: "year" },
  QBA_WHITE_LABEL_YEARLY: { price_id: "price_1TPZepE0iuyRsYRxRDKp70AG", name: "QBA White Label Yearly", amount: 9999.0, currency: "USD", interval: "year" },
  QUANTUM_HOSTING_BASIC: { price_id: "price_1TPZepE0iuyRsYRxiHi9UTO0", name: "Quantum Hosting Basic", amount: 19.99, currency: "USD", interval: "month" },
  QUANTUM_HOSTING_PRO: { price_id: "price_1TPZeqE0iuyRsYRxwCsYpyFA", name: "Quantum Hosting Pro", amount: 49.99, currency: "USD", interval: "month" },
  QUANTUM_HOSTING_ENTERPRISE: { price_id: "price_1TPZeqE0iuyRsYRxZtl8t7de", name: "Quantum Hosting Enterprise", amount: 149.99, currency: "USD", interval: "month" },
  QUANTUM_HOSTING_ULTIMATE: { price_id: "price_1TPZerE0iuyRsYRx1dJKGAV4", name: "Quantum Hosting Ultimate", amount: 499.99, currency: "USD", interval: "month" },
  FOTC_FREE_TRIAL: { price_id: "price_1TPZerE0iuyRsYRxqRvzbH0s", name: "FotC Free Trial", amount: 0.0, currency: "USD", interval: "month" },
  FOTC_MEMBERSHIP_BASIC: { price_id: "price_1TPZesE0iuyRsYRxjrNnkP37", name: "FotC Membership Basic", amount: 9.99, currency: "USD", interval: "month" },
  FOTC_MEMBERSHIP_PREMIUM: { price_id: "price_1TPZesE0iuyRsYRx1KmV8rXj", name: "FotC Membership Premium", amount: 49.99, currency: "USD", interval: "month" },
  FOTC_MEMBERSHIP_FOUNDERS: { price_id: "price_1TPZetE0iuyRsYRxm3zheTjZ", name: "FotC Membership Founders", amount: 99.99, currency: "USD", interval: "month" },
  FOTC_MEMBERSHIP_LIFETIME: { price_id: "price_1TPZetE0iuyRsYRxgo3tSFgc", name: "FotC Membership Lifetime", amount: 999.0, currency: "USD", interval: "year" },
  FOTC_TIER_1___STREET_INTEL_NFT: { price_id: "price_1TPZetE0iuyRsYRxdWF1Dcea", name: "FotC Tier 1 - Street Intel NFT", amount: 20.0, currency: "USD", interval: "one-time" },
  FOTC_TIER_2___DEEP_COVER_NFT: { price_id: "price_1TPZeuE0iuyRsYRxL7uR27B1", name: "FotC Tier 2 - Deep Cover NFT", amount: 50.0, currency: "USD", interval: "one-time" },
  FOTC_TIER_3___WIRETAP_ACCESS_NFT: { price_id: "price_1TPZeuE0iuyRsYRxXEWAbM5T", name: "FotC Tier 3 - Wiretap Access NFT", amount: 100.0, currency: "USD", interval: "one-time" },
  FOTC_TIER_4___IDENTITY_FORGE_NFT: { price_id: "price_1TPZevE0iuyRsYRxbS8ILZxV", name: "FotC Tier 4 - Identity Forge NFT", amount: 250.0, currency: "USD", interval: "one-time" },
  FOTC_TIER_5___CABAL_INFILTRATOR_NFT: { price_id: "price_1TPZevE0iuyRsYRxud5EkQsN", name: "FotC Tier 5 - Cabal Infiltrator NFT", amount: 500.0, currency: "USD", interval: "one-time" },
  FOTC_TIER_6___SHADOW_DIRECTOR_NFT: { price_id: "price_1TPZewE0iuyRsYRxJbwjA6sD", name: "FotC Tier 6 - Shadow Director NFT", amount: 1000.0, currency: "USD", interval: "one-time" },
  FOTC_TIER_7___THE_PUPPET_MASTER_NFT: { price_id: "price_1TPZewE0iuyRsYRx1cfOuT58", name: "FotC Tier 7 - The Puppet Master NFT", amount: 5000.0, currency: "USD", interval: "one-time" },
  FOTC_STARTER_PACK_TIER_1_3_BUNDLE: { price_id: "price_1TPZexE0iuyRsYRx0yP91rlu", name: "FotC Starter Pack (Tier 1-3 Bundle)", amount: 150.0, currency: "USD", interval: "one-time" },
  FOTC_ELITE_PACK_TIER_4_6_BUNDLE: { price_id: "price_1TPZexE0iuyRsYRxnN2jOIYI", name: "FotC Elite Pack (Tier 4-6 Bundle)", amount: 1500.0, currency: "USD", interval: "one-time" },
  FOTC_COMPLETE_COLLECTION_TIER_1_7: { price_id: "price_1TPZeyE0iuyRsYRx8MSWX63B", name: "FotC Complete Collection (Tier 1-7)", amount: 5000.0, currency: "USD", interval: "one-time" },
  FOTC_FOUNDERS_PLEDGE: { price_id: "price_1TPZeyE0iuyRsYRxJ40v91tf", name: "FotC Founder's Pledge", amount: 0.0, currency: "USD", interval: "one-time" },
  FOTC_HUNTED_FOUNDER_TOKEN: { price_id: "price_1TPZeyE0iuyRsYRxsj1L6Oz8", name: "FotC Hunted Founder Token", amount: 0.0, currency: "USD", interval: "one-time" },
  ₡CC_STARTER_BUNDLE_1000_CREDITS: { price_id: "price_1TPZezE0iuyRsYRxxVzQfenk", name: "₡CC Starter Bundle (1,000 credits)", amount: 9.99, currency: "USD", interval: "one-time" },
  ₡CC_STANDARD_BUNDLE_5500_CREDITS: { price_id: "price_1TPZf0E0iuyRsYRx0OuS9Hda", name: "₡CC Standard Bundle (5,500 credits)", amount: 49.99, currency: "USD", interval: "one-time" },
  ₡CC_PREMIUM_BUNDLE_12000_CREDITS: { price_id: "price_1TPZf0E0iuyRsYRxMDcqqLy4", name: "₡CC Premium Bundle (12,000 credits)", amount: 99.99, currency: "USD", interval: "one-time" },
  ₡CC_ELITE_BUNDLE_65000_CREDITS: { price_id: "price_1TPZf0E0iuyRsYRxuPGCVoz9", name: "₡CC Elite Bundle (65,000 credits)", amount: 499.99, currency: "USD", interval: "one-time" },
  ₡CC_LEGENDARY_BUNDLE_140000_CREDITS: { price_id: "price_1TPZf1E0iuyRsYRx5YEsmw1p", name: "₡CC Legendary Bundle (140,000 credits)", amount: 999.99, currency: "USD", interval: "one-time" },
  ₡CC_CABAL_BUNDLE_500000_CREDITS: { price_id: "price_1TPZf1E0iuyRsYRxjXiLJH4i", name: "₡CC Cabal Bundle (500,000 credits)", amount: 2499.99, currency: "USD", interval: "one-time" },
};

function redirectToCheckout(priceId, successUrl, cancelUrl) {
  const stripe = Stripe(STRIPE_PK);
  stripe.redirectToCheckout({
    lineItems: [{ price: priceId, quantity: 1 }],
    mode: priceId.interval === 'one-time' ? 'payment' : 'subscription',
    successUrl: successUrl || window.location.origin + '/checkout/success.html',
    cancelUrl: cancelUrl || window.location.origin + '/checkout/canceled.html',
  });
}
