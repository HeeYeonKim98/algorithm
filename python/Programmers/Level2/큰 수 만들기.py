# 주어진 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자

# 풀이

def maxNum(number,k):
    number=list(number)
    for i in range(k):
        number.pop(number.index(min(number)))
    answer="".join(number)
    return answer

print(maxNum("1924",2))
print(maxNum("1231234",3))
