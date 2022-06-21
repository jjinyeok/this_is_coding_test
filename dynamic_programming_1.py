# p.217 1로 만들기

def solution(number):
    calculation_counts = [-1 for _ in range(30001)]
    calculation_counts[1] = 0
    for i in range(2, number + 1):
        number_candidates = []
        if i % 5 == 0:
            number_candidates.append(calculation_counts[i // 5] + 1)
        if i % 3 == 0:
            number_candidates.append(calculation_counts[i // 3] + 1)
        if i % 2 == 0:
            number_candidates.append(calculation_counts[i // 2] + 1)
        number_candidates.append(calculation_counts[i - 1] + 1)
        calculation_counts[i] = min(number_candidates)
    return calculation_counts[number]


# print(solution(26))  # 3
