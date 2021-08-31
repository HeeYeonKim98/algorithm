# String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수를 작성하시오.

# 풀이

def solution(seoul):
    for index, value in enumerate(seoul):
        if value=="Kim":
            num=index
            break
            
    return "김서방은 %d에 있다" %num

arr=["Jane", "Kim"]
print(solution(arr))

# 다른 풀이

def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

arr=["Jane", "Kim"]
print(findKim(arr))