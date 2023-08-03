import requests

# pip install django
# django-admin startproject example
# python manage.py runserver

def get_info_by_ip(ip_address) -> dict:
    address = ip_address.strip()
    url = f"https://ipinfo.io/widget/demo/{address}"
    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:112.0) Gecko/20100101 Firefox/112.0",
        "Referer": "https://ipinfo.io/",
        "Alt-Used": "ipinfo.io",
    }
    return requests.get(url, headers=headers).json()

