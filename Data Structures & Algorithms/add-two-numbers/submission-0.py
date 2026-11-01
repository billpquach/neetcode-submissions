# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # iterate through both linked lists
        # append to separate arrays one_arr, two_arr [1, 2, 3], [4, 5, 6] 
        # slice and reverse both arrays [::-1]       [3, 2, 1], [6, 5, 4]

        # s1, s2 = "".join(one_arr), "".join(two_arr)

        # res = []
        # s1, s2 = int(s1), int(s2)
        # s1 += s2
        # for i in s1:
        #     res.append(i)
        # return res

        l_arr , r_arr = [], []
        res = []

        curr = l1
        while curr != None:
            l_arr.append(str(curr.val))    # [1, 2, 3]
            curr = curr.next


        while l2 != None:
            r_arr.append(str(l2.val))    # [4, 5, 6]
            l2 = l2.next
        
        l_arr, r_arr = l_arr[::-1], r_arr[::-1]     # [6, 5, 4] ; [3, 2, 1]
        s1, s2 = "".join(l_arr), "".join(r_arr)     #    "654"  ;   "321"
        s1, s2 = int(s1), int(s2)
        s1 += s2
        s1 = str(s1)
        s1 = list(s1)
        s1 = s1[::-1]

        print(s1)
        
        l3 = ListNode()
        curr = l3
        for i in range(len(s1)-1):
            curr.next = ListNode()
            curr = curr.next
        curr = l3
        for i in s1:
            curr.val = i
            curr = curr.next
            
            
        return l3
        
        
    