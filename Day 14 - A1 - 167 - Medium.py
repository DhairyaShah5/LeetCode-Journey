class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]
        
            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                return [left + 1, right + 1]
            
        return []

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             x = target - numbers[i]
#             for y in range(i+1, len(numbers)):
#                 if numbers[y] == x:
#                     return i+1,y+1