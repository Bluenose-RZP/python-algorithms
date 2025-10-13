'''Given a linked list starting at head, remove the link n nodes from the tail of the list
with 1 <= n <= list length.  n=1 would remove the tail
'''
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

'''
This one was tricky for syntax and testing, but most of the logic was straightforward.
The hardest part was edge cases where n was the list length or the list was empty.
I fixed those with a small boolean tree, but it would be more efficient and
simpler to use a dummy head for the list to start my count.
'''
def removeNthFromEnd(head: [ListNode],
                         n: int) -> [ListNode]:
     
     node = head
     nodeR = head
     for i in range(n + 1):
          if node:
               node = node.next
          else:
               if head.next:
                    return head.next
               else:
                    return None
     while node:
          node = node.next
          nodeR = nodeR.next
     nodeR.next = nodeR.next.next if nodeR.next.next else None
     return head

#create example list
example1 = ListNode(1)
node = example1
for i in range(5):
     node.next = ListNode(i+2)
     node = node.next
node = example1
'''while node:
     print(node.val)
     node = node.next
'''
#test section
example1 = removeNthFromEnd(example1, 6)
node = example1
while node:
     print(node.val)
     node = node.next
