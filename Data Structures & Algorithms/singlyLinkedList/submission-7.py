class LinkedList:
    class ListNode:
        def __init__(self, next, val):
            self.val = val
            self.next = next
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if self.head is None: return -1
        temp = self.head
        for i in range(0,index):
            if temp is None: return -1
            if temp.next is None: return -1
            temp=temp.next
        return temp.val

        

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = self.ListNode(None, val)
            self.tail = self.head
        else:
            self.head = self.ListNode(self.head, val)

    def insertTail(self, val: int) -> None:
        if not self.tail:
            self.head = self.ListNode(None, val)
            self.tail = self.head
        else:
            self.tail.next = self.ListNode(None,val)
            self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head is None :return False
            else:
                self.head = self.head.next
                return True
        else:
            temp = self.head
            for i in range(0,index-1):
                if temp is None:
                    return False
                if temp.next is None:
                    return False
                temp = temp.next
            if temp.next is None:
                return False
            if temp.next.next == None:
                temp.next.next is None
                temp.next=None
                self.tail = temp
            else: 
                temp.next = temp.next.next
            return True
                
            

        

    def getValues(self) -> List[int]:
        if self.head is None: return []
        rtn = []
        temp = self.head
        rtn.append(temp.val)
        while temp.next is not None:
            temp = temp.next
            rtn.append(temp.val)
        return rtn
        
