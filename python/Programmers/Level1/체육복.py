# 전체 학생 수(n), 체육복을 도난당한 학생 번호 배열(lost), 여벌의 체육복을 가져온 학생 번호 배열(reserve)가 있을 때, 체육수업을 들을 수 있는 학생의 최댓값을 반환

# 풀이

def solution(n,lost,reserve):
    set_reserve=set(reserve)-set(lost)
    set_lost=set(lost)-set(reserve)
    
    return 0

n=5
lost=[2,4]
reserve=[1,3,5]
print(solution(n,lost,reserve))

i=0
sum=0
while i<10:
    i=i+1
    if i%2==0:
        continue
    sum=sum+i


print(sum)