from bs4 import BeautifulSoup

class HTMLParser:
    def __init__(self):
        print("HTMLParser init")

    def parse(self, html_doc):
        print(html_doc)
        #print(html_doc.readlines().decode('utf-8', 'ignore'))
        soup = BeautifulSoup(html_doc.read(), 'lxml')
        soup = soup.prettify('utf-8', 'ignore')
        print(soup)
        soup = BeautifulSoup(soup, 'html.parser')
        print(soup.get_text('ignore'))
        return soup.get_text()

'''
parser = HTMLParser()
parser.parse("""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
""")
'''