import numpy as np
# 두개의 행렬을 받아 같은 행, 열의 값을 서로 더한 값을 반환

# 풀이

# def solution(arr1, arr2):
#     Arr1=np.array(arr1)
#     Arr2=np.array(arr2)
#     answer=Arr1+Arr2
#     print(answer.tolist())

# print(solution([[1,2],[2,3]],[[3,4],[5,6]]))

# 다른 풀이 (numpy 사용 x)

def solution(arr1,arr2):
    answer=[[c+d for c,d in zip(a,b)] for a,b in zip(arr1,arr2)]
    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))