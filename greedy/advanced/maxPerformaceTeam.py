"""
Max performance of a team

Select at most k engineers with speed and efficiency, and maximize performance = sum(speed) * min(efficiency).
"""

def max_performance(n, speed, efficiency, k):
    engineers = sorted(zip(efficiency, speed), reverse=True)
    heap = []
    total_speed = result = 0
    for e,s in engineers:
        heapq.heappush(heap, s)
        total_speed += s
        if len(heap) > k:
            heapq.heappop()
        result = max(result, total_speed*e)
    
    return result%(10**9+7)

