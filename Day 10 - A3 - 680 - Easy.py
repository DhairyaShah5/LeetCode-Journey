class Solution:
    def validPalindrome(self, s: str) -> bool:
        sNew = "".join(char for char in s if char.isalnum()).lower()

        left, right = 0, len(sNew) - 1
        counter = 0

        while left < right:
            if sNew[left] == sNew[right]:
                left += 1
                right -= 1
            else:
                counter += 1
                isLeftPalindrome = sNew[left + 1:right + 1] == sNew[left + 1:right + 1][::-1]
                isRightPalindrome = sNew[left:right] == sNew[left:right][::-1]

                if isLeftPalindrome:
                    left += 1  
                elif isRightPalindrome:
                    right -= 1
                else:
                    counter += 1
                    break
        if counter <= 1:
            return True

        return False