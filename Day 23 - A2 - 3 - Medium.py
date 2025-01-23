class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        curSubString = ""
        maxSubString = ""

        for right in range(len(s)):
            if s[right] in curSubString:
                left = curSubString.index(s[right]) + 1
                curSubString = curSubString[left:right]

            curSubString += s[right]

            if len(curSubString) > len(maxSubString):
                maxSubString = curSubString

        return len(maxSubString)