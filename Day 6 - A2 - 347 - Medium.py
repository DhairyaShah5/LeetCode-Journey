class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
            
        sorted_dictionary = sorted(dictionary.items(), key = lambda item: item[1], reverse = True)

        top_k_elements_array = [x[0] for x in sorted_dictionary[:k]]

        return top_k_elements_array
