# 배열에서 가장 작은 수를 제거한 배열을 리턴

# 풀이

def solution(arr):
    arr.remove(min(arr))
    if len(arr)==0: arr.append(-1)
    return arr

print(solution([1]))