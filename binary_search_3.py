# p.201 떡볶이 떡 만들기

def solution(nm, rice_cakes):
    n, m = nm
    start, end = 0, max(rice_cakes)
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for rice_cake in rice_cakes:
            total += max(rice_cake - mid, 0)
        if total < m:
            end = mid - 1
        elif total > m:
            start = mid + 1
        else:
            start += 1
    return start - 1


# print(solution([4, 6], [19, 15, 10, 17]))  # 15
