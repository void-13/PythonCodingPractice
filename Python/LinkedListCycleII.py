"""
Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the next pointer. Internally,
pos is used to denote the index of the node that tail's next pointer is
connected to (0-indexed). It is -1 if there is no cycle. Note that pos is
not passed as a parameter.

Do not modify the linked list.

https://leetcode.com/problems/linked-list-cycle-ii/description/
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None or head.next is None:
            return None

        slow = head
        fast = head

        # Phase 1: Detect if cycle exists
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # Cycle detected
            if slow == fast:
                # Phase 2: Find the start of the cycle
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        # No cycle found
        return None

