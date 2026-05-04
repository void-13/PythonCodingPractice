# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Basic edge cases
        if not head or not head.next or k == 0:
            return head

        # 1. Calculate length and find the tail
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1

        # 2. Connect tail to head to create a circle
        tail.next = head

        # 3. Handle k > length
        k = k % length

        # 4. Find the new tail (length - k steps from the old tail)
        steps_to_new_tail = length - k
        temp = tail # Starting from tail like in your Java code

        while steps_to_new_tail > 0:
            temp = temp.next
            steps_to_new_tail -= 1

        # 5. Set new head and break the circle
        new_head = temp.next
        temp.next = None

        return new_head
