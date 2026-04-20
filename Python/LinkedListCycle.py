"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer. Internally, pos is used
to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

https://leetcode.com/problems/linked-list-cycle/description/
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Floyd's Cycle Detection Algorithm (Tortoise and Hare)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None or head.next is None:
            return False

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Alternative: More concise version (without initial check)
class SolutionConcise:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Test helper function to create a linked list with cycle
def create_linked_list_with_cycle(values, pos):
    """
    Creates a linked list with a cycle at position pos
    values: list of node values
    pos: index where tail connects (-1 for no cycle)
    """
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    nodes = [head]

    # Create the linked list
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        nodes.append(current)

    # Create cycle if pos is valid
    if pos >= 0 and pos < len(nodes):
        current.next = nodes[pos]

    return head


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: [3,2,0,-4], pos = 1
    head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    print(f"Test 1: {solution.hasCycle(head1)}")  # Expected: True

    # Test case 2: [1,2], pos = 0
    head2 = create_linked_list_with_cycle([1, 2], 0)
    print(f"Test 2: {solution.hasCycle(head2)}")  # Expected: True

    # Test case 3: [1], pos = -1
    head3 = create_linked_list_with_cycle([1], -1)
    print(f"Test 3: {solution.hasCycle(head3)}")  # Expected: False

    # Test case 4: Empty list
    head4 = None
    print(f"Test 4: {solution.hasCycle(head4)}")  # Expected: False
