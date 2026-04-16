"""
Given a singly linked list, we have to check whether it is a palindrome or not.
https://www.geeksforgeeks.org/dsa/function-to-check-if-a-singly-linked-list-is-palindrome/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class PalindromeLinkedList:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None or head.next is None:
            return True

        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev = None
        curr = slow.next
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Compare first half with reversed second half
        while prev is not None:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True


# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to print linked list
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))


# Test cases
if __name__ == "__main__":
    solution = PalindromeLinkedList()

    # Test case 1: [1, 2, 2, 1] - Palindrome
    head1 = create_linked_list([1, 2, 2, 1])
    print("List 1:", end=" ")
    print_linked_list(head1)
    print(f"Is Palindrome: {solution.isPalindrome(head1)}")  # True
    print()

    # Test case 2: [1, 2, 3, 2, 1] - Palindrome (odd length)
    head2 = create_linked_list([1, 2, 3, 2, 1])
    print("List 2:", end=" ")
    print_linked_list(head2)
    print(f"Is Palindrome: {solution.isPalindrome(head2)}")  # True
    print()

    # Test case 3: [1, 2, 3, 4] - Not a palindrome
    head3 = create_linked_list([1, 2, 3, 4])
    print("List 3:", end=" ")
    print_linked_list(head3)
    print(f"Is Palindrome: {solution.isPalindrome(head3)}")  # False
    print()

    # Test case 4: [1] - Single node (palindrome)
    head4 = create_linked_list([1])
    print("List 4:", end=" ")
    print_linked_list(head4)
    print(f"Is Palindrome: {solution.isPalindrome(head4)}")  # True
    print()

    # Test case 5: [1, 2] - Not a palindrome
    head5 = create_linked_list([1, 2])
    print("List 5:", end=" ")
    print_linked_list(head5)
    print(f"Is Palindrome: {solution.isPalindrome(head5)}")  # False
