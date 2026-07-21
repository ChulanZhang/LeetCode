class Leaderboard:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] = self.scores.get(playerId, 0) + score
        
    def top(self, K: int) -> int:
        scores = sorted(self.scores.values(), reverse = True)
        return sum(scores[:K])

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

# time complexity: O(NlogN) for top, O(1) for addscore and reset
# space complexity: O(N) for hashmap
# https://bytebytego.com/courses/system-design-interview/real-time-gaming-leaderboard