# p.149 음료수 얼려 먹기

from collections import deque


def bfs(y, x, n, m, graph):
    q = deque()
    q.append([y, x])
    graph[y][x] = -1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
                graph[ny][nx] = -1
                q.append([ny, nx])


def solution(n, m, graph):
    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                bfs(i, j, n, m, graph)
                answer += 1
    return answer


# ex_n, ex_m = 4, 5
# ex_graph = [[0, 0, 1, 1, 0],
#             [0, 0, 0, 1, 1],
#             [1, 1, 1, 1, 1],
#             [0, 0, 0, 0, 0]]
# print(solution(ex_n, ex_m, ex_graph))  # 3
