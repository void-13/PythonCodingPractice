# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=problem-list-v2&envId=two-pointers


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    #   Time Complexity: O(n)
    #   Space Complexity: O(1)
    slow = head
    fast = head

    for i in range(n):
        fast = fast.next

    if fast is None:
        return head.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return head
