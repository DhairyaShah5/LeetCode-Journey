class Solution:
    def reverse(self, x: int) -> int:
        intMax = 2**31 - 1  # 2147483647
        intMin = -2**31     # -2147483648

        sign = -1 if x < 0 else 1
        xAbs = abs(x)
        rev = 0

        while xAbs != 0:
            digit = xAbs % 10
            xAbs //= 10

            # Check for overflow before actually adding the digit
            if rev > (intMax - digit) // 10:
                return 0

            rev = rev * 10 + digit

        return sign * rev