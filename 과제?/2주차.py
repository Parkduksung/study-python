#k번째 수

array = [1,5,2,6,3,7,4]
commands = [[2,5,3], [4,4,1], [1,7,3]]

#풀긴했는데 더 줄여볼수 있음 lambda 쓰면.
def solution(array, commands):
    answer = []
    for num in commands:
        answer.append(sorted(array[num[0]-1:num[1]])[num[2]-1])
    return answer

print(solution(array,commands))


#두 정수 사이의 합
def solution(a, b):
    return sum([i for i in range(min(a,b),max(a,b)+1,1)])

# 축약해봄.
# def solution1(a, b):
#     return sum(range(min(a,b),max(a,b)+1))

#만약 min , max 못쓰면 3항연산자 써서 하면됨.
# max = a >= b and a or b 등.


#문자열 내 p와 y의 개수
def solution(s):
    return s.lower().count("p")==s.lower().count("y")==0 and True or s.lower().count("p")==s.lower().count("y")

# 근데 사실상 0 일때의 예외 처리 생각해서 3항 연산자 넣어봤는데 
# 처음 생각했던 s.lower().count("p")==s.lower().count("y") 이것만 해도 될듯.
# 왜냐면 둘다 0개면 저 식이 성립해서 true 뱉어내니.. 
# def solution(s):
#     return s.lower().count("p")==s.lower().count("y")

s = "Zbcdefg"

print(sorted(s))

#문자열 내림차순으로 배치하기.
def solution(s):
    return ''.join(list(reversed(sorted(s))))