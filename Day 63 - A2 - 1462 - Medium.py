class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjacencyList = defaultdict(list)
        for prerequisite, course in prerequisites:
            adjacencyList[course].append(prerequisite)

        def dfs(course):
            if course not in prerequisiteMap:
                prerequisiteMap[course] = set()
                for prerequisite in adjacencyList[course]:
                    prerequisiteMap[course] = prerequisiteMap[course] | dfs(prerequisite) # Union of Hash sets
                prerequisiteMap[course].add(course)
            return prerequisiteMap[course]
        
        prerequisiteMap = {} # Map course -> Hashset of indirect prerequisites
        for course in range(numCourses):
            dfs(course)
        
        result = []
        for prerequisite, course in queries:
            result.append(prerequisite in prerequisiteMap[course])
        return result