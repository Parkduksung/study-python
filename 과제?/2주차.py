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

s = "oo"

result = s.lower().count("p")==s.lower().count("y")==0 and True or s.lower().count("p")==s.lower().count("y")

print(result)

#문자열 내 p와 y의 개수
def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True




