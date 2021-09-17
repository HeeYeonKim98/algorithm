# 세 명의 수포자가 찍는 방식으로 가장 많은 문제를 맞힌 사람을 배열에 담아 반환

# 풀이

def solution(answers):
    pattern1=[1,2,3,4,5]
    pattern2=[2,1,2,3,2,4,2,5]
    pattern3=[3,3,1,1,2,2,4,4,5,5]
    count1=0
    count2=0
    count3=0

    answer=[]
    
    for i in range(len(answers)):
        if answers[i]==pattern1[i%len(pattern1)]:
            count1+=1
        if answers[i]==pattern2[i%len(pattern2)]:
            count2+=1
        if answers[i]==pattern3[i%len(pattern3)]:
            count3+=1

    count_arr=[count1,count2,count3]
    for key,value in enumerate(count_arr):
        if value==max(count_arr):
            answer.append(key+1)

    return answer

print(solution([1,2,3,4,5]))