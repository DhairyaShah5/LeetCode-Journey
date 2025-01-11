class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        resultArray = []

        while i < len(word1) and j < len(word2):
            resultArray.append(word1[i])
            resultArray.append(word2[j])
            i += 1
            j += 1

        resultArray.append(word1[i:])
        resultArray.append(word2[j:])
            
        return "".join(resultArray)