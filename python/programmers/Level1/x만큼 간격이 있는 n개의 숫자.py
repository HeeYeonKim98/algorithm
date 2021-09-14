# 정수와 자연수를 입력받아 정수씩 증가하는 숫자를 지니는 리스트를 리턴

# 풀이

def solution(x,n):
    arr=[x*i for i in range(1,n+1)]
    return arr

print(solution(-4,2))