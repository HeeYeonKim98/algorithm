# 동전의 종류가 N개이고 그 동전으로 가치의 합을 K로 만들려고 할 때, 필요한 동전 개수의 최솟값을 구해라

# 풀이

def min_coin(price, arr):
    min_coin=0
    for i in arr:
        if price<i: continue
        else:
            min_coin+=int(price/i)
            price=price%i
    return min_coin

coin,price=map(int,input().split(" "))
coin_type=[]
for i in range(coin):
    coin_type.append(int(input()))

coin_type.sort(reverse=True)

print(min_coin(price,coin_type))

# 출처 baekjoon 11047