# 스코빌 지수 공식을 이용하여 리스트 안 모든 숫자가 K이상의 스코빌이 되도록 

# 풀이
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    print(scoville)

    while scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville)+(heapq.heappop(scoville) * 2))
        answer += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer, scoville


print(solution([1, 10, 9, 3, 2, 12],7)) # 2
print(solution([1, 7, 6, 13, 14, 16],7)) # 2
print(solution([1, 6, 7, 1, 14, 16],7)) # 2
