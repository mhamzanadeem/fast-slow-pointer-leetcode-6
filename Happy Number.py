class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x: int) -> int:
            total = 0
            while x:
                x, digit = divmod(x, 10)
                total += digit * digit
            return total

        # A number is happy iff it reaches 1; otherwise it falls into a cycle
        # of unhappy numbers. Treat numbers as a "linked list" and use Floyd.
        slow = fast = n
        while True:
            slow = next_num(slow)
            fast = next_num(next_num(fast))
            if fast == 1:
                return True
            if slow == fast:
                return False
