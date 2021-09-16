# 문자열 내림차순으로 정렬해 반환

# 풀이

def solution(s):
    arr=list(map(str,s))
    arr.sort(reverse = True)
    return "".join(arr)

print(solution("Zbcdefg"))

# 풀이 고치기

def solution(s):
    return "".join(sorted(s,reverse=True))