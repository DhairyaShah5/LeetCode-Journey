class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray = []
        suffixArray = []
        answerArray = []

        currentProduct = 1
        for num in nums:
            currentProduct *= num
            prefixArray.append(currentProduct)
            
        currentProduct = 1
        for num in reversed(nums):
            currentProduct *= num
            suffixArray.append(currentProduct)

        suffixArray = list(reversed(suffixArray))

        for i in range(len(nums)):
            left = prefixArray[i - 1] if i > 0 else 1
            right = suffixArray[i + 1] if i < len(nums) -1 else 1
            answerArray.append(left * right)

        return answerArray