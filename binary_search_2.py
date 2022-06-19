# p.197 부품 찾기

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 'yes'
        elif target < array[mid]:
            end = mid - 1
        elif target > array[mid]:
            start = mid + 1
    return 'no'


def solution(n, haves, m, finds):
    answer = []
    haves.sort()
    for find in finds:
        answer.append(binary_search(haves, find, 0, n - 1))
    return ' '.join(answer)


print(solution(5, [8, 3, 7, 9, 2], 3, [5, 7, 9]))
