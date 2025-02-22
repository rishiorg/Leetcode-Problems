# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0) 
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            sum_val = carry
            
            if l1:
                sum_val += l1.val
                l1 = l1.next
                
            if l2:
                sum_val += l2.val
                l2 = l2.next
            
            carry, value = divmod(sum_val, 10)
            
            current.next = ListNode(value)
            current = current.next  # Move to the next node
        
        return dummy.next  # Return the head of the result list


        