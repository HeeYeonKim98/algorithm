n=int(input())
arr_random=list(map(int, input().split()))
num=23
for i in arr_random:
    if num>i:
        num=i

print(num)