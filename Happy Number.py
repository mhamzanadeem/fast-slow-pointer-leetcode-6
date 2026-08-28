class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1:

            if n in visited:
                return False

            visited.add(n)

            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit
                n = n // 10

            n = total

        return True