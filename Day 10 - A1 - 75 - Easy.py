class Solution:

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(i, j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
        
        leftPointer = 0
        rightPointer = (len(s) - 1)

        for i in range(len(s)//2):
            swap(leftPointer, rightPointer)
            leftPointer += 1
            rightPointer -= 1
        return s