# 1071 - 1080

# 1071 : 0 입력될 때까지 무한 출력
# 1072 : 정수 입력받아 무한 출력

# 1073 : 0 입력될 때까지 무한 출력
a=input().split()
for i in range(len(a)):
    if a[i]=="0": break
    else: print(a[i])

# 1074 : 정수 입력받아 카운트다운 출력
a=int(input())
for i in range(1,a+1):
    print(a)
    a=a-1

# 1075 : 정수 입력받아 카운트다운 출력
a=int(input())
for i in range(1,a+1):
    a=a-1
    print(a)

# 1076 : 문자 입력받아 알파벳 출력


# 1077 : 
# 1078 : 짝수 합 출력
s=int()
a=int(input())
for i in range(1,a+1):
    if i%2==0: s=s+i
print(s)

# 1079 : "q" 입력될 때까지 무한 출력
a=input().split(" ")
for i in range(len(a)):
    if a[i]=="q":
        print(a[i])
        break
    else:
        print(a[i])

# 1080 : 원하는 숫자보다 같거나 클때까지 더하기
a=int(input())
result=0
for i in range(1,a):
    if(a<=result):
        print(i-1)
        break
    else:
        result=result+i
