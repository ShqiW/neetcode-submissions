class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 找到所有石头中的最大重量
        maxStone = max(stones)
        
        # 创建桶数组，索引表示重量，值表示该重量的石头数量
        # bucket[i] = 重量为 i 的石头有几个
        bucket = [0] * (maxStone + 1)
        
        # 统计每个重量的石头数量（频率计数）
        for stone in stones:
            bucket[stone] += 1
        
        # first: 当前考虑的最重石头的重量
        # second: 次重石头的重量
        # 初始都指向最大重量
        first = second = maxStone
        
        # 持续处理直到没有石头剩余（first == 0）
        while first > 0:
            # 如果当前重量的石头数量是偶数
            # 它们会两两抵消，跳过这个重量
            if bucket[first] % 2 == 0:
                first -= 1  # 移动到下一个更轻的重量
                continue
            
            # 当前重量石头数量是奇数，需要找次重的石头来碰撞
            # 从 first-1 和 second 中取较小值开始找
            # （second 是上次找到的次重石头位置，可能已经更轻了）
            j = min(first - 1, second)
            
            # 向下扫描找到第一个非零的重量（有石头存在的重量）
            while j > 0 and bucket[j] == 0:
                j -= 1
            
            # 如果找不到其他石头（j == 0），说明只剩当前这个石头
            if j == 0:
                return first
            
            # 更新 second 为找到的次重石头重量
            second = j
            
            # 进行碰撞：各减少一个石头
            bucket[first] -= 1
            bucket[second] -= 1
            
            # 产生差值石头（如果 first == second 则差值为 0，不会产生新石头）
            bucket[first - second] += 1
            
            # 更新 first 指针到可能还有石头的较重位置
            # 新产生的石头重量是 first - second
            # second 位置可能还有剩余石头
            # 取两者较大值继续处理
            first = max(first - second, second)
        
        # 所有石头都抵消了，返回 0
        return first
