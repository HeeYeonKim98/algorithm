# 입력받은 N개의 최소공배수 구하기

# 풀이 | 입력받은 배열 요소 중 두 개씩 뽑아 최대공약수를 구한 후, 최소공배수를 구한다. 

import math

def nLCM(arr):
    result=arr[0]
    for i in arr:
        result = i * result // math.gcd(i,result) 
    return result

print(nLCM([1,2,3]))