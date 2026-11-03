class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l, r = 0, 0

        while r < len(nums):
            # monostack: decreading, pop smaller from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # add current index
            q.append(r)

            # move left index
            while q[0] < l:
                q.popleft()

            # update maxnum
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res
