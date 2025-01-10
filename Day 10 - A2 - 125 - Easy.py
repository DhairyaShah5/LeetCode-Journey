class Solution:
    def isPalindrome(self, s: str) -> bool:
        sNew = "".join(char for char in s if char.isalnum()).lower()

        sNew2 = sNew[::-1]

        if sNew == sNew2:
            return True
        else:
            return False

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         sNew = "".join(char for char in s if char.isalnum()).lower()

#         left, right = 0, len(sNew) - 1

#         while left <= right:
#             if sNew[left] == sNew[right]:
#                 left += 1
#                 right -= 1
#             else:
#                 return False
                
#         return True