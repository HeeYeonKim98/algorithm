# 입력받은 문자열 속 숫자의 최대, 최솟값 구하기

# 풀이 | 입력받은 문자열을 list로 변환하여 최대, 최소를 구한다.

def max_min(s):
    arr=list(map(int, s.split()))
    return str(min(arr)) + " " + str(max(arr))

print(max_min("1 2 3 4"))