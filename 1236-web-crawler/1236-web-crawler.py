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
        start_hostname = self.parse_hostname(startUrl)
        queue = deque([startUrl])
        visited = {startUrl}

        while queue:
            current_url = queue.popleft()
            for next_url in htmlParser.getUrls(current_url):
                if self.parse_hostname(next_url) != start_hostname:
                    continue
                if next_url in visited:
                    continue
                
                visited.add(next_url)
                queue.append(next_url)
        
        return visited

    def parse_hostname(self, url: str):
        return url.split("/")[2]

        

        