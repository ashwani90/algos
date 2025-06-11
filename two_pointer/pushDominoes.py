'''

There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

 

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

'''

def pushDominoes(dominoes):
    n = len(dominoes)
    forces = [0] * n

    # Simulate rightward forces
    force = 0
    for i in range(n):
        if dominoes[i] == 'R':
            force = n  # Assign a large force
        elif dominoes[i] == 'L':
            force = 0  # No rightward force
        else:
            force = max(force - 1, 0)  # Decay the force
        forces[i] += force

    # Simulate leftward forces
    force = 0
    for i in range(n - 1, -1, -1):
        if dominoes[i] == 'L':
            force = n  # Assign a large force
        elif dominoes[i] == 'R':
            force = 0  # No leftward force
        else:
            force = max(force - 1, 0)  # Decay the force
        forces[i] -= force

    # Determine final state
    result = []
    for f in forces:
        if f > 0:
            result.append('R')
        elif f < 0:
            result.append('L')
        else:
            result.append('.')

    return ''.join(result)


def pushDominoesw(dominoes):
    res = ""
    for i, j in enumerate(dominoes):
        if (j != "."):
            res += j
        else:
            if i == len(dominoes)-1:
                if dominoes[i-1] == 'R':
                    res += 'R'
                else:
                    res += j
                break

            if (dominoes[i+1] == 'L' and dominoes[i-1] == 'R'):
                res += j
            elif dominoes[i+1] == 'L':
                res += 'L'
            elif dominoes[i-1] == 'R':
                res += 'R'
            else:
                res += j
    
    return res
