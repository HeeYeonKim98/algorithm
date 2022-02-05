# n번째 피보나치 수를 1234567로 나눈 나머지를 리턴

# 풀이 | 피보나치 수열 식을 3번째부터 구현하게 만들고 1234567로 나누어 fib 리스트에 추가하였다. 

def fibonacciNum(n):
    fib=[0,1]
    for i in range(2, n+1):
        fib.append((fib[i-1]+fib[i-2])%1234567)
    return fib[-1]

print(fibonacciNum(5))


# 참고 : 피보나치 수열 알고리즘
def fibonacci(n):
    return fibonacci(n-1)+fibonacci(n-2) if n>=2 else n

for n in range(1,11):
    print(fibonacci(n))
print(fibonacci(10))