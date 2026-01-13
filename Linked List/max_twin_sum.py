# Maximum Twin Sum of a Linked List asks for the max pairt sum.
# The pairs are the first and last node, second and second last node, third and third last node, etc.

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self,head: ListNode)->int:
        # find mid node of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the list
        prev = None
        curr = slow # mid node
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # compute twin sum
        max_sum = 0
        first = head
        second = prev # prev is head of the second half

        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum
    

# Build linked list
def build_linked_list(values):
    head = ListNode(values[0])
    cur = head
    for val in values[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head


def print_linked_list(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")

### Test Solution
head = build_linked_list([5, 9, 2, 4])
print_linked_list(head)

sol = Solution()
print(sol.pairSum(head))

# This solution to re-organize data to make expensive comparision cheaper
