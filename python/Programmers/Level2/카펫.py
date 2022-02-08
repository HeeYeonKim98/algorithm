# 갈색, 노란색 격자가 담긴 카펫의 가로, 세로 크기를 반환

# 풀이 | 둘레를 이용해서 brown + yellow = width * height를 구할 수 있다.

def carpet(brown, yellow):
    answer=[]
    total = brown + yellow

    for height in range(1, total + 1):
        width = total / height
        if (width) % 1 == 0 and width >= height and 2 * width + 2 * height == brown + 4:
            return [int(width), height]
    return answer

print(carpet(24, 24))