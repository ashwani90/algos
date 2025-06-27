Sure! Continuing with problem 10:

---

## 10. **Sort list of points based on their x-coordinate using bucket sort**

### Problem:

Given a list of points `(x, y)`, sort them based on their `x` values using bucket sort.

### Solution:

```python
def bucket_sort_points(points):
    n = len(points)
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    bucket_range = (max_x - min_x) / n + 1e-9
    buckets = [[] for _ in range(n)]

    for point in points:
        idx = int((point[0] - min_x) / bucket_range)
        if idx == n:
            idx = n - 1
        buckets[idx].append(point)

    # Sort each bucket by x (though all have similar x in bucket)
    for bucket in buckets:
        bucket.sort(key=lambda p: p[0])

    sorted_points = []
    for bucket in buckets:
        sorted_points.extend(bucket)
    return sorted_points

points = [(2,3), (1,5), (4,1), (3,8), (2,2), (5,0)]
print(bucket_sort_points(points))
```

### Explanation:

We distribute points into buckets based on their `x` coordinate, then sort each bucket. Since points are grouped by close `x`, sorting within buckets is efficient.

---

If you'd like, I can continue with more bucket sort problems or help with other sorting algorithms!
