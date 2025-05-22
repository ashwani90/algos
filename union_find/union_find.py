class UnionFind:
    def __init__(self, size):
        # Initialize parent and rank arrays
        self.parent = list(range(size))  # Initially, each element is its own parent
        self.rank = [1] * size  # All sets start with rank 1
    
    def find(self, x):
        # Path compression: Make each node point directly to the root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Recursively find the root
        return self.parent[x]
    
    def union(self, x, y):
        # Find the roots of the sets containing x and y
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:  # Only unite if they are in different sets
            # Union by rank: Attach the smaller tree to the larger tree
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                # If they are equal in rank, make one root the parent of the other
                self.parent[rootY] = rootX
                self.rank[rootX] += 1  # Increase the rank of the root

# Example usage
uf = UnionFind(5)  # 5 elements: {0, 1, 2, 3, 4}

# Union operations
uf.union(0, 1)  # Merge sets containing 0 and 1
uf.union(1, 2)  # Merge sets containing 1 and 2

# Find operations
print(uf.find(0))  # Output: 0 (Element 0 is in its own set, the root is 0)
print(uf.find(1))  # Output: 0 (Element 1 is now in the set containing 0)
print(uf.find(2))  # Output: 0 (Element 2 is now in the set containing 0)