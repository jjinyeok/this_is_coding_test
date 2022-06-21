# p.223 바닥 공사

def solution(n):
    results = [0 for _ in range(n)]
    results[0] = 1
    results[1] = 3
    for i in range(2, n):
        results[i] = (results[i - 1] + results[i - 2] * 2) % 796796
    return results[n - 1]


# print(solution(3))  # 5
