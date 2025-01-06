class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_array = []

        currentSum = 0
        for num in nums:
            currentSum += num
            self.prefix_array.append(currentSum)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix_array[right]
        leftSum = self.prefix_array[left - 1] if left > 0 else 0
        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)