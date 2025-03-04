class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adjacencyList = [[] for _ in range (numCourses)]
        for course, prerequisite in prerequisites:
            indegree[prerequisite] += 1
            adjacencyList[course].append(prerequisite)

        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completedCourses, courseOrder = 0, []
        while queue:
            currentCourse = queue.popleft()
            courseOrder.append(currentCourse)
            completedCourses += 1

            for dependentCourse in adjacencyList[currentCourse]:
                indegree[dependentCourse] -= 1
                if indegree[dependentCourse] == 0:
                    queue.append(dependentCourse)

        if completedCourses != numCourses:
            return []

        return courseOrder[::-1]