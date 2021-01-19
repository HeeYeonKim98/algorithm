# a,b,v=map(int,input().split(" "))

# print(v//(a-b))


# a=int

# while a!=0:
#     a=input().split()
#     for i in range(len(a)):
#         if a[i]=="0": break
#         else: print(a[i])
#     break
    
# a=chr(input())
# while a<'z'+1:
#     print(a)
#     a=a+1
s=int()
a=int(input())
for i in range(1,a+1):
    if i%2==0: s=s+i
print(s)
