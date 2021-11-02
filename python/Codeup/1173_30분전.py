# 1173

# 시간과 분을 입력받아 이 시간 기준 30분 전 시간을 출력하시오.

h,m=map(int, input().split(" "))

res=m-30

if res<0:
    if h==0:
        h+=23
    else:
        h-=1
    res=60-(-res)
    print(h,res)
else:
    print(h,res)

# 다른 풀이

