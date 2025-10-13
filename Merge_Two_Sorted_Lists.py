'''Given the heads of two sorted linked lists list1 and list2:
Merge the two lists into one sorted list by splicing together the lists.
Return the head of the merged linked list.

example: input list1 = [1,2,4] list2 = [1,3,4]
Output = [1,1,2,3,4,4]

Constraints: The number of nodes in both lists is in range [0,50]
-100 <= Node.val <= 100
both list1 and list2 are sorted in non decreasing order.
'''

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
'''class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        
This was my first attempt, taking a bit of tweaking and bug catching.
it works correctly, but is inefficient for a number of reasons.
I don't need to loop in with or and continue after one of the lists has
run out, I can link directly to the next item in the remaining list and it
will have all of the remaining nodes linked to it. Also, the val arguments
are redundant.
        node1 = list1
        node2 = list2
        node3Head = ListNode(0) # startup node for new list
        node3 = node3Head
        val1 = node1.val if node1 else 101
        val2 = node2.val if node2 else 101
        while node1 or node2: # loop for both.
            if node1 and val1 <= val2:
                node3.next = ListNode(val1)
                node1 = node1.next
                val1 = node1.val if node1 else 101
            elif node2:
                node3.next = ListNode(val2)
                node2 = node2.next
                val2 = node2.val if node2 else 101
            node3 = node3.next
        return node3Head.next
            '''


'''This next solution is much more simple and efficient.
It's removed the extra processing for uneven list lengths and also removed
all of the unnecessary added variables.
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        
        nodeHead = ListNode(0)
        node = nodeHead
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next
            node = node.next
        node.next = list1 if list1 else list2
        return nodeHead.next
                
        
