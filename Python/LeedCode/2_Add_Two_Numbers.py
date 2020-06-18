'''

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

'''

class Solution(object):

    def addTwoNumbers(self, l1, l2):

        p = head = ListNode(0)
        carryValue = 0

        while l1 or l2 :

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0         
            sum = val1 + val2 + carryValue
            carryValue = sum//10

            p.next = ListNode(sum%10)
            p = p.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
    
        if carryValue > 0:
            p.next = ListNode(1)

        return head.next

'''
知识点:

Python中除号用/表示，但是和C语言不同的是/得到的值总是浮点数，例如：5 / 5结果是1.0。
Python中整除用//表示是，//表示两数相除，向下取整，例如8 // 5 结果是1。
'''
