class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    while current:
        after = current.next
        current.next = prev
        prev = current
        current = after
    return prev
