class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list) 
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.following:
            self.following[userId] = set()
        if userId not in self.tweets:    
            self.tweets[userId] = []
        self.tweets[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        heap = []
        for f in users:
            if self.tweets[f]:
                t , tweetid = self.tweets[f][-1]
                heap.append((-t, tweetid, len(self.tweets[f])-1,f))
        heapq.heapify(heap)
        result = []
        while heap and len(result) < 10:
            t , tweetid, idx, f = heapq.heappop(heap)
            result.append(tweetid)
            if idx > 0:
                t , tweetid = self.tweets[f][idx-1]
                heapq.heappush(heap, (-t,tweetid, idx-1, f))
        return result
    def follow(self, followerId: int, followeeId: int) -> None:
        # if followeeId in self.followed:
        self.following[followerId].add(followeeId)
        # else:
        #     self.followed[followeeId] = set([followerId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # if followeeId in self.followed and followerId in self.followed[followeeId]:
        self.following[followerId].discard(followeeId)
        
