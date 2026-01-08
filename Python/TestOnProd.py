"""
Problem: Add Two Numbers Represented by Linked Lists. Given two linked lists representing non-negative integers, return their sum as a linked list.
https://www.geeksforgeeks.org/problems/test-on-prod--120504/1?page=1&sortBy=latest

Time Complexity: O(n + m)
Space Complexity: O(1) auxiliary space

Approach:
1. Reverse both input lists
2. Add digit by digit with carry handling
3. Build result by adding nodes to front (avoids final reversal)
4. Remove leading zeros from result
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def addTwoLists(self, head1, head2):
        # Handle edge cases
        if head1 is None and head2 is None:
            return Node(0)
        if head1 is None:
            return self.removeLeadingZeros(head2)
        if head2 is None:
            return self.removeLeadingZeros(head1)

        # Reverse both lists
        head1 = self.reverseLinkedList(head1)
        head2 = self.reverseLinkedList(head2)

        # Initialize variables
        carry = 0
        result = None

        # Addition loop
        while head1 is not None or head2 is not None or carry != 0:
            val1 = head1.data if head1 is not None else 0
            val2 = head2.data if head2 is not None else 0

            sum_val = val1 + val2 + carry
            digit = sum_val % 10
            carry = sum_val // 10

            # Create new node and add to front
            new_node = Node(digit)
            new_node.next = result
            result = new_node

            # Move pointers
            if head1 is not None:
                head1 = head1.next
            if head2 is not None:
                head2 = head2.next

        # Remove leading zeros
        return self.removeLeadingZeros(result)

    def reverseLinkedList(self, head):
        before = None
        current = head

        while current is not None:
            after = current.next
            current.next = before
            before = current
            current = after

        return before

    def removeLeadingZeros(self, head):
        while head is not None and head.data == 0 and head.next is not None:
            head = head.next
        return head
