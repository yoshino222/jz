# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
# 示例1：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 限制：
#
# 0 <= 链表长度 <= 1000
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre1=l1
        pre2=l2
        while l1:
            if pre2.val>=l1.val:
                pre=pre.next
            else:
                pre1.next=l2
                pre1=pre1.next
        #2
        cur=tmp=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
            return cur
        cur.next=l1 if l1 else l2






