# p. 96 숫자 카드 게임

def solution(n, m, array):
    answer = 0
    for row in array:
        min_row = min(row)
        if answer < min_row:
            answer = min_row
    return answer


# print(solution(3, 3, [[3, 1, 2], [4, 1, 4], [2, 2, 2]]))  # 2
# print(solution(2, 4, [[7, 3, 1, 8], [3, 3, 3, 4]]))  # 3
