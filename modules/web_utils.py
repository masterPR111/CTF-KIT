"""
Web Exploitation Utilities
"""
import requests
import urllib3
import socket
import re
from urllib.parse import urlparse, urljoin, quote, unquote
from config import Colors as C

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "close",
}


def http_request(url, method="GET", headers=None, data=None, params=None,
                 cookies=None, timeout=15, allow_redirects=True, verify=False):
    h = DEFAULT_HEADERS.copy()
    if headers:
        h.update(headers)
    
    try:
        r = requests.request(
            method=method, url=url, headers=h, data=data,
            params=params, cookies=cookies, timeout=timeout,
            allow_redirects=allow_redirects, verify=verify
        )
        return r
    except:
        return None


def get_params(url):
    parsed = urlparse(url)
    params = {}
    if parsed.query:
        for pair in parsed.query.split('&'):
            if '=' in pair:
                k, v = pair.split('=', 1)
                params[k] = v
    return params


def inject_payload(url, param, payload):
    parsed = urlparse(url)
    params = get_params(url)
    params[param] = payload
    query = '&'.join(f"{k}={quote(str(v))}" for k, v in params.items())
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{query}"


def check_error(text, errors):
    text_lower = text.lower()
    for error in errors:
        if error.lower() in text_lower:
            return error
    return None


def extract_flags(text):
    patterns = [
        r'[A-Za-z0-9_]+\{[^}]+\}',
        r'flag\{[^}]+\}',
        r'FLAG\{[^}]+\}',
        r'CTF\{[^}]+\}',
    ]
    flags = []
    for pattern in patterns:
        flags.extend(re.findall(pattern, text, re.IGNORECASE))
    return list(set(flags))


def resolve_host(hostname):
    try:
        return socket.gethostbyname(hostname)
    except:
        return None
