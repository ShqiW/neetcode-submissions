class Twitter:

    def __init__(self):
        self.count = 0
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1       

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                tweets = self.tweet_map[followeeId]
                index = len(tweets)-1
                count, tweetId = tweets[index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index])
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index= heapq.heappop(minHeap)
            res . append(tweetId)

            if index > 0:
                index -= 1
                count, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index])
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
