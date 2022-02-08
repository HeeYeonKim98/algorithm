# 우선순위가 있는 문서를 프린트 하는 과정에서 순서를 출력

# 풀이 | 한 번더 풀어보기

def printer(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    answer = 0

    while True:
        item = queue.pop(0)
        if any(item[1] < q[1] for q in queue):
            queue.append(item)
        else:
            answer += 1
            if item[0] == location:
                return answer

print(printer([2, 1, 3, 2],2))

# 오답
    # if max(priorities)>priorities[0]:
    #     priorities.append(priorities.pop(0))
    # else:
    #     arr.append(priorities.pop(0))