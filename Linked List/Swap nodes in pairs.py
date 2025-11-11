
class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(values):
    if not values:
        return None

    head = ListNode(values[0])
    curr = head
    for val in values[1: ]:
        curr.next = ListNode(val)
        curr = curr.next

    return head

def printLinkedList(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)


## Solution to swap every pair of nodes
    
def swapPairs(head:ListNode) -> ListNode:
    # edge case: list with 0 or 1 node
    if not head or not head.next:
        return head

    dummy = head.next
    prev = None
    while head and head.next:
        if prev:
            prev.next = head.next

        prev = head
        next_node = head.next.next
        head.next.next = head #reverse the pair
        head.next = next_node
        head = next_node
        
    return dummy


# Test case
head = createLinkedList([1,2,3,4,5,6])
printLinkedList(head)
result = swapPairs(head)
printLinkedList(result)






    
