from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        
        # 构建最大堆：存储每个任务的剩余次数（用负数表示，因为 Python 的 heapq 是最小堆）
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)  # 堆化
        
        time = 0
        
        # 冷却队列：存储正在冷却的任务
        # 每个元素是 [剩余次数, 可以再次执行的时间]
        # 例如：[-2, 5] 表示任务还剩 2 次，在时间 5 可以再次执行
        q = deque()
        
        # 只要还有任务（正在执行的或冷却中的），就继续循环
        while maxHeap or q:
            time += 1  # 时间前进一个周期
            
            # 情况 1：当前没有可执行的任务（都在冷却中）
            if not maxHeap:
                # 优化：直接跳到最早可用任务的时间，避免逐个周期空转
                time = q[0][1]
            else:
                # 情况 2：有可执行的任务
                # 从最大堆中取出剩余次数最多的任务（贪心策略）
                cnt = 1 + heapq.heappop(maxHeap)
                # 注意：heappop 返回负数，+1 表示执行一次
                # 例如：-3 + 1 = -2（执行一次后还剩 2 次）
                
                # 如果任务还有剩余次数（cnt != 0）
                if cnt:
                    # 将任务放入冷却队列
                    # time + n 表示该任务在 n 个周期后可以再次执行
                    q.append([cnt, time + n])
            
            # 检查冷却队列中是否有任务冷却完成
            # 如果队列不为空，且第一个任务的冷却时间到了
            if q and q[0][1] == time:
                # 将冷却完成的任务移回最大堆，使其可以再次执行
                heapq.heappush(maxHeap, q.popleft()[0])
        
        # 返回总共需要的 CPU 周期数
        return time