class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjacencyList = [[] for _ in range (numCourses)]
        for course, prerequisite in prerequisites:
            indegree[prerequisite] += 1
            adjacencyList[course].append(prerequisite)

        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completedCourses = 0
        while queue:
            currentCourse = queue.popleft()
            completedCourses += 1

            for dependentCourse in adjacencyList[currentCourse]:
                indegree[dependentCourse] -= 1
                if indegree[dependentCourse] == 0:
                    queue.append(dependentCourse)

        return completedCourses == numCourses