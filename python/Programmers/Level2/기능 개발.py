# 진척도와 진행도가 담긴 리스트를 가지고 하루의 배포 횟수 구하기

# 풀이 | queue가 비어있거나 계산올림한 값이 이전 배포일 보다 길 때, 1을 넣어주고 같거나 짧을 때, 배포 갯수를 올려준다.

import math

def deployment(progresses, speeds):
    queue=[]
    for p, s in zip(progresses, speeds):
        if len(queue) == 0 or queue[-1][0] < math.ceil((100 - p) // s):
            queue.append([math.ceil((100 - p) // s), 1])
        else:
            queue[-1][1] += 1
    return [q[1] for q in queue]

print(deployment([93,30,55],[1,30,5]))
print(deployment([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))

# 오답

# def deployment(propgresses,speeds):
#     index = 0
#     count = 1
#     period = []
#     deploy=[]

#     while index < len(propgresses):
#         p,s=propgresses[index],speeds[index]
#         period.append(math.ceil((100 - p) / s))
#         index += 1

#     for i in range(len(period)-1):
#         point=period[i]
#         while point >= period[i+1]:
#             count += 1
#         deploy.append(count)
#             # period.pop(i)

#     return period,deploy