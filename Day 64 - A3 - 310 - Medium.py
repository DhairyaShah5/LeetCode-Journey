class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
            
        adjacencyList = defaultdict(list)

        # Build the adjacency list
        for nodeA, nodeB in edges:
            adjacencyList[nodeA].append(nodeB)
            adjacencyList[nodeB].append(nodeA)

        remainingEdges = {}  # Dictionary to track remaining edges for each node
        leafQueue = deque()  # Queue to store leaf nodes

        # Identify initial leaf nodes (nodes with only one connection)
        for node, neighbors in adjacencyList.items():
            remainingEdges[node] = len(neighbors)
            if len(neighbors) == 1:
                leafQueue.append(node)

        while leafQueue:
            if n <= 2:
                return list(leafQueue)

            for _ in range(len(leafQueue)):
                leaf = leafQueue.popleft()
                n -= 1
                for neighbor in adjacencyList[leaf]:
                    remainingEdges[neighbor] -= 1  # Decrease edge count
                    
                    if remainingEdges[neighbor] == 1:
                        leafQueue.append(neighbor)  # Add new leaf node
