class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}

        for substrings in strs:
            sorted_substrings = ''.join(sorted(substrings))

            if sorted_substrings in grouped_anagrams:
                grouped_anagrams[sorted_substrings].append(substrings)
            else:
                grouped_anagrams[sorted_substrings] = [substrings]

        return list(grouped_anagrams.values())
