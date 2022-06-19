# p.152 미로 탈출

from collections import deque


def solution(n, m, graph):
    q = deque()
    q.append([0, 0])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                q.append([ny, nx])
    return graph[n - 1][m - 1]


# ex_n, ex_m = 5, 6
# ex_graph = [[1, 0, 1, 0, 1, 0],
#             [1, 1, 1, 1, 1, 1],
#             [0, 0, 0, 0, 0, 1],
#             [1, 1, 1, 1, 1, 1],
#             [1, 1, 1, 1, 1, 1]]
# print(solution(ex_n, ex_m, ex_graph))  # 10
