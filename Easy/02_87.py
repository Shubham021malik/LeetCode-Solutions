class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        i = head
        while i and i.next:
            if i.val == i.next.val:
                i.next = i.next.next
            else:
                i = i.next
        return head
