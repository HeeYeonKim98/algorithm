# 문자열이 4 또는 6이고, 숫자로만 구성되어있는지 확인

# 풀이

def solution(s):
    if len(s)==4 or len(s)==6:
        if s.isdigit(): return True
        else: return False
    else: return False

print(solution("123a"))