# Q. 맥스 힙은 원소를 추가한 다음에도 맥스 힙의 규칙을 유지해야 한다.
# 맥스 힙에 원소를 추가하시오.


class MaxHeap:
    def __init__(self):
        self.items = [None]

# 1. 원소 맨끝에 추가
# 2. 지금 넣은 새노드를 부모와 비교, 만약 부모보다 크다면 교체
# 3. 이 과정을 꼭대기까지 반복

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1 # 가장 마지막에 있는 노드

        while cur_index > 1: # 1일경우 맨 정상이기때문에 1전까지
            parent_index = cur_index // 2 # 부모 인덱스 가져오는 방법
            if self.items[parent_index] < self.items[cur_index]: #만약 자식이 부모보다 크다면
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index] #교체
                cur_index = parent_index #바꾼 후에는 자식 인덱스가 부모 인덱스보다 크기때문에 값을 바꿔줘야한다.
            else:
                break


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!


#시간 복잡도 : O(log(N))