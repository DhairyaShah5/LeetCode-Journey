class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is "0", the result is "0"
        if "0" in [num1, num2]:
            return "0"

        # Initialize result array to store intermediate sums
        result = [0] * (len(num1) + len(num2))
        num1Reversed, num2Reversed = num1[::-1], num2[::-1]

        # Multiply each digit and add the result to the correct position
        for i in range(len(num1Reversed)):
            for j in range(len(num2Reversed)):
                digitProduct = int(num1Reversed[i]) * int(num2Reversed[j])
                result[i + j] += digitProduct
                # Handle carry over
                result[i + j + 1] += result[i + j] // 10
                result[i + j] = result[i + j] % 10

        # Reverse the result list back to the correct order
        result = result[::-1]

        # Skip any leading zeros
        startIndex = 0
        while startIndex < len(result) and result[startIndex] == 0:
            startIndex += 1

        # Convert list of digits to string
        resultStr = map(str, result[startIndex:])
        return "".join(resultStr)