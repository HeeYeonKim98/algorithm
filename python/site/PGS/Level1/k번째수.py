# 배열을 정해진 숫자대로 자르고 정렬했을 때, k번째에 있는 수를 반환

# 풀이

def solution(arr,commands):
    k_arr=[]
    for i,j,k in commands:
        sort_arr=sorted(arr[i-1:j])
        k_arr.append(sort_arr[k-1])
    return k_arr

arr=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(arr,commands))