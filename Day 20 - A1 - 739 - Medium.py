class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resultArray = [0] * len(temperatures)
        stack = []

        for index,temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                resultArray[stackIndex] = index - stackIndex
            stack.append((temperature, index))
        return resultArray