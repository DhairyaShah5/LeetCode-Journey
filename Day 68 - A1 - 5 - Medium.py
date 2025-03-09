class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.result = ""
        self.resultLength = 0

        for i in range(len(s)):
            # Checking for Odd Length Palindrome
            self.checkPalindrome(s, i, i)

            # Checking for Even Length Palindrome
            self.checkPalindrome(s, i, i + 1)
  
        return self.result

    def checkPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > self.resultLength:
                self.result = s[left: right + 1]
                self.resultLength = right - left + 1
            left -= 1
            right += 1