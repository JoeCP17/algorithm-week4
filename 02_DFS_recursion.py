# DFS를 이용한 예제

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
visited = []


# 제공되있는것 : 그래프 , 시작점 , 방문한곳 담기
# 방문한곳 = > visited_array에 추가


def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)  # 방문 목록에 현재 노드를 추가
    for adjacent_node in adjacent_graph:  # 그리고 인접노드를 확인하기 위해 그래프를 반복
        if adjacent_node not in visited_array:  # 만약 인접노드 배열에 포함되지 않는다면
            
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)  # 함수를 한번더 반복


dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!
