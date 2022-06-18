# p.87 예제 3-1 거스름 돈

def solution(n):
    answer = 0
    coins = [500, 100, 50, 10]
    for coin in coins:
        if n > coin:
            answer += (n // coin)
            n %= coin
    return answer


# print(1260)  # 5
