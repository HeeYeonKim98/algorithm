# 1091 - 1099

# 1091 : 만든 수열 구현
a,m,d,n=map(int, input().split(" "))
for i in range(1,n):
    a=a*m+d
print(a)

# 1092 : 함께 문제 풀어보는 날 예측하기
a,b,c=map(int, input().split(" "))
day=1
while day%a!=0 or day%b!=0 or day%c!=0:
    day+=1
print(day)

# 1093 : 출석 부르기 1

# 1094 : 출석 부르기 2

# 1095 : 출석 부르기 3

# 1096 : 바둑판

# 1097 : 바둑알

# 1098 : 설탕과자 뽑기

# 1099 : 성실한 개미
