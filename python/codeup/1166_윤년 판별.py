# 1166

# 해를 입력받아 그 해가 윤년인지 아닌지 판별하시오.

year=int(input())

if year%4==0:
    if year%100!=0:
        print("yes")
    elif year%400==0:
        print("yes")
    else:
        print("no")

else:
    print("no")