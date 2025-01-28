class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        result = 0

        while left <= right:
            mid = left + ((right - left) // 2)
            
            if target == nums[mid]:
                result = nums[mid]
                return nums.index(result)
                break
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1 
                
        else:
            return -1