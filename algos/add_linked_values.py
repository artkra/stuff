class ListNode():
    def __init__(self, x, next=None):
        self.x = x
        self.next = next

    def add_two(self, l1, l2):
        tmp = self
        dec = 0

        while l1.next or l2.next:
            print(l1.x, l2.x)

            dec = (l1.x + l2.x)//10

            tmp.x = (l1.x + l2.x)%10 + dec
            l1 = l1.next
            l2 = l2.next
            tmp.next = ListNode(0)
            tmp = tmp.next

        print(l1.x, l2.x)
        tmp.x = (l1.x + l2.x)%10 + dec

        dec = (l1.x + l2.x)//10 

        if dec > 0:
            tmp.next = ListNode(dec, None)
        else:
            tmp.next = None
        return self


def print_ln(ln):
    while ln.next:
        print(ln.x, '\t')
        ln = ln.next
    print(ln.x)

if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(4, ListNode(5, ListNode(6)))
    res = ListNode(0)
    res.add_two(l1, l2)
    print_ln(res)