class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas: [1,2,3,4,5]
        # cost: [3,4,5,1,2]
        # gas-cost: [-2,-2,-2,3,3]


        # gas-cost:[-1，-1，1]

        total = 0
        min_total = 0
        start = 0
        for i in range(len(cost)):
            total += gas[i]-cost[i]
            if total < min_total:
                min_total = total
                start = i + 1
        
        if total < 0:
            return -1
        return start