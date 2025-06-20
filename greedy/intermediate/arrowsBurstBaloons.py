"""

Arrows to burst baloons

"""


def minArrows(points):
    points.sort(key lambda x: x[1])
    arrows = 0
    last_finish = float('-inf')
    for start, finish in points:
        if start > last_finish:
            arrows += 1
            last_finish = finish
    
    return arrows
