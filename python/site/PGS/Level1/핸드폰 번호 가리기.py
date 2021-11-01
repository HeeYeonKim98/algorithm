# 핸드폰 번호를 입력받아 뒷 4자리를 제외한 나머지 번호를 *로 가리기

# 풀이

def solution(phone_number):
    return "*"*(len(phone_number)-4)+phone_number[-4:]

myNumber=input("")
print(solution(myNumber))
