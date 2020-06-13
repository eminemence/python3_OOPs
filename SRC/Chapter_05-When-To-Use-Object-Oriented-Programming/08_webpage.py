from urllib.request import urlopen
import time


class WebPage(object):
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        return self._content


if __name__ == "__main__":
    webapage = WebPage("http://ccphillips.net")
    now = time.time()
    content1 = webapage.content
    print(time.time() - now)
    now = time.time()
    content2 = webapage.content
    print(time.time() - now)
    print(content1 == content2)
