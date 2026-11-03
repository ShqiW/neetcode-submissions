class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        achieved = set()
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                if a == target[0]:
                    achieved.add(0)
                if b == target[1]:
                    achieved.add(1)
                if c == target[2]:
                    achieved.add(2)
        return len(achieved) == 3 