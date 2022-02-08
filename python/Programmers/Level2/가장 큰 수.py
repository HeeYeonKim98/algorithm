# 입력받은 배열을 이어붙여 만들 수  있는 수 중 가장 큰 수 구하기

# 풀이 | numbers가 1000이하 이므로 문자열을 3배로 키우고 sort한다.
# int-str로 변환하는 이유는 000(*3한 값이)을 처리 하기 위함

def maxNumber(numbers):
    numbers=list(map(str,numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return ''.join(numbers)

print(maxNumber([6, 10, 2,0]))
