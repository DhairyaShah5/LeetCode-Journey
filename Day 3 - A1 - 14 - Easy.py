class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start by assuming the first string is the common prefix
        prefix = strs[0]

        # Compare this prefix with each string in the list
        for s in strs[1:]:
            # Reduce the prefix until it matches the current string
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         separate_list = []
#         for s in strs:
#             separate_list.append(list(s))

#         longest_common_prefix = []
#         n = 0

#         while True:
#             try:
#                 current_characters = [new_list[n] for new_list in separate_list]
#                 if len(set(current_characters)) == 1:
#                     longest_common_prefix.append(current_characters[0])
#                 else:
#                     break
#                 n += 1

#             except IndexError:
#                 break

#         return ''.join(longest_common_prefix)