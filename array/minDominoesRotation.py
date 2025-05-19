'''

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

 

Example 1:


Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.

'''

def minDominoRotation(tops, bottoms):
    def count_rotations(target):
        top_rotations = 0
        bottom_rotations = 0
        for i in range(len(tops)):
            if tops[i] != target and bottoms[i] != target:
                return float('inf')  # Not possible for this target
            elif tops[i] != target:
                top_rotations += 1  # Rotate top to make it target
            elif bottoms[i] != target:
                bottom_rotations += 1  # Rotate bottom to make it target
        return min(top_rotations, bottom_rotations)

    # Check rotations for tops[0] and bottoms[0]
    rotations_top = count_rotations(tops[0])
    rotations_bottom = count_rotations(bottoms[0])

    # Get the minimum rotations of the two candidates
    result = min(rotations_top, rotations_bottom)
    return result if result != float('inf') else -1