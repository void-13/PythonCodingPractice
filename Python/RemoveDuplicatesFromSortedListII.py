class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class RemoveDuplicatesFromSortedListII:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        temp = ListNode(0, head)
        prev = temp
        curr = head

        while curr is not None:
            if curr.next is not None and curr.val == curr.next.val:
                while curr.next is not None and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return temp.next
