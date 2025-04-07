'''

There is an undirected weighted graph with n vertices labeled from 0 to n - 1.

You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.

A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.

The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the bitwise AND operator.

You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending at vertex ti. If there exists no such walk, the answer is -1.

Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.

 

Example 1:

Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]

Output: [1,-1]

Explanation:
'''

def find_all_recipes(recipes, ingredients, supplies):
    can_cook = {s:True for s in supplies}
    recipe_index = {r:i for i,r in enumerate(recipes)}

    def dfs(r):
        if r in can_cook:
            return can_cook[r]

        if r not in recipe_index:
            return False
        
        can_cook[r] = False

        for nei in ingredients[recipe_index[r]]:
            if not dfs(nei):
                return False
        
        can_cook[r] = True
        return can_cook[r]
    
    return [ r for r in recipes if dfs(r) ]