# p.178 위에서 아래로

def solution(n, array):
    array.sort(reverse=True)
    return ' '.join(map(str, array))


# print(solution(3, [15, 27, 12]))  # 27 15 12
