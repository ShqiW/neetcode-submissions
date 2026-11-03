class Solution:
    def kClosest(self, points, k):
        # Lambda 函数：计算点到原点的欧氏距离的平方
        # 不需要开方，因为只比较大小关系
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2
        
        # partition 函数：类似快排的分区操作
        # 将数组分成两部分：左边 <= pivot，右边 > pivot
        def partition(l, r):
            # 选择最右边的点作为 pivot
            pivotIdx = r
            pivotDist = euclidean(points[pivotIdx])
            
            # i 是"小于等于 pivot"区域的右边界
            i = l
            
            # 遍历 [l, r) 范围内的所有点
            for j in range(l, r):
                # 如果当前点距离 <= pivot 距离
                if euclidean(points[j]) <= pivotDist:
                    # 交换到"小于等于区域"
                    points[i], points[j] = points[j], points[i]
                    i += 1  # 扩大"小于等于区域"
            
            # 将 pivot 放到正确位置（i 的位置）
            # 此时 [l, i) 都 <= pivot，(i, r] 都 > pivot
            points[i], points[r] = points[r], points[i]
            
            # 返回 pivot 最终的索引位置
            return i
        
        # 搜索范围：整个数组
        L, R = 0, len(points) - 1
        
        # pivot 初始化为一个不可能的值
        pivot = len(points)
        
        # 当 pivot 不等于 k 时，继续缩小搜索范围
        while pivot != k:
            # 进行一次分区，返回 pivot 的最终位置
            pivot = partition(L, R)
            
            # 如果 pivot 在第 k 个位置的左边
            # 说明第 k 小的元素在右半部分
            if pivot < k:
                L = pivot + 1  # 在右半部分继续找
            # 如果 pivot 在第 k 个位置的右边
            # 说明第 k 小的元素在左半部分
            else:
                R = pivot - 1  # 在左半部分继续找
        
        # 当 pivot == k 时，前 k 个元素就是最近的 k 个点
        # 注意：这 k 个点内部不一定有序，但都比后面的点近
        return points[:k]