class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counter = Counter(hand)
        sorted_key = sorted(counter.keys())

        for num in sorted_key:
            while counter[num] > 0:
                for i in range(groupSize):
                    current = num + i
                    if counter[current] <= 0:
                        return False
                    counter[current] -= 1
        return True