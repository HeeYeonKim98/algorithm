# 트럭이 다리를 건너는 데에 걸리는 시간을 반환

# 풀이 | 햔재 다리를 건너는 트럭과 다음 다리를 건널 트럭의 무게의 합이 다리가 견딜 수 있는 무게보다 적으면 함께 건너게 한다.

def solution(bridge_length, weight, truck_weights):
    answer=0
    bridge=[0 for _ in range(bridge_length)]

    while bridge:
        answer += 1
        bridge.pop(0)

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
            else:
                bridge.append(0)
    return answer

print(solution(2,10,[7,4,5,6]))