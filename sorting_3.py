# p.182 두 배열의 원소 교체

def solution(n, k, array_a, array_b):
    array_a.sort()
    array_b.sort(reverse=True)
    for i in range(k):
        if array_a[i] < array_b[i]:
            array_a[i], array_b[i] = array_b[i], array_a[i]
        else:
            break
    return sum(array_a)


print(solution(5, 3, [1, 2, 5, 4, 3], [5, 5, 6, 6, 5]))  # 26
