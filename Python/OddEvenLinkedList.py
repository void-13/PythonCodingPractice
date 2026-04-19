"""
Given the head of a singly linked list, group all the nodes with odd indices
together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain
as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

https://leetcode.com/problems/odd-even-linked-list/description/?envType=study-plan-v2&envId=leetcode-75
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_head = even

        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head


# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values"""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Convert linked list to Python list for easy verification"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.oddEvenList(head1)
    print(f"Example 1: {linked_list_to_list(result1)}")  # [1, 3, 5, 2, 4]

    # Example 2
    head2 = create_linked_list([2, 1, 3, 5, 6, 4, 7])
    result2 = solution.oddEvenList(head2)
    print(f"Example 2: {linked_list_to_list(result2)}")  # [2, 3, 6, 7, 1, 5, 4]

    # Edge case: empty list
    head3 = create_linked_list([])
    result3 = solution.oddEvenList(head3)
    print(f"Edge case (empty): {linked_list_to_list(result3)}")  # []

    # Edge case: single node
    head4 = create_linked_list([1])
    result4 = solution.oddEvenList(head4)
    print(f"Edge case (single): {linked_list_to_list(result4)}")  # [1]

    # Edge case: two nodes
    head5 = create_linked_list([1, 2])
    result5 = solution.oddEvenList(head5)
    print(f"Edge case (two nodes): {linked_list_to_list(result5)}")  # [1, 2]
