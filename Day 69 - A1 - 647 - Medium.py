class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            # Checking for Odd Length Palindromes
            result += self.countPalindrome(s, i, i)
            # Checking for Even Length Palindromes
            result += self.countPalindrome(s, i, i + 1)
        
        return result
    
    def countPalindrome(self, s, left, right):
        result = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            left -= 1
            right +=1
            
        return result