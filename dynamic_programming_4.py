# p.226 효율적인 화폐 구성

def solution(nm, coins):
    n, m = nm
    results = [-1 for _ in range(10001)]
    for coin in coins:
        results[coin] = 1
    for i in range(1, m + 1):
        if results[i] != -1:
            continue
        tmp_result = []
        for coin in coins:
            if coin < i and results[i - coin] != -1:
                tmp_result.append(results[i - coin] + 1)
        if tmp_result:
            results[i] = min(tmp_result)
    return results[m]


# print(solution([2, 15], [2, 3]))  # 5
# print(solution([3, 4], [3, 5, 7]))  # -1
