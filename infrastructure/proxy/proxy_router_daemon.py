#!/usr/bin/env python3
"""
Proxy Router & Smart Scraper Daemon
- Auto-harvests free proxies from 10+ sources
- Tests with 3-second timeout
- Routes ALL outbound calls through proxies via rotation
- Zero delay workflow — never blocked by rate limits
"""

import json, os, sys, time, threading, random, socket, ssl
from urllib.request import Request, urlopen, ProxyHandler, build_opener, install_opener
from urllib.error import URLError

PROXY_FILE = os.path.join(os.path.dirname(__file__), 'proxy_pool_working.json')
LOG_FILE = '/dev/null'

class ProxyRouter:
    def __init__(self):
        self.lock = threading.Lock()
        self.working = {}
        self.blacklist = set()
        self.index = 0
        self.load()
        # Start background refresh
        threading.Thread(target=self._refresh_loop, daemon=True).start()

    def load(self):
        try:
            with open(PROXY_FILE) as f:
                raw = json.load(f)
                for p in raw:
                    if isinstance(p, dict) and 'proxy' in p:
                        self.working[p['proxy']] = p.get('latency', 1000)
                    elif isinstance(p, str):
                        self.working[p] = 1000
        except: self.working = {}

    def save(self):
        data = [{'proxy': k, 'latency': v} for k,v in self.working.items()]
        with open(PROXY_FILE, 'w') as f:
            json.dump(data, f, indent=2)

    def _scrape_sources(self):
        """Harvest from 10+ free proxy sources"""
        sources = [
            # API-based (fast, structured)
            ('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all', 'text'),
            ('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all', 'text'),
            ('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all', 'text'),
            ('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt', 'text'),
            ('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt', 'text'),
            ('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt', 'text'),
            ('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt', 'text'),
            ('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt', 'text'),
            ('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt', 'text'),
            ('https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTP_RAW.txt', 'text'),
            ('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt', 'text'),
            ('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt', 'text'),
            # JSON API sources
            ('https://openproxy.space/list/http', 'json'),
            ('https://openproxy.space/list/socks4', 'json'),
            ('https://openproxy.space/list/socks5', 'json'),
            ('https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc', 'json'),
            ('https://proxylist.geonode.com/api/proxy-list?limit=500&page=2&sort_by=lastChecked&sort_type=desc', 'json'),
        ]

        all_proxies = set()
        for url, fmt in sources:
            try:
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                ctx = ssl.create_default_context()
                ctx.che[REDACTED] = False
                ctx.verify_mode = ssl.CERT_NONE
                resp = urlopen(req, timeout=8, context=ctx)
                data = resp.read().decode('utf-8', errors='ignore')

                if fmt == 'json':
                    try:
                        obj = json.loads(data)
                        if isinstance(obj, list):
                            for entry in obj:
                                if isinstance(entry, str):
                                    all_proxies.add(entry.strip())
                                elif isinstance(entry, dict):
                                    ip = entry.get('ip', '')
                                    port = entry.get('port', '') or entry.get('portHTTP', '')
                                    if ip and port: all_proxies.add(f'{ip}:{port}')
                        elif isinstance(obj, dict):
                            for key in ('data', 'proxies', 'list', 'result'):
                                items = obj.get(key, [])
                                if isinstance(items, list):
                                    for item in items:
                                        if isinstance(item, str):
                                            all_proxies.add(item.strip())
                                        elif isinstance(item, dict):
                                            ip = item.get('ip', '')
                                            port = str(item.get('port', '') or item.get('portHTTP', '') or item.get('portSSL', ''))
                                            if ip and port: all_proxies.add(f'{ip}:{port}')
                    except: pass
                else:
                    for line in data.split('\n'):
                        line = line.strip()
                        if line and ':' in line and not line.startswith('#'):
                            all_proxies.add(line)
            except: pass

        return list(all_proxies)

    def _test_proxy(self, proxy):
        """Quick connectivity test"""
        if proxy in self.blacklist:
            return None
        try:
            parts = proxy.split(':')
            if len(parts) != 2: return None
            ip, port = parts[0], int(parts[1])
            start = time.time()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((ip, port))
            s.close()
            latency = int((time.time() - start) * 1000)
            return latency
        except: return None

    def refresh(self):
        """Full scrape + test cycle"""
        print(f'[proxy] Scraping free proxy sources...', flush=True)
        raw = self._scrape_sources()
        print(f'[proxy] Got {len(raw)} raw proxies, testing...', flush=True)

        tested = {}
        for i, proxy in enumerate(raw):
            if len(tested) >= 200:  # Keep top 200 for speed
                break
            lat = self._test_proxy(proxy)
            if lat is not None:
                tested[proxy] = lat

        with self.lock:
            self.working = tested
            self.save()

        print(f'[proxy] Pool refreshed: {len(tested)} working proxies', flush=True)

    def _refresh_loop(self):
        """Auto-refresh every 15 minutes"""
        time.sleep(5)  # Initial delay
        while True:
            try: self.refresh()
            except: pass
            time.sleep(900)  # 15 min

    def get_proxy(self):
        """Get next working proxy in rotation"""
        with self.lock:
            if not self.working:
                # Fallback: Tor if available
                return 'socks5://127.0.0.1:9050'
            keys = list(self.working.keys())
            if self.index >= len(keys):
                self.index = 0
            proxy = keys[self.index]
            self.index = (self.index + 1) % len(keys)
            return proxy

    def get_opener(self):
        """Get urlopen opener with a working proxy"""
        proxy = self.get_proxy()
        # Try HTTP, SOCKS5
        handler = ProxyHandler({
            'http': f'http://{proxy}',
            'https': f'http://{proxy}'
        })
        ctx = ssl.create_default_context()
        ctx.che[REDACTED] = False
        ctx.verify_mode = ssl.CERT_NONE
        return build_opener(handler), proxy

    def fetch(self, url, timeout=15):
        """Fetch with automatic proxy rotation and retry"""
        max_retries = 5
        last_error = None
        for attempt in range(max_retries):
            try:
                opener, used_proxy = self.get_opener()
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                resp = opener.open(req, timeout=timeout)
                return resp.read().decode('utf-8', errors='ignore')
            except Exception as e:
                last_error = str(e)
                if attempt < max_retries - 1:
                    time.sleep(0.5)
        raise Exception(f'All proxies failed for {url}: {last_error}')


def main():
    router = ProxyRouter()
    print(f'[proxy] Proxy Router Daemon — 24/7 Zero-Delay')
    print(f'[proxy] Pool: {len(router.working)} proxies')
    print(f'[proxy] Starting background refresh cycle (every 15min)...')

    if len(router.working) < 10:
        print(f'[proxy] Pool small — running immediate scrape...')
        router.refresh()

    # Serve as long-lived daemon
    while True:
        time.sleep(60)

if __name__ == '__main__':
    main()
