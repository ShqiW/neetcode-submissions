class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)
        
        def backtrack():
            # 终止条件：路径长度等于数组长度
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            # 遍历所有元素
            for i in range(len(nums)):
                # 剪枝：如果当前元素已被使用，跳过
                if used[i]:
                    continue
                
                # 做选择
                path.append(nums[i])
                used[i] = True
                
                # 递归
                backtrack()
                
                # 撤销选择
                path.pop()
                used[i] = False
        
        backtrack()
        return res