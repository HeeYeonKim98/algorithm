# 인덱스 n번째 글자 기준으로 오름차순 정렬하여 반환

# 풀이

def solution(strings, n): 
    return sorted(strings, key = lambda x : x[n])

strings=["abce", "abcd", "cdxa"]
print(solution(strings,3))

## 출력 오류..