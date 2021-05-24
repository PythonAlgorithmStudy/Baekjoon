# 스택과 큐 두 자료형을 모두 갖고 있는 복합 자료형 '데크'
# 데크란 더블 엔디드 큐의 줄임말로, 글자 그대로 양쪽 끝을 모두 추출할 수 있는 큐를 일반화한 형태의 추상 자료형(ADT) 이다.

# 원형 데크 디자인 (아래 연산을 제공하는 데크를 디자인하기)

class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

## 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node: ListNode, new: ListNode):
        n = node.right ### 이 부분만 이해가 안된다 왜 갑자기 n이 나타난거지? 흠..? n이 무조건 node 오른쪽에 있는 것을 뜻하는 건가?
        node.right = new
        new.left, new.rigth = node, n
        n.left = new
    
    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node
    
    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k: # 리스트 길이 판별
            return False
        self.len += 1 # 
        self._add(self.tail.left, ListNode(value)) 
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.lent -= 1
        self._del(self.head)
        return True
    
    def deleteLst(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.en else -1
    
    def isEmpth(self) -> bool:
        return self.len == 0
    
    def isFull(self) -> bool:
        return self.len == self.k
