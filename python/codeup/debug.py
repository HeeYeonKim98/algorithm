a=int(input())
result=0

for i in range(1,a+2):
    if result>=a:
        print(result)
        break
    else:
        result+=i