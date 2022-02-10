#18. 删除链表的节点 （四种方法）
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#方法1 单指针
def onep(head,val):
    if not head:#空链表
        return head
    if head.val==val:#删除头结点
        return  head.next
    pre=head#指针指向头结点
    while head and head.val!=val:#不是要删除的数字时
        pre=pre.next#向后移动
    if pre.next:#当遇到删除位置 弹出循环，
        pre.next=pre.next.next
    return head
#方法2 双指针
def twop(head,val):
    if not head:
        return head
    if head.val==val:
        return head.next
    pre,cur=head,head
    while cur and cur.val!=val:
        pre,cur=cur,cur.next
    if cur:
        pre.next=cur.next
    return head

