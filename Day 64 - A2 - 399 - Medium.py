class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)  # Maps variable to a list of (neighbor, value)
        
        # Build the graph from given equations
        for index, (numerator, denominator) in enumerate(equations):
            value = values[index]
            graph[numerator].append((denominator, value))
            graph[denominator].append((numerator, 1 / value))

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            
            queue = deque([(start, 1.0)])  # (current node, accumulated product)
            visited = set([start])

            while queue:
                current_node, current_product = queue.popleft()
                
                if current_node == end:
                    return current_product
                
                for neighbor, weight in graph[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, current_product * weight))
                        visited.add(neighbor)
            
            return -1.0  # No valid path found

        # Process each query using BFS
        return [bfs(start, end) for start, end in queries]