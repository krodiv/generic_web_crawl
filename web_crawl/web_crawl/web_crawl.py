from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup
 
@dataclass
class Page_content:
    home_url: str
    urls: list

    def get_all_url(self):
        req = requests.get(self.home_url)
        return req

    def find_all_href(self, content):
        soup = BeautifulSoup(content.text, 'html.parser')
        
        url = []
        for link in soup.find_all('a'):
            raw_link = link.get('href')
            if not isinstance(raw_link, str):
                continue
            if raw_link[:1] == '/':
                raw_link = self.prepend_url(raw_link)
            if raw_link not in url:
                url.append(raw_link)
        self.urls = url

    def prepend_url(self, suffex):
        new_str = self.home_url[:-1] + suffex
        return new_str

    def get_urls(self):
        return self.urls

    def build_url_map(self):
        req = self.get_all_url()
        self.find_all_href(req)


urls = Page_content('', [])
urls.build_url_map()
print(urls.get_urls)
