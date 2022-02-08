# 한 자리 숫자가 적힌 종이들을 이어 붙여 만들 수 있는 소수의 갯수를 반환

# 풀이 | 에라토스테네스의 체

import itertools

def primeNumber(number):
    answer = []
    newNumber = []
    last=[]

    for n in range(1, len(number) + 1):
        answer += list(itertools.permutations(list(number), n))
    newNumber = [int("".join(a)) for a in answer]

    for i in newNumber:
        if i < 2:
            continue
        check=True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                check=False
                break
        if check:
            last.append(i)
            
    return len(set(last))

# print(primeNumber("17"))
print(primeNumber("011"))