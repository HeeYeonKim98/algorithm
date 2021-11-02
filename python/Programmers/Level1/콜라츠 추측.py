# 조건을 만족하여 1이 될 때까지 반복하고, 500번 이상 반복되면 -1을 반환

# 풀이

def solution(number):
    i=0
    while number!=1:
        if number%2==0:
            number=number/2
        else:
            number=number*3+1
        i+=1
        
        if i>=500:
            return -1

    return i

num = int(input(""))
print(solution(num))