/**
 * Fall of the Cabal — XRPL NFT Mint Endpoint
 * POST /api/mint -> Stripe webhook -> NFTokenMint -> deliver to wallet
 * 
 * Flow: Stripe Checkout → Webhook → This endpoint → XRPL Mainnet → Wallet
 */
const XRPL = require('xrpl');

// XRPL Mainnet connection
const XRPL_SERVER = 'wss://xrplcluster.com'; // Mainnet

// Fee wallet (receives mint payments)
const FEE_WALLET_SEED = process.env.XRPL_ISSUER_SEED; // Set in environment

const RARITIES = {
  normal: { taxon: 1, fee: 0 },
  uncommon: { taxon: 2, fee: 5 },
  rare: { taxon: 3, fee: 10 },
  epic: { taxon: 4, fee: 25 },
  legendary: { taxon: 5, fee: 50 },
  mythic: { taxon: 6, fee: 100 },
  mystic: { taxon: 7, fee: 250 },
};

const NFT_CATEGORIES = {
  intel: 'Intel Document',
  identity: 'Identity',
  weapon: 'Weapon',
  vehicle: 'Vehicle',
  safehouse: 'Safehouse',
  honeypot: 'Honeypot',
  territory: 'Territory',
  codename: 'Codename',
};

const NFT_NAMES = {
  1: ['Surveillance Photo', 'Wiretap Transcript', 'Bank Record', 'Email Dump', 'Phone Log'],
  2: ['Diplomatic Passport', 'Cover Identity', 'Media Credentials', 'Military ID', 'Security Clearance'],
  3: ['Classified File', 'Operation Dossier', 'Black Site Location', 'Asset List', 'Dead Drop Map'],
  4: ['Honey Pot Blueprint', 'Cabal Org Chart', 'Money Trail Map', 'Double Agent File', 'Election Interference Proof'],
  5: ['Golden Dossier', 'Ghost Identity', 'The Black Book', 'Founders Document', 'Endgame Protocol'],
  6: ['One-of-a-kind Asset', 'Unique Operation', 'Legendary Intel'],
  7: ['Mystic Artifact', 'The Unseen', 'Final Truth'],
};

const NFT_IMAGES = {
  1: '/fallofthecabal/assets/nft/intel-normal.png',
  2: '/fallofthecabal/assets/nft/intel-uncommon.png',
  3: '/fallofthecabal/assets/nft/intel-rare.png',
  4: '/fallofthecabal/assets/nft/intel-epic.png',
  5: '/fallofthecabal/assets/nft/intel-legendary.png',
  6: '/fallofthecabal/assets/nft/intel-mythic.png',
  7: '/fallofthecabal/assets/nft/intel-mystic.png',
};

let client = null;

async function getClient() {
  if (!client) {
    client = new XRPL.Client(XRPL_SERVER);
    await client.connect();
  }
  return client;
}

async function mintNFT({ rarity, category, walletAddress, customerEmail }) {
  const c = await getClient();
  
  // Load fee wallet (the game's issuer wallet)
  if (!FEE_WALLET_SEED) {
    throw new Error('XRPL_ISSUER_SEED not set in environment');
  }
  const feeWallet = XRPL.Wallet.fromSeed(FEE_WALLET_SEED);
  
  const rarityData = RARITIES[rarity] || RARITIES.normal;
  const categoryName = NFT_CATEGORIES[category] || NFT_CATEGORIES.intel;
  
  // Generate unique NFT name from the pool
  const namePool = NFT_NAMES[rarityData.taxon] || NFT_NAMES[1];
  const nftName = namePool[Math.floor(Math.random() * namePool.length)];
  
  // Build URI metadata (IPFS would be better, inline JSON for MVP)
  const metadata = JSON.stringify({
    name: `${categoryName}: ${nftName}`,
    description: `Fall of the Cabal - ${rarity.toUpperCase()} ${categoryName}`,
    image: NFT_IMAGES[rarityData.taxon] || NFT_IMAGES[1],
    attributes: [
      { trait_type: 'Rarity', value: rarity.toUpperCase() },
      { trait_type: 'Category', value: categoryName },
      { trait_type: 'Taxon', value: rarityData.taxon },
      { trait_type: 'Edition', value: 1 },
      { trait_type: 'Serial', value: Date.now().toString(36).toUpperCase() },
      { trait_type: 'Location', value: 'Washington DC' },
      { trait_type: 'Game', value: 'Fall of the Cabal' },
    ],
    properties: {
      minted_for: customerEmail || 'anonymous',
      mint_timestamp: new Date().toISOString(),
      game_version: '1.0.0-prealpha',
    },
  });
  
  // Hex encode the URI
  const uri = Buffer.from(metadata).toString('hex').toUpperCase();
  
  // Mint transaction
  const tx = {
    TransactionType: 'NFTokenMint',
    Account: feeWallet.classicAddress,
    URI: uri,
    Flags: 8, // lsfTransferable
    TransferFee: rarityData.fee * 100, // Basis points (0-50000)
    NFTokenTaxon: rarityData.taxon,
    Issuer: feeWallet.classicAddress,
  };
  
  const prepared = await c.autofill(tx);
  const signed = feeWallet.sign(prepared);
  const result = await c.submitAndWait(signed.tx_blob);
  
  if (result.result.meta.TransactionResult !== 'tesSUCCESS') {
    throw new Error(`Mint failed: ${result.result.meta.TransactionResult}`);
  }
  
  // Extract NFTokenID from metadata
  const nftID = result.result.meta.AffectedNodes
    .find(n => n.CreatedNode?.LedgerEntryType === 'NFTokenPage')
    ?.CreatedNode?.NewFields?.NFTokens?.[0]?.NFToken?.NFTokenID;
  
  // Send to buyer wallet (transfer)
  if (walletAddress && nftID) {
    const sendTx = {
      TransactionType: 'NFTokenCreateOffer',
      Account: feeWallet.classicAddress,
      NFTokenID: nftID,
      Amount: '0', // Free transfer to buyer
      Destination: walletAddress,
      Flags: 1, // lsfSellNFToken
    };
    const sendPrepared = await c.autofill(sendTx);
    const sendSigned = feeWallet.sign(sendPrepared);
    await c.submitAndWait(sendSigned.tx_blob);
  }
  
  return {
    success: true,
    nftID: nftID,
    name: nftName,
    category: categoryName,
    rarity: rarity,
    txHash: result.result.hash,
    metadata: JSON.parse(metadata),
  };
}

async function mintFounderToken(walletAddress, subscriberNumber) {
  const c = await getClient();
  const feeWallet = XRPL.Wallet.fromSeed(FEE_WALLET_SEED);
  
  if (subscriberNumber > 1000) {
    throw new Error('All 1,000 Founder Tokens have been claimed');
  }
  
  const metadata = JSON.stringify({
    name: `Founders Pledge — FP-${String(subscriberNumber).padStart(4, '0')}`,
    description: 'First 1,000 — Soulbound. Cannot be traded or sold.',
    image: '/fallofthecabal/assets/nft/founder-token.png',
    attributes: [
      { trait_type: 'Type', value: 'Founders Token' },
      { trait_type: 'Serial', value: `FP-${String(subscriberNumber).padStart(4, '0')}` },
      { trait_type: 'Soulbound', value: 'True' },
      { trait_type: 'Benefit', value: 'Quarterly Royalty Split +25% Intel' },
    ],
    properties: {
      mint_type: 'founders_pledge',
      reason: 'first_1000_subscribers',
      mint_timestamp: new Date().toISOString(),
    },
  });
  
  const uri = Buffer.from(metadata).toString('hex').toUpperCase();
  
  // Mint as lsfOnlyXRP (blockchain-tradeable — not sold in our store)
  const tx = {
    TransactionType: 'NFTokenMint',
    Account: feeWallet.classicAddress,
    URI: uri,
    Flags: 0, // Blockchain-tradeable - storable in wallet
    NFTokenTaxon: 0,
    Issuer: feeWallet.classicAddress,
  };
  
  const prepared = await c.autofill(tx);
  const signed = feeWallet.sign(prepared);
  const result = await c.submitAndWait(signed.tx_blob);
  
  if (result.result.meta.TransactionResult !== 'tesSUCCESS') {
    throw new Error(`Founder mint failed: ${result.result.meta.TransactionResult}`);
  }
  
  // Transfer Founder Token to buyer wallet
  const nftID = result.result.meta.AffectedNodes
    .find(n => n.CreatedNode?.LedgerEntryType === 'NFTokenPage')
    ?.CreatedNode?.NewFields?.NFTokens?.[0]?.NFToken?.NFTokenID;
  
  if (walletAddress && nftID) {
    const sendTx = {
      TransactionType: 'NFTokenCreateOffer',
      Account: feeWallet.class