# 단어의 가운데 글자를 반환하는 함수, solution을 만드시오.

# 풀이

def solution(word):
    leng=len(word)
    if leng%2==0:
        answer=word[leng//2-1:leng//2+1]
        return answer
    else:
        answer=word[leng//2:leng//2+1]
        return answer

# 다른 풀이

def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]

print(string_middle("power"))