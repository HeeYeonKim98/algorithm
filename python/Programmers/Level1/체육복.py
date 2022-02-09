# 전체 학생 수(n), 체육복을 도난당한 학생 번호 배열(lost), 여벌의 체육복을 가져온 학생 번호 배열(reserve)가 있을 때, 체육수업을 들을 수 있는 학생의 최댓값을 반환

# 풀이

def solution(n,lost,reserve):
    set_reserve=set(reserve)-set(lost)
    set_lost=set(lost)-set(reserve)

    for i in set_lost:
        if i+1 in set_reserve:
            set_reserve.remove(i+1)
        elif i-1 in set_reserve:
            set_reserve.remove(i-1)
        else:
            n-=1
    return n


print(solution(5,[2, 4],[1, 3, 5]))