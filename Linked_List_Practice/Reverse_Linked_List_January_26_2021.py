# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        # Function to reverse the linked list
        prev = None
        pointer = node
        while pointer:
            # store the next pointer
            nextt = pointer.next
            # make the next pointer the previous
            pointer.next = prev
            # make the previous the current pointer
            prev = pointer
            # increment to work on the next node
            pointer = nextt
        node = prev
        return node