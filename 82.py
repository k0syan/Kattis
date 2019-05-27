class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(self, head: ListNode) -> ListNode:
    c = head
    p = head
    n = head.next
    print(c, p, n)
    while n is not None:
        c = n
        n = c.next