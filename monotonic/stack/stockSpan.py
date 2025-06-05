"""

Stock span problem
Input is stock prices

"""

def stock_span(prices):
    stack = []
    span = [-1]*len(prices)

    for i in range(len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        span[i] = i - stack[-1] if stack else i+1
        stack.append(i)
    
    return span