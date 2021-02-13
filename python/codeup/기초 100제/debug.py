n=int(input())
arr = [[0 for col in range(19)] for row in range(19)]
for i in range(n):
    a,b=map(int, input().split(" "))
    arr[a-1][b-1]=1

for i in arr:
    for j in i:
        print(j,end=" ")
    print()