# 배열의 평균값을 리턴하는 함수

# 풀이

def solution(arr):
    sum = 0
    for i in arr:
        sum+=i
    avg=sum/len(arr)

    return avg

# 다른 풀이

def solution(arr):
    return sum(arr)/len(arr)

print(solution([1,2,3,4]))
