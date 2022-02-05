# 2차원 행렬 2개를 곱한 결과를 반환

# 풀이 | i,j,k로 행렬을 접근하여 곱하기

def matrix(arr1, arr2):
    result = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                result[i][j] += (arr1[i][k] * arr2[k][j])
    return result

print(matrix([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))