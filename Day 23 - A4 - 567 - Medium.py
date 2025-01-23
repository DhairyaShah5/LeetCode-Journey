class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freqCounter1, freqCounter2 = Counter(s1), Counter(s2[0:len(s1)])

        if freqCounter1 == freqCounter2:
            return True

        left, right = 0, len(s1)

        while right < len(s2):
            freqCounter2[s2[left]] -= 1
            freqCounter2[s2[right]] += 1

            if freqCounter1 == freqCounter2:
                return True
            
            left += 1
            right += 1

        return False