# 정수를 입력받아 정수의 약수를 모두 더한 값을 리턴

# 풀이

def solution(n):
    result=0
    for i in range(1,n+1):
        if n%i==0: result+=i
    return result

print(solution(12))


# 다른 풀이

def s(n):
    return sum([i for i in range(1,n+1) if n%i==0])

print(s(12))
