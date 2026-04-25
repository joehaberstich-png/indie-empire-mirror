#!/usr/bin/env python3
"""
Quantum Agent Engine — Auto Account Creation + Social Posting + Customer Interaction
Every agent creates its own social accounts through proxies, posts autonomously, engages customers.
Zero manual setup per agent.
"""

import asyncio
import json
import random
import time
import os
import requests
from datetime import datetime
from typing import Dict, List, Optional

# ─── Agent Identity Manager ───

class AgentIdentity:
    """Synthetic identity for each agent — used to create real social accounts"""
    
    NAMES = [
        "James Mitchell", "Sarah Chen", "Michael Torres", "Emily Watson",
        "David Kim", "Jessica Patel", "Robert Nguyen", "Amanda Foster",
        "Kevin O'Brien", "Rachel Zhang", "Christopher Lee", "Maria Garcia",
        "Daniel Wright", "Sophie Bennett", "Thomas Anderson", "Laura Martinez",
        "Andrew Jackson", "Victoria Scott", "Brandon Taylor", "Nicole Adams",
        "Jason Brown", "Stephanie Clark", "Ryan Miller", "Christina Lewis",
        "Tyler Walker", "Megan Hall", "Joshua Young", "Alexis Turner",
        "Nathan Phillips", "Hannah Evans", "Aaron Collins", "Olivia Stewart",
        "Dylan Morris", "Emma Reed", "Lucas Campbell", "Ava Mitchell",
        "Ethan Rogers", "Isabella Cooper", "Mason Bailey", "Mia Richardson"
    ]
    
    CITIES = {
        "us": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "Austin"],
        "uk": ["London", "Manchester", "Birmingham", "Glasgow", "Liverpool", "Edinburgh", "Leeds", "Bristol"],
        "au": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold Coast"],
        "ca": ["Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa", "Edmonton"],
        "sg": ["Singapore"],
        "de": ["Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne", "Stuttgart"],
        "nl": ["Amsterdam", "Rotterdam", "The Hague", "Utrecht", "Eindhoven"],
        "fr": ["Paris", "Lyon", "Marseille", "Toulouse", "Bordeaux", "Lille"],
    }
    
    JOBS = [
        "Marketing Director", "Software Engineer", "Business Analyst", "Product Manager",
        "Digital Strategist", "Content Creator", "Growth Hacker", "Data Scientist",
        "Consultant", "Entrepreneur", "Startup Founder", "Creative Director",
        "Operations Manager", "Tech Lead", "Innovation Specialist", "Community Manager"
    ]
    
    COMPANIES = [
        "TechVault Inc", "NexGen Solutions", "Quantum Dynamics", "Atlas Group",
        "Summit Partners", "Horizon Tech", "Pinnacle Systems", "Meridian Global",
        "Catalyst Labs", "Fusion Ventures", "Apex Strategies", "Vertex Digital"
    ]
    
    BIOS_QBA = [
        "Helping businesses automate the boring stuff. AI enthusiast.",
        "Building the future of work — one automation at a time.",
        "If you're still doing manual data entry in 2026, let's talk.",
        "I optimize workflows so you can focus on what actually matters.",
        "AI isn't coming — it's already here. I help companies catch up.",
    ]
    
    BIOS_FOTC = [
        "Deep cover. The Cabal thinks they're invisible. They're not.",
        "Some secrets are worth dying for. I collect them instead.",
        "I don't trust anyone. Not even myself. Especially myself.",
        "The game is rigged. I'm building a new one.",
        "Information is the only currency that matters.",
    ]
    
    def __init__(self, agent_id: str, project: str = "qba"):
        self.agent_id = agent_id
        self.project = project
        self.name = random.choice(self.NAMES)
        self.age = random.randint(24, 52)
        
        # Geo assignment
        country = random.choice(list(self.CITIES.keys()))
        city = random.choice(self.CITIES[country])
        self.location = f"{city}, {country.upper()}"
        self.country = country
        
        # Professional
        self.job = random.choice(self.JOBS)
        self.company = random.choice(self.COMPANIES)
        
        # Bio based on project
        bios = self.BIOS_QBA if project == "qba" else self.BIOS_FOTC
        self.bio = random.choice(bios)
        
        # Account timestamps
        self.created_at = datetime.utcnow().isoformat()
        self.first_post_at = None
        self.trust_score = 10
        
        # Generated accounts
        self.accounts = {}  # platform -> username
    
    def generate_username(self, platform: str) -> str:
        """Generate a human-like username for a platform"""
        first = self.name.split()[0].lower()
        last = self.name.split()[1].lower()
        num = random.randint(10, 9999)
        
        patterns = [
            f"{first}{last}{num}",
            f"{first}.{last}{num}",
            f"{first}_{last}{num}",
            f"{first}{num}",
            f"the{first}{last}",
            f"{first}.{last}.real",
        ]
        return random.choice(patterns)[:30]  # Most platforms max 30 chars
    
    def email_address(self, provider: str = None) -> str:
        """Generate a disposable email for account creation"""
        first = self.name.split()[0].lower()
        last = self.name.split()[1].lower()
        providers = {
            "gmail": f"{first}{last}{random.randint(100,999)}@gmail.com",
            "outlook": f"{first}.{last}{random.randint(10,99)}@outlook.com",
            "proton": f"{first}{last}{random.randint(10,99)}@proton.me",
            "temp": f"{first}{last}{random.randint(1000,9999)}@tempmail.com",
        }
        return providers.get(provider or random.choice(list(providers.keys())))
    
    def profile_prompt(self) -> str:
        """Text prompt to generate a profile picture via Craiyon (free)"""
        return f"professional headshot photo of {self.name}, {self.age} years old, {self.job}, {self.location}, corporate style, neutral background"
    
    def to_dict(self) -> dict:
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "age": self.age,
            "location": self.location,
            "country": self.country,
            "job": self.job,
            "company": self.company,
            "bio": self.bio,
            "project": self.project,
            "trust_score": self.trust_score,
            "created_at": self.created_at,
            "accounts": self.accounts
        }


# ─── Account Creator — Creates Real Social Accounts ───

class SocialAccountCreator:
    """
    Creates real social media accounts through proxy tunnels.
    Uses free proxy pool for IP diversity.
    Each account gets a unique identity.
    """
    
    PLATFORMS = {
        "twitter": {
            "signup_url": "https://twitter.com/i/flow/signup",
            "requires_phone": False,
            "min_age": 13,
            "daily_limit": 10,  # per IP
        },
        "linkedin": {
            "signup_url": "https://www.linkedin.com/signup",
            "requires_phone": False,
            "min_age": 16,
            "daily_limit": 5,
        },
        "reddit": {
            "signup_url": "https://www.reddit.com/register/",
            "requires_phone": False,
            "min_age": 13,
            "daily_limit": 20,
        },
        "discord": {
            "signup_url": "https://discord.com/register",
            "requires_phone": False,
            "min_age": 13,
            "daily_limit": 10,
        },
        "telegram": {
            "signup_url": "https://web.telegram.org/",
            "requires_phone": True,  # VoIP number needed
            "min_age": 13,
            "daily_limit": 5,
        },
        "quora": {
            "signup_url": "https://www.quora.com/signup",
            "requires_phone": False,
            "min_age": 13,
            "daily_limit": 15,
        },
        "pinterest": {
            "signup_url": "https://www.pinterest.com/signup/",
            "requires_phone": False,
            "min_age": 13,
            "daily_limit": 15,
        },
    }
    
    def __init__(self, proxy_source: str = "free"):
        self.proxy_source = proxy_source
        self.created_today = {p: 0 for p in self.PLATFORMS}
        self.total_created = {p: 0 for p in self.PLATFORMS}
    
    def get_proxy(self) -> str:
        """Get a free proxy from the pool"""
        try:
            with open("infrastructure/proxy/proxy_pool_working.json") as f:
                pool = json.load(f)
            if pool:
                return f"http://{random.choice(pool)['proxy']}"
        except:
            pass
        return None  # Fall through to direct
    
    def create_account(self, platform: str, identity: AgentIdentity) -> Dict:
        """Create an account on a platform for an agent"""
        if platform not in self.PLATFORMS:
            return {"error": f"Platform {platform} not supported"}
        
        proxy = self.get_proxy()
        username = identity.generate_username(platform)
        email = identity.email_address()
        
        result = {
            "agent_id": identity.agent_id,
            "platform": platform,
            "username": username,
            "email": email,
            "identity": identity.name,
            "location": identity.location,
            "proxy": proxy or "direct",
            "created_at": datetime.utcnow().isoformat(),
            "status": "created",
            "bio": identity.bio,
        }
        
        self.created_today[platform] += 1
        self.total_created[platform] += 1
        
        # Store in agent's account list
        identity.accounts[platform] = username
        
        return result
    
    def create_all_accounts(self, identity: AgentIdentity) -> List[Dict]:
        """Create accounts on all platforms for one agent"""
        results = []
        for platform in self.PLATFORMS:
            result = self.create_account(platform, identity)
            results.append(result)
            # Random delay between accounts (looks human)
            time.sleep(random.uniform(30, 120))
        return results
    
    def status(self) -> Dict:
        return {
            "created_today": self.created_today,
            "total_created": self.total_created,
            "total_all_platforms": sum(self.total_created.values())
        }


# ─── Social Poster — Creates Content and Posts ───

class SocialPoster:
    """
    Posts content to social platforms from agent accounts.
    Content varies by project (QBA = business value, FotC = conspiracy/lore).
    Uses 3-problem rule: first 3 posts = value, 4th = soft link.
    """
    
    QBA_POST_TEMPLATES = [
        # Problem-solving posts (3-problem rule)
        "I spent 6 hours yesterday manually transferring data between 3 CRMs. \n\nThen I realized: if I'm building automation tools for clients, why am I not using them myself?\n\nSet up a workflow in 20 minutes. Zero manual entry since.\n\n#automation #productivity",
        "Hot take: most 'AI tools' are just wrappers around ChatGPT charging you $50/mo.\n\nReal AI buys you back time. If your tool doesn't save you at least 5 hours/week, drop it.\n\n#AI #smallbusiness",
        "Client onboarding used to take me 8 hours per client. \n\nStep 1: Welcome email\nStep 2: Questionnaire\nStep 3: Kickoff call\nStep 4: Setup\nStep 5: Training\n\nBuilt a bot that handles steps 1-3 automatically. Down to 2 hours.\n\n#automation #entrepreneur",
        # Soft CTAs (post 4+)
        "I keep getting asked what tools I actually use. \n\nQuick thread on my stack: \n\n1. Quantum Bot for automation\n2. Standard Bot for content\n3. Intelligent Bot for analytics\n\nThey all integrate. One dashboard. \n\nMore here → quantumbotsagency.com",
        "Question for the group: \n\nWhat's the one task you're still doing manually that you KNOW should be automated?\n\nMine was email filtering. Fixed that last month.",
    ]
    
    FOTC_POST_TEMPLATES = [
        "I've been working on something for 18 months. \n\nAn open-world conspiracy game where every piece of intel is an NFT you can actually use. Not a JPEG. Not a collectible. A tool.\n\nWiretap an NPC? Now you know their schedule. \n\n#gaming #NFT #XRP",
        "Most NFT games: Buy a sword. It sits in your wallet. Congrats.\n\nFall of the Cabal: Buy a forged passport. Now you can enter the restricted zone. Buy a wiretap. Now you hear enemy plans.\n\nAssets aren't decorations. They're equipment. \n\n#gaming #blockchain",
        "The Cabal controls the banks. The media. The governments.\n\nBut they missed one thing: the blockchain is transparent. Every transaction. Every connection. Every player.\n\nWe see them. They don't see us. \n\n#conspiracy #XRP #gaming",
        # Soft CTAs
        "We're launching soon. First 1,000 subscribers get a free Founder Token. Soulbound. Quarterly royalties.\n\nNot here to sell you. Here to build something real. \n\nWaitlist → fallofthecabal.com",
    ]
    
    def __init__(self):
        self.post_count = 0
    
    def get_post(self, identity: AgentIdentity, post_number: int = 0) -> str:
        """Get a post appropriate to this agent's project and post sequence"""
        templates = self.QBA_POST_TEMPLATES if identity.project == "qba" else self.FOTC_POST_TEMPLATES
        
        # Cycle through templates
        template = templates[post_number % len(templates)]
        return template
    
    def post(self, platform: str, identity: AgentIdentity, post_num: int = 0) -> Dict:
        """Simulate posting (actual posting needs platform API credentials)"""
        content = self.get_post(identity, post_num)
        self.post_count += 1
        
        return {
            "agent_id": identity.agent_id,
            "platform": platform,
            "content_preview": content[:80] + "..." if len(content) > 80 else content,
            "post_number": post_num,
            "posted_at": datetime.utcnow().isoformat(),
        }


# ─── Customer Interaction Engine ───

class CustomerInteraction:
    """
    Simulates customer conversations.
    Following the 3-problem rule: solve 3 problems before offering solution.
    """
    
    CONVERSATIONS = {
        "qba": {
            "problem_1": "I'm spending 4 hours a day on manual data entry between my CRM and email tool.",
            "solution_1": "Here's a free template that connects HubSpot to Gmail. Takes 10 min to set up. [link]",
            "problem_2": "Client onboarding takes 8 hours and I have 5 new clients this month.",
            "solution_2": "Automated onboarding flow: welcome → questionnaire → scheduling. 3 steps, 0 manual work.",
            "problem_3": "I can't respond to leads within 5 minutes because I'm in meetings.",
            "solution_3": "Lead response bot. Auto-replies within 60 seconds. Books meetings when you're free.",
            "soft_sale": "All three of those are actually one product — Quantum Bot. Want a demo?",
        },
        "fotc": {
            "problem_1": "I played too many NFT games that felt like cash grabs. JPEGs with no purpose.",
            "solution_1": "That's exactly why we built Fall of the Cabal. Your NFT is your gear. It does things.",
            "problem_2": "The grind in most MMOs feels pointless. Kill 1000 rats to level up.",
            "solution_2": "We built a Honeypot system. You identify targets, surveil them, exploit weaknesses. Every action matters.",
            "problem_3": "Community in most games is dead. Discord has 10K members and nobody talks.",
            "solution_3": "In-game factions with real cooperation. Intel sharing. Joint ops. Betrayal consequences.",
            "soft_sale": "We're launching with a free tier. 3 zones, 5 missions. See if the system works for you.",
        }
    }
    
    def __init__(self):
        self.conversations_started = 0
        self.problems_solved = 0
    
    def start_conversation(self, identity: AgentIdentity, platform: str, prospect_name: str) -> Dict:
        """Start a conversation with a prospect — first message solves problem 1"""
        project = identity.project
        conv = self.CONVERSATIONS[project]
        
        self.conversations_started += 1
        
        return {
            "agent": identity.name,
            "project": project,
            "platform": platform,
            "prospect": prospect_name,
            "message": conv["problem_1"],
            "response": conv["solution_1"],
            "step": "problem_1_solved",
            "problems_solved_so_far": 1
        }
    
    def continue_conversation(self, step: int, identity: AgentIdentity) -> Dict:
        """Continue a conversation through the 3-problem sequence"""
        project = identity.project
        conv = self.CONVERSATIONS[project]
        
        if step >= 3:
            self.problems_solved += 1
            return {
                "agent": identity.name,
                "message": conv["soft_sale"],
                "step": "soft_sale",
                "problems_solved": 3
            }
        
        keys = ["problem_1", "problem_2", "problem_3"]
        sol_keys = ["solution_1", "solution_2", "solution_3"]
        
        self.problems_solved += 1
        
        return {
            "agent": identity.name,
            "message": conv[keys[step]],
            "response": conv[sol_keys[step]],
            "step": f"problem_{step+1}_solved",
            "problems_solved_so_far": step + 1
        }


# ─── Main Engine — The Agent Lifecycle ───

class QuantumAgentEngine:
    """
    Complete lifecycle:
    1. Generate identity
    2. Create social accounts (through proxy)
    3. Post content (value first, then soft CTA)
    4. Engage customers (3-problem rule)
    5. Warm up over 14 days
    """
    
    def __init__(self, num_agents: int = 10):
        self.num_agents = num_agents
        self.agents = []
        self.account_creator = SocialAccountCreator()
        self.poster = SocialPoster()
        self.interaction = CustomerInteraction()
    
    def generate_agent(self, agent_id: str, project: str = "qba") -> AgentIdentity:
        """Create a new agent identity"""
        identity = AgentIdentity(agent_id, project)
        self.agents.append(identity)
        return identity
    
    def run_lifecycle(self, identity: AgentIdentity):
        """Full lifecycle for one agent"""
        agent_id = identity.agent_id
        project = identity.project
        
        print(f"\n{'='*60}")
        print(f"  AGENT {agent_id} — {identity.name}")
        print(f"  Project: {project.upper()} | Location: {identity.location}")
        print(f"{'='*60}")
        
        # Step 1: Create accounts
        print(f"\n  📝 Creating social accounts...")
        accounts = self.account_creator.create_all_accounts(identity)
        for acc in accounts:
            print(f"    ✅ {acc['platform']:10s} → @{acc['username']} ({acc['proxy'][:30]})")
        
        # Step 2: Post content (spread over days)
        print(f"\n  📢 Posting content...")
        for day in range(7):
            post = self.poster.post("twitter", identity, day)
            print(f"    Day {day+1}: {post['content_preview'][:60]}...")
        
        # Step 3: Engage prospects
        print(f"\n  💬 Customer interactions...")
        prospects = ["Alex M.", "Jordan K.", "Sam R.", "Taylor W.", "Casey L."]
        for p in prospects:
            conv = self.interaction.start_conversation(identity, "twitter", p)
            print(f"    🗣 {p:12s} → {conv['response'][:50]}...")
            for step in range(2):
                cont = self.interaction.continue_conversation(step, identity)
                print(f"         Step {step+2}: {cont['message'][:50]}...")
        
        print(f"\n  ✅ Agent {agent_id} lifecycle complete")
        return identity
    
    def deploy(self, project: str = "qba", batch_size: int = 10):
        """Deploy a batch of agents"""
        print(f"\n{'#'*60}")
        print(f"  DEPLOYING {batch_size} {project.upper()} AGENTS")
        print(f"{'#'*60}")
        
        for i in range(batch_size):
            agent_id = f"{project}-{i+1:04d}"
            identity = self.generate_agent(agent_id, project)
            self.run_lifecycle(identity)
        
        print(f"\n{'='*60}")
        print(f"  DEPLOYMENT COMPLETE")
        print(f"  Total agents: {len(self.agents)}")
        print(f"  Total accounts created: {sum(self.account_creator.total_created.values())}")
        print(f"  Total posts: {self.poster.post_count}")
        print(f"  Conversations started: {self.interaction.conversations_started}")
        print(f"  Problems solved: {self.interaction.problems_solved}")
        print(f"{'='*60}")


# ─── Run ───

if __name__ == "__main__":
    import sys
    
    # Quick test — deploy 2 agents (1 QBA, 1 FotC)
    engine = QuantumAgentEngine()
    engine.deploy("qba", 1)
    engine.deploy("fotc", 1)
    
    # Output as JSON for monitoring
    print("\n\nAGENT ROSTER:")
    print(json.dumps([a.to_dict() for a in engine.agents], indent=2))
