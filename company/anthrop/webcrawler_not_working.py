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
        self.domain = self.getDomain(startUrl)
        self.htmlParser = htmlParser
        with ThreadPoolExecutor(max_workers = 8) as executor:
            self.executor = executor
            self.executor.submit(self.parseUrl, startUrl)
        return list(self.visted)
    
    def parseUrl(self, url):
        for next in self.htmlParser.getUrls(url):
            with self.lock:
                if next not in self.visted and self.getDomain(next) == self.domain:
                    self.visted.add(next)
                    self.executor.submit(self.parseUrl, next)
    
    def getDomain(self, url):
        return url.split('/')[2]
        

# it is not working, since I kick off 8 works, but main thread is done without waiting for thead complete              
            

        