def create_linked_list(values):
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def linked_list_to_list(head):
    """Helper function to convert linked list to Python list"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Example 1: [1,3,4,7,1,2,6]
    head1 = create_linked_list([1, 3, 4, 7, 1, 2, 6])
    result1 = solution.deleteMiddle(head1)
    print(linked_list_to_list(result1))  # Output: [1, 3, 4, 1, 2, 6]

    # Example 2: [1,2,3,4]
    head2 = create_linked_list([1, 2, 3, 4])
    result2 = solution.deleteMiddle(head2)
    print(linked_list_to_list(result2))  # Output: [1, 2, 4]

    # Example 3: [2,1]
    head3 = create_linked_list([2, 1])
    result3 = solution.deleteMiddle(head3)
    print(linked_list_to_list(result3))  # Output: [2]