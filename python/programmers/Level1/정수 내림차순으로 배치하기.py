# 입력 받은 정수를 내림차순으로 정렬하여 리턴하기

# 풀이

def solution(num):
    numArr = list(map(int,str(num)))
    numArr.sort(reverse=True)
    return int("".join(map(str,numArr)))

print(solution(118372))

# 풀이 고치기

def dolution(num):
    numArr = list(str(num))
    numArr.sort(reverse=True)
    return int("".join(numArr))

# 다른 풀이
