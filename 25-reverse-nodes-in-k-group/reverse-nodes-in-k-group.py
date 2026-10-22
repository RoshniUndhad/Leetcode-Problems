class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            kth = prev

            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            group_next = kth.next

            curr = prev.next
            prev_group = group_next

            while curr != group_next:
                temp = curr.next
                curr.next = prev_group
                prev_group = curr
                curr = temp

            temp = prev.next
            prev.next = kth
            prev = temp