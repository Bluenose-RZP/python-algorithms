'''Given head, the head of a linked list, determine if the linked list has
a cycle in it.

There is a cycle in a linked list if there is some node that can be reached again
by continuously following the next pointer.

Return true if there is a cycle in the linked list. Otherwise, return false.
the number of nodes is in range[0.10**4]
-10**5 <= node.val <= 10**5
cycle is either does not exist, or repeats to a valid list index.


THOUGHTS-- I was brainstorming a number of different ways, from a simple counter
(impractical) to destroying or modifying the list(easy but definitely not ideal)
Then I asked a syntax question to an ai regarding it and it spoiled the concept
behind Floyd's Algorithm. Even just the idea of two counters at different
speeds makes the solution obvious. I'll implement it now. Shame i didn't get
to see if I could recreate it myself.
'''

class ListNode:
    def _init_(self, x):
        self.val = x
        self.next = None

'''
This version worked, was simple and clean, but still wasn't quite optimal

def hasCycle(head:[ListNode]) -> bool:
    fast = slow = head
    while fast:
        fast = fast.next
        fast = fast.next if fast else None
        slow = slow.next
        if slow == fast and slow:
            return True
    return False
'''
'''
I move the fast.next check to the while loop so I can iterate fast in a single
jump. I also shift the edge case of a small list check to the front instead of
integrating into the loop checks.
This second version sped up the runtime.
'''
def hasCycle(head:[ListNode]) -> bool:
    if not head or not head.next:
        return False
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False
