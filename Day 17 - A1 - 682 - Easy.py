class Solution:
    def calPoints(self, operations: List[str]) -> int:
        resultArray = []

        for i in range(len(operations)):
            if operations[i].lstrip('-').isdigit():
                resultArray.append(int(operations[i]))
                print(resultArray)
            elif operations[i] == 'C':
                resultArray.pop()
            elif operations[i] == 'D':
                resultArray.append(resultArray[-1]*2)
            elif operations[i] == '+':
                resultArray.append(resultArray[-1] + resultArray[-2])

        return sum(resultArray)