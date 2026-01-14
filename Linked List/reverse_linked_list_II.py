#Given the head of a singly linked list and two integers left and right where left <= right,
#reverse the nodes of the list from position left to position right, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self,head:ListNode, left:int, right:int)->ListNode:
        if not head or left==right:
            return head

        # create a dummy node to ensure we have a node before reversal incase left = 1
        # we return dummy.next, so value of dummy node doesn't matter
        dummy = ListNode(0) 
        dummy.next = head
        prev = dummy

        # move prev to node before left
        for _ in range(left-1):
            prev = prev.next

        # reverse between left and right
        curr = prev.next
        for _ in range(right-left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
    
            
