# Q. 맥스 힙은 원소를 제거한 다음에도 맥스 힙의 규칙을 유지해야 한다.
# 맥스 힙의 원소를 제거하시오.


class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

            # 1. 루트 노드를 맨 마지막 노드 (맨 아래 레벨의 맨 오른쪽 노드)교환
            # 2. 루트노드를 배열에서 제거한뒤 저장
            # 3. 현재 꼭대기에 올라간 노드를 자식 노드들과 비교하며 내려보낸다. 이때 더큰 자식노드와 바꾸며 내려간다.
            # 4. 이과정을 자식들 보다 내가 더 클 때 혹은 바닥에 다다랐을때 까지 반복

    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]  # 맨앞과 맨마지막 노드를 바꿔준다.
        delete_heap = self.items.pop()  # 마지막 노드를 저장
        cur_index = 1  # 현재 값이있는 처음 노드가 1부터 시작

        while cur_index <= len(self.items) - 1:  # 현재 값부터 마지막까지 반복
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index # 현재 길이를 저장

             #왼쪽 트리 비교
            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                #만약 self.items의 길이의 마지막 보다 작고 그리고 items 트리내의 자식 노드의 index가 max_index보다 크다면
                max_index = left_child_index # max_index에 왼쪽 자식의 길이 저장

            #오른쪽 트리 비교     == 왼쪽 비교와 동일
            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            if max_index == cur_index: #만약 같다면 끝까지 진행된것이기 때문에
                break #브레이크

            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index] #각 비교한 값을 바꿔 저장
            cur_index = max_index

        return delete_heap  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)

# 시간 복잡도 O(log(N))

# 최대값 , 최소값을 빨리뽑을때 사용

# 최대값만 필요하고 다른건 필요없을시 , 이때 사용
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]
