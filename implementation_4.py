# p.118 게임 개발

def solution(nm, character, graph):
    n, m = nm
    y, x, direction = character
    count = 0
    answer = 1
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    while True:
        if count == 4:
            break
        ny = y + dy[direction]
        nx = x + dx[direction]
        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == 0:
                graph[ny][nx] = 2
                y, x = ny, nx
                answer += 1
            else:
                direction = (direction + 1) % 4
                count += 1
    return answer


print(solution([4, 4], [1, 1, 0], [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]))
