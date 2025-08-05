"""
Problem: Pick k cards from the front or end of the array to maximize the total points.
"""

def max_score(cardPoints, k):
    total = sum(cardPoints[:k])
    max_score = total
    for i in range(1, k + 1):
        total += cardPoints[-i] - cardPoints[k - i]
        max_score = max(max_score, total)
    return max_score