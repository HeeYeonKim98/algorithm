# 수박과 같은 패던을 유지하는 문자열을 반환

# 풀이

def solution(n):
    s=""
    for i in range(0,n):
        if i%2==0:
            s+="수"
        else:
            s+="박"
    return s

print(solution(5))

