# 배열 각 요소를 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환

# 풀이

def solution(arr,divisor):
    arr_divisor=[]
    for i in arr:
        if i%divisor==0:
            arr_divisor.append(i)
    if len(arr_divisor)==0: return [-1]
    arr_divisor.sort()
    return arr_divisor

print(solution([5, 9, 7, 10],5))

# 다른 풀이

def solution(arr,divisor):
    return sorted([i for i in arr if i%divisor==0]) or [-1]

print(solution([5, 9, 7, 10],5))
