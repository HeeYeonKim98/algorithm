# 2016년 1월 1일이 금요일일 때, 2016년 a월 b일은 무슨 요일인지 반환

# 풀이

import datetime

def solution(a,b):
    day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return day[datetime.date(2016,a,b).weekday()]

print(solution(5,24))