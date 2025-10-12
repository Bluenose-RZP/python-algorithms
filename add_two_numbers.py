''' You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a
single digit. Add the two numbers and return the sum as a linked list. You may
assume the two numbers do not contain any leading zero, except the number 0 itself.

example: input l1 = [2,4,3], l2 = [5,6,4]
        output: [7,0,8]

Constraints: The number of nodes in eached linked list is in the range [1,100].
0 <= Node.val <= 9
The list numbers will not have any leading zeros.
'''
class ListNode(object):
    def _init_(self, val = 0, next = None):
        self.val = val
        self.next = next



def addTwoNumbers(self, l1, l2):
    node1 = l1
    node2 = l2
    nodeSum = node1.val + node2.val
    if nodeSum > 9:
        nodeRemain = True
        nodeSum = nodeSum%10
    else:
        nodeRemain = False
    node3Head = ListNode(nodeSum) # initialize the head of the new list
    node1 = node1.next
    node2 = node2.next
    node3 = node3Head
    
    while node1 or node2: # Start a loop adding additional nodes
        #print(node1.val) #for debugging
        #print(node2.val) #for debugging
        if node1 and node2:
            nodeSum = node1.val + node2.val
        elif node1:
            nodeSum = node1.val
        else:
            nodeSum = node2.val
        #print(nodeSum) #for debugging
        if nodeRemain: #add remainder
            nodeSum += 1
        #print(nodeSum) #for debugging
        if nodeSum > 9:
            nodeRemain = True
            nodeSum = nodeSum%10
        else:
            nodeRemain = False
        if node1: node1 = node1.next
        if node2: node2 = node2.next
        node3.next = ListNode(nodeSum)
        node3 = node3.next

    if nodeRemain:
        node3.next = ListNode(1)
    return node3Head
