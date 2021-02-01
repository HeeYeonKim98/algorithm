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

# 1093 : 랜덤으로 n명 출석 부르기
n=int(input())
arr_random=input().split(" ")
arr_num=list(0 for i in range(24))

for i in range(n):
    arr_num[int(arr_random[i])]+=1

for j in range(1,24):
    print(arr_num[j], end=" ")

# 잘 나오는데 오답(map함수를 사용한게 원인인듯 함.)
n=int(input())
arr_random=map(int, input().split(" "))
arr_num=list(0 for i in range(24))

for i in arr_random:
    arr_num[i]+=1

for j in range(1,24):
    print(arr_num[j], end=" ")


# 1094 : 출석 번호 순서 바꾸기
n=int(input())
arr_random=list(map(int, input().split()))
for i in reversed(arr_random):
    print(i, end=" ")

# 1095 : 출석 부르기 3
n=int(input())
arr_random=list(map(int, input().split()))
print(min(arr_random))

#
n=int(input())
arr_random=list(map(int, input().split()))
num=23
for i in arr_random:
    if num>i:
        num=i

print(num)

# 1096 : 바둑판

# 1097 : 바둑알

# 1098 : 설탕과자 뽑기

# 1099 : 성실한 개미
