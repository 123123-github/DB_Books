import requests
from bs4 import BeautifulSoup


# url --> html text
def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print("get html error!")
        raise


