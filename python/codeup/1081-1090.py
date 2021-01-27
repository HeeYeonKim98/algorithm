# 1081 - 1090

# 1081 : 주사위 2개를 굴렸을 때 나올 수 있는 수 출력
n,m=map(int, input().split(" "))
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)

# 1082 : 16진수 구구단
a=input()
a=int(a,16)
for i in range(1,16):
    result=a*i
    print("%X*%X=%X" %(a,i,result))

# 1083 : 369게임
a=int(input())
for i in range(1,a+1):
    if i==3 or i==6 or i==9: print("X",end=" ")
    else: print(i,end=" ")

# 1084 : rgb 모든 경우의 조합 출력
r,g,b=map(int,input().split(" "))
cnt=0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print("%d %d %d" %(i,j,k))
            cnt+=1
print(cnt)

# 1085 : 소리 파일 용량 계산
h,b,c,s=map(int,input().split(" "))
result=((h*b*c*s)/8)/2**20
print("%.1f MB" %result)

# 1086 : 그림 파일 용량 계산
w,h,b=map(int,input().split(" "))
result=((w*h*b)/8)/2**20
print("%.2f MB" %result)

# 1087 : 1부터 더하다가 원하는 숫자보다 크거나 같을때 break
a=int(input())
result=0
for i in range(1,a+2):
    if result>=a:
        print(result)
        break
    else: result+=i

# 1088 : 
# 1089 : 
# 1090 : 