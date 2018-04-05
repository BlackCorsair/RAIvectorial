#!venv/bin/python
from bs4 import BeautifulSoup, Comment


class HTMLParser:
    def __init__(self):
        print("HTMLParser init")

    def parse(self, html_doc):
        soup = BeautifulSoup(html_doc, 'lxml',
                             from_encoding='ASCII', exclude_encodings='UTF-8')
        # Remove scripts and styles
        for x in soup.findAll('script', 'style', 'href', 'a'):
            x.extract()
        # Avoid commets2010-17-011.html
        comments = soup.findAll(text=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()
        return soup.get_text()
