# 입력받은 정수가 제곱수인지 판별

# 풀이

import math

def solution(n):
    answer=math.sqrt(n)
    if answer-int(answer)==0: return (answer+1)**2
    else: return -1

print(solution(3))