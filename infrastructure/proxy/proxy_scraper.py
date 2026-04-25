#!/usr/bin/env python3
"""
Free Proxy Scraper & Pool Manager
Collects, tests, and maintains a pool of free working proxies
Runs as a service — no cost, no accounts needed
"""

import asyncio
import aiohttp
import json
import time
import random
import os
import logging
from datetime import datetime
from typing import List, Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("proxy_scraper")

PROXY_FILE = os.path.join(os.path.dirname(__file__), "proxy_pool.json")
WORKING_FILE = os.path.join(os.path.dirname(__file__), "proxy_pool_working.json")

SOURCES = [
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTP_RAW.txt",
    "https://raw.githubusercontent.com/almorp/ProxyScraper/main/proxies.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/volvotiger/Proxies/main/http.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
    "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/free.txt",
]

TEST_URLS = [
    "http://httpbin.org/ip",
    "https://httpbin.org/ip",
    "https://api.ipify.org?format=json",
]

class ProxyScraper:
    def __init__(self):
        self.pool: List[Dict] = []
        self.working_pool: List[Dict] = []

    async def fetch_source(self, session, url):
        try:
            async with session.get(url, timeout=10) as resp:
                text = await resp.text()
                proxies = [line.strip() for line in text.split("\\n")
                          if line.strip() and ":" in line and not line.startswith("#")]
                return proxies
        except:
            return []

    async def scrape_all(self):
        all_proxies = set()
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_source(session, url) for url in SOURCES]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            for proxies in results:
                if isinstance(proxies, list):
                    all_proxies.update(proxies)
        return list(all_proxies)

    async def test_proxy(self, session, proxy):
        proxy_url = f"http://{proxy}"
        for test_url in TEST_URLS:
            try:
                async with session.get(test_url, proxy=proxy_url, timeout=5) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        ip = data.get("origin", proxy.split(":")[0])
                        return {
                            "proxy": proxy,
                            "ip": ip,
                            "protocol": "http",
                            "tested_at": datetime.utcnow().isoformat()
                        }
            except:
                pass
        return None

    async def verify_pool(self, proxies, max_test=100):
        working = []
        async with aiohttp.ClientSession() as session:
            for i in range(0, min(len(proxies), max_test), 20):
                batch = proxies[i:i+20]
                tasks = [self.test_proxy(session, p) for p in batch]
                results = await asyncio.gather(*tasks)
                for r in results:
                    if r:
                        working.append(r)
                await asyncio.sleep(2)
        return working

    async def full_refresh(self):
        logger.info("Scraping free proxy sources...")
        all_proxies = await self.scrape_all()
        logger.info(f"Got {len(all_proxies)} raw proxies")

        logger.info(f"Testing up to {min(len(all_proxies), 200)} proxies...")
        working = await self.verify_pool(all_proxies, max_test=200)

        self.pool = [{"proxy": p} for p in all_proxies]
        self.working_pool = working

        with open(PROXY_FILE, "w") as f:
            json.dump(self.pool, f, indent=2)
        with open(WORKING_FILE, "w") as f:
            json.dump(self.working_pool, f, indent=2)

        logger.info(f"Saved: {len(self.pool)} raw, {len(self.working_pool)} working")
        return working

    def get_proxy(self, agent_id=None):
        if not self.working_pool:
            return {"proxy": "tor", "fallback": True}
        p = random.choice(self.working_pool)
        return {**p, "agent_id": agent_id or "unknown"}

    def get_http(self, agent_id=None):
        p = self.get_proxy(agent_id)
        return f"http://{p['proxy']}"

async def main():
    scraper = ProxyScraper()
    await scraper.full_refresh()
    print(f"\\nProxy pool: {len(scraper.pool)} raw, {len(scraper.working_pool)} working")
    test = scraper.get_proxy(agent_id="agent-001")
    print(f"Test proxy for agent-001: {test['proxy']}")

if __name__ == "__main__":
    asyncio.run(main())
