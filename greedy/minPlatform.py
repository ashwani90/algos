"""

minimum platforms based on arrivals and departures

"""

def minPlatforms(arr, deps):
    arr.sort()
    deps.sort()
    platforms = 0
    min_platforms = 0
    i = j = 0
    for i in range(len(arr)):
        if arr[i] <= deps[j]:
            platforms += 1
            min_platforms = max(min_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
    
    return min_platforms