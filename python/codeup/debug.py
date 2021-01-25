a=input()
result="a"

while result!=a:
    print(result,end=' ')
    result=ord(result)
    result=result+1
    result=chr(result)
print(a)