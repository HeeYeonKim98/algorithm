# 짝수번째는 대문자로, 홀수번째는 소문자로 바꾼 문자열을 리턴

# 풀이

def solution(s):
    split=s.split(" ")
    for i in range(len(split)):
        split_arr=list(split[i])
        for j in range(len(split_arr)):
            if j%2==0:
                split_arr[j]=split_arr[j].upper()
            else:
                split_arr[j]=split_arr[j].lower()
        split[i]="".join(split_arr)
    result=" ".join(split)
    return result


print(solution("try hello world"))