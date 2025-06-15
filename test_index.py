import unittest
from html.parser import HTMLParser

class PTagParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_p = False
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.in_p = True

    def handle_endtag(self, tag):
        if tag == 'p':
            self.in_p = False

    def handle_data(self, data):
        if self.in_p:
            self.text.append(data.strip())

class TestIndex(unittest.TestCase):
    def test_p_contains_hello_world(self):
        with open('index.html', encoding='utf-8') as f:
            parser = PTagParser()
            parser.feed(f.read())
        p_text = ' '.join(parser.text).strip()
        self.assertEqual(p_text, 'hello world')

if __name__ == '__main__':
    unittest.main()
