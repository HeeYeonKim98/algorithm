# H-index 구하기 https://www.ibric.org/myboard/read.php?Board=news&id=270333

# 풀이 | 내림차순으로 정렬하고, 인덱스가 같아지거나 인용지수보다 커지는 순간의 인덱스를 반환한다.

def hIndex(citations):
    citations.sort(reverse=True)
    for i,c in enumerate(citations):
        if i>=c:
            return i

print(hIndex([3, 0, 6, 1, 5]))