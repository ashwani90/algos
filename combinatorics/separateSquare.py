"""

You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

Answers within 10-5 of the actual answer will be accepted.

Note: Squares may overlap. Overlapping areas should be counted multiple times.
"""

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def helper(line: float, squares: List[List[int]]) -> float:
            aAbove = 0.0
            aBelow = 0.0
            for sq in squares:
                x, y, l = sq
                total = l * l
                if line <= y:
                    aAbove += total
                elif line >= y + l:
                    aBelow += total
                else:
                    # The line intersects the square.
                    aboveHeight = (y + l) - line
                    belowHeight = line - y
                    aAbove += l * aboveHeight
                    aBelow += l * belowHeight
            return aAbove - aBelow

        lo = 0
        hi = 2*1e9
        for sq in squares:
            y, l = sq[1], sq[2]
            lo = min(lo, float(y))
            hi = max(hi, float(y) + l)
        
        for _ in range(60):
            mid = (lo + hi) / 2.0
            diff = helper(mid, squares)
            

            if diff > 0:
                lo = mid
            else:
                hi = mid
        
        return hi