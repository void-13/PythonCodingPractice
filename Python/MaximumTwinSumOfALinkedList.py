"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.
Given the head of a linked list with even length, return the maximum twin sum of the linked list.

https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: ListNode) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None or head.next is None:
            return 0

        # Find the middle of the linked list
        slow = head
        fast = head.next.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        reverse_head = slow.next
        prev = None
        current = reverse_head
        slow.next = None

        while current is not None:
            after = current.next
            current.next = prev
            prev = current
            current = after

        reverse_head = prev

        # Calculate maximum twin sum
        max_sum = 0

        while head is not None and reverse_head is not None:
            sum_val = head.val + reverse_head.val
            max_sum = max(max_sum, sum_val)
            head = head.next
            reverse_head = reverse_head.next

        return max_sum