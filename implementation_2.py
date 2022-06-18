# p.113 시각

def solution(n):
    non_three_time = 15 * 60 + 60 * 15 - 15 * 15
    three_time = 60 * 60
    if n < 3:
        answer = non_three_time * (n + 1)
    elif 3 <= n < 13:
        answer = three_time + non_three_time * n
    elif 13 <= n < 23:
        answer = three_time * 2 + non_three_time * (n - 1)
    elif 23 <= n:
        answer = three_time * 3 + non_three_time * (n - 2)
    return answer


# print(solution(5))  # 11475
