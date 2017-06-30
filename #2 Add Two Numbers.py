# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l_head = ListNode(l1.val + l2.val)
        l_sum = l_head
        while l1.next != None and l2.next != None:
            if l_sum.val >= 10:
                l_sum.val = l_sum.val - 10
                l1 = l1.next
                l2 = l2.next
                l_tmp = ListNode(l1.val + l2.val + 1)
                l_sum.next = l_tmp
                l_sum = l_sum.next
            else:
                l1 = l1.next
                l2 = l2.next
                l_tmp = ListNode(l1.val + l2.val)
                l_sum.next = l_tmp
                l_sum = l_sum.next
        while l1.next != None:
            if l_sum.val >= 10:
                l_sum.val = l_sum.val - 10
                l1 = l1.next
                l_tmp = ListNode(l1.val + 1)
                l_sum.next = l_tmp
                l_sum = l_sum.next
            else:
                l_sum.next = l1.next
                break
        while l2.next != None:
            if l_sum.val >= 10:
                l_sum.val = l_sum.val - 10
                l2 = l2.next
                l_tmp = ListNode(l2.val + 1)
                l_sum.next = l_tmp
                l_sum = l_sum.next
            else:
                l_sum.next = l2.next
                break
        if l_sum.val >= 10:
            l_tmp = ListNode(1)
            l_sum.val = l_sum.val - 10
            l_sum.next = l_tmp
        return l_head
