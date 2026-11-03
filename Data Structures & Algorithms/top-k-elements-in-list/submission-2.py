class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        sorted_freq = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
        
        # Step 3: Extract the top k elements
        top_k = [item[0] for item in sorted_freq[:k]]
        
        return top_k



        