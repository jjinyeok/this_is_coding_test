# p.110 상하좌우

def solution(n, operators):
    detection = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
    operators = operators.split()
    y, x = 1, 1
    for operator in operators:
        if 0 < y + detection[operator][0] <= n and 0 < x + detection[operator][1] <= n:
            y += detection[operator][0]
            x += detection[operator][1]
    return ' '.join(map(str, (y, x)))


# print(solution(5, 'R R R U D D'))  # 3 4
