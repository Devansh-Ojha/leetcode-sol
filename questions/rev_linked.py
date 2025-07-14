class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev=head, None
        while curr:

            tmp = curr.next # store the pointer for later use
        
            curr.next=prev # now reverse it basicall makes 1->2 to 2<-1
            prev=curr # so None points to back of list or 2
            curr=tmp 
        return prev
