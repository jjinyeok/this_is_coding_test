# p.190 이진 탐색

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid + 1
        elif target < array[mid]:
            end = mid - 1
        elif target > array[mid]:
            start = mid + 1
    return None


# print(binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 7, 0, 9))  # 4
