'''
Example 3: Stock Span Problem
Problem:
Given an array prices representing stock prices, find the span of each stock’s price. The span is defined as the number of consecutive days (before the current day) where the price was less than or equal to the current price.

Steps:
Use a monotonic decreasing stack (elements in the stack are in decreasing order).

Iterate through the array:

While the stack is not empty and the current price is greater than or equal to the price at the top of the stack, pop from the stack.

Calculate the span as the difference between the current index and the index at the top of the stack.

Push the current index onto the stack.

'''

def stockSpan(prices):
    n = len(prices)
    spans = [1] * n
    stack = []
    
    for i in range(n):
        while stack and prices[i] >= prices[stack[-1]]:
            stack.pop()
        spans[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    
    return spans