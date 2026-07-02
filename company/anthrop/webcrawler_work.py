import threading
from concurrent.futures import ThreadPoolExecutor

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        if not startUrl:
            return []
        self.lock = threading.Lock()
        self.visted = {startUrl}
        self.result = []
        # if have #

        self.domain = self.getDomain(startUrl)
        self.htmlParser = htmlParser
        self.done = threading.Event()
        self.pending = 1

        with ThreadPoolExecutor(max_workers = 8) as executor:
            self.executor = executor
            self.executor.submit(self.parseUrl, startUrl)
            self.done.wait()
        return list(self.visted)
    
    def parseUrl(self, url):
        nextList = self.htmlParser.getUrls(url)
        with self.lock:
            for next in nextList:
                if next not in self.visted and self.getDomain(next) == self.domain:
                    self.visted.add(next)
                    self.executor.submit(self.parseUrl, next)
                    self.pending += 1
            self.pending -= 1
            if self.pending == 0:
                self.done.set()
    
    def getDomain(self, url):
        return url.split('/')[2]
        

                
            

        