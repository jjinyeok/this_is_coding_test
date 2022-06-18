# p.115 왕실의 나이트

def solution(location):
    answer = 0
    x = ord(location[0]) - ord('a')
    y = int(location[1]) - 1
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    for i in range(8):
        if 0 <= dx[i] + x < 8 and 0 <= dy[i] + y < 8:
            answer += 1
    return answer


# print(solution('a1'))  # 2
# print(solution('c2'))  # 6
