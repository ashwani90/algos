"""
Calculate nPr


"""

def factorial(n):
    return 1 if n == 0 else n*factorial(n-1)

def nPr(n,r):
    return factorial(n)//factorial(n-r)

