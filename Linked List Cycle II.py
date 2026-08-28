from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        # Step 1: detect a cycle with Floyd's algorithm.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            # No cycle found.
            return None

        # Step 2: reset one pointer to head, keep the other at the meeting point.
        # Move both one step at a time; they meet at the cycle's entry node.
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow
