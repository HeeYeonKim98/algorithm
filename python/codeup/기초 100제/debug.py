h,w=map(int, input().split(" "))
arr = [[0 for col in range(h)] for row in range(w)]
n=int(input())

for i in range(n):
    l,d,x,y=map(int, input().split(" "))

for i in arr:
    for j in i:
        print(j,end=" ")
    print()