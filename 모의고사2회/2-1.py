def solution(n,price) :
    games = n*(n-1) // 2
    per_day = n // 2
    answer = (games//per_day)*price
    return answer

print(solution(7,100000))