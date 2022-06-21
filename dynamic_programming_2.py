# p.220 개미 전사

def solution(n, array):
    results = [0 for _ in range(n)]
    results[0] = array[0]
    results[1] = max(array[0], array[1])
    for i in range(2, n):
        results[i] = max(results[i - 2] + array[i], results[i - 1])
    return results[n - 1]


# print(solution(4, [1, 3, 1, 5]))  # 8
