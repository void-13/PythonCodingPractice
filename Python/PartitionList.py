class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    less = less_tail = ListNode(0)
    geq = geq_tail = ListNode(0)
    temp = head

    while temp:
        if temp.val < x:
            less_tail.next = temp
            less_tail = less_tail.next
        else:
            geq_tail.next = temp
            geq_tail = geq_tail.next
        temp = temp.next

    geq_tail.next = None
    less_tail.next = geq.next
    return less.next
