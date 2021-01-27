# Q. 인접 리스트가 주어질 때, 모든 노드를 DFS 순서대로 방문하시오.


# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):
    stack = [start_node] # 값을 넣을 스택 생성
    visited_node = [] # 방문값을 저장할 배열 생성

    while stack: #stack값이 false일때 까지 반복
        current_node = stack.pop() #current_node라는 변수에 stack에서 하나씩 뺀 값을 저장
        visited_node.append(current_node) #그 값을 방문배열에 저장

        for adjacent_node in adjacent_graph[current_node]: # 스택에서 뺀 값의 배열 반복
            if adjacent_node not in visited_node: #만약 그 값이 방문된 값에 없을경우
                stack.append(adjacent_node) # stack에 그 값이 현재 저장된 adjacent_node를 추가한다.

    return visited_node


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!
