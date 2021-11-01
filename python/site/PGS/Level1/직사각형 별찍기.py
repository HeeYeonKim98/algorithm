# 입력받은 숫자로 직사각형 별 찍기

# 풀이

a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a-1):
        print("*",end="")
    print("*")
    
# 풀이 고치기

a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print("*",end="")
    print("")

# 다른 풀이

a,b = map(int, input().strip().split(" "))
answer = ('*'*a+'\n')*b
print(answer)

