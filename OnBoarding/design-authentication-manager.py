class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = {}
        self.t = timeToLive

        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = [currentTime, currentTime+self.t]
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and currentTime < self.tokens[tokenId][1]:
            self.tokens[tokenId][1] = currentTime + self.t

    def countUnexpiredTokens(self, currentTime: int) -> int:
        c = 0
        for tokenId in self.tokens:
            if currentTime < self.tokens[tokenId][1]:
                c += 1
        return c
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)