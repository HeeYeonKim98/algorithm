# 1167

# 세 개의 숫자가 주어질 때 두번째로 작은 수를 출력하시오.

num = list(map(int, input().split(" ")))
num.sort()
print(num[1])