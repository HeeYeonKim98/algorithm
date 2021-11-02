# 입력받은 자연수를 뒤집어 배열로 리턴

# 풀이

def solution(n):
    arr=list(map(int,str(n)))
    arr.reverse()
    return arr

print(solution(12345))