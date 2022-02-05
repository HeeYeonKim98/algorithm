# 첫 문자가 대문자이고, 그 외의 알파벳은 소문자로 바꾸기

# 풀이 | 문장을 단어로 쪼갠 후, capitalize함수를 이용하여 첫 글자를 대문자로 바꾼 후 다시 join한다.

def jadenCase(s):
    arr=[]
    for i in s.split(" "):
        arr.append(i.capitalize())
    return " ".join(arr)

# 다른 풀이

def jadenCase(s):
    return s.title()

print(jadenCase("3people unFollowed me"))
