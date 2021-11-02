# 두 수를 입력받아 최대공약수와 최소공배수를 반환

# 풀이

import math

def solution(n,m):
    GCD=math.gcd(n,m)
    LCM=n*m//GCD
    return GCD,LCM

print(solution(2,5))

# 다른 풀이 (유클리드 호제법)

def gcd(n,m):
    a,b=max(n,m),min(n,m)
    answer=1
    while answer!=0:
        answer=a%b
        a,b=b,answer
    return a

print(gcd(1112,695))

