# Q. 인접 리스트가 주어질 때, 모든 노드를 BFS 순서대로 방문하시오.


# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


# 1. 시작 노드를 큐에 넣는다.
# 2. 현재 큐의 노드를 빼서 visited에 추가
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가

def bfs_queue(adj_graph, start_node):
    queue = [start_node]  # 초기노드 값 queue에 저장
    visited = []  # 방문한 곳 저장

    while queue:  # queue가 빈상태가 아닐때까지 반복
        current_node = queue.pop(0)  # 앞자리가 계속빠져나가야하기때문에 0삽입
        # 큐에서 하나씩 빼서 그 수를 current_node에 저장

        visited.append(current_node)  # 뺀 수 visited 리스트에 저장
        for adj_node in adj_graph[current_node]:  # for문을통해 큐에서뺀 초기값이 있는 수부터 계속 반복
            if adj_node not in visited:  # adj_node에 있는 숫자가 visited에 없다면
                queue.append(adj_node)  # 큐에 그 수를 추가함으로 하나씩 빼서 visited에 저장시키게한다.

    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!
