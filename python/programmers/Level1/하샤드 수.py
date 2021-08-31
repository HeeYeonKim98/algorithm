# 

# 풀이

def solution(num):
    hap=sum(map(int,str(num)))
    print(num)
    if num%hap==0: return True
    else: return False

print(solution(18))