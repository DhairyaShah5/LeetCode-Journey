class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helperFunction(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            result = helperFunction(x * x, n // 2)
            return x * result if n % 2 else result

        result = helperFunction(x, abs(n))
        return result if n >= 0 else 1 / result