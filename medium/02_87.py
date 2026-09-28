class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        i = dummy

        while i.next and i.next.next:
            if i.next.val == i.next.next.val:
                val = i.next.val

                while i.next and i.next.val == val:
                    i.next = i.next.next
            else:
                i = i.next
        return dummy.next

