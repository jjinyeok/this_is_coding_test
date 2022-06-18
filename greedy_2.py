# p.92 큰 수의 법칙

def solution(nmk, array):
    answer = 0
    n, m, k = nmk
    array.sort(reverse=True)
    answer += (array[0] * k + array[1] * 1) * (m // (k + 1))
    added_count = m % (k + 1)
    answer += array[0] * added_count
    return answer


# print(solution([5, 8, 3], [2, 4, 5, 4, 6]))  # 46
