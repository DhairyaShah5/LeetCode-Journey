class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        size = [1] * (len(edges) + 1)

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]

        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            if root1 == root2:
                return False  # Cycle detected
            
            # Union by size
            if size[root1] > size[root2]:
                parent[root2] = root1
                size[root1] += size[root2]
            else:
                parent[root1] = root2
                size[root2] += size[root1]
            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]  # Redundant edge that creates a cycle