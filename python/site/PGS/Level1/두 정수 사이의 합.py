# 두 정수를 받아 두 정수 사이에 속한 모든 정수의 합을 반환

# 풀이

def solution(a,b):
    result=0
    a,b=min(a,b),max(a,b)
    for i in range(a,b+1):
        result+=i
    return result

print(solution(5,3))

# 풀이 고치기

def solution(a,b):
    a,b=min(a,b),max(a,b)
    return sum(range(a,b+1))

print(solution(5,3))


