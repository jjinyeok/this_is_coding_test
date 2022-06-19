# p.180 성적이 낮은 순서로 학생 출력하기

def solution(n, array):
    array.sort(key=lambda x: x[1])
    answer = []
    for name, score in array:
        answer.append(name)
    return ' '.join(answer)


# print(solution(2, [['홍길동', 95], ['이순신', 77]]))  # 이순신 홍길동
