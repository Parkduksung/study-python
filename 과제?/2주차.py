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


#문자열 내림차순으로 배치하기.
def solution(s):
    return ''.join(list(reversed(sorted(s))))

#sorted 는 list() 로 안감싸도 잘 나오는데 
#reversed 는 list 로 감싸야 나옴.
#kotlin 에서 joinToString 같이 join 으로 list -> String 으로 바꿈.
#sorted 내부 보니까 파라메터로 bool 형식의 reverse 가 있네.
# 좀더 줄여보면 ''.join(sorted(s, reverse=True)) 이런식으로 가능. 가독성에서는 좋지만 하는건 똑같음.


#문자열 다루기 기본.
def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()

#여기서 한번더 줄여보면 4,6 이니까 이걸 그냥 리스트에 담아 놓고 in 으로 안에 있는지 확인해볼수 있는듯.
#len(s) in [4,6] and s.isdigit()

#문자열 내 마음대로 정렬하기
import operator

def solution(strings, n):
    return  [i[0] for i in sorted(({i:i[n] for i in sorted(strings)}).items(), key=operator.itemgetter(1))]


#가운데 글자 가져오기
def solution(s):
    return s[int(len(s)/2)-1 : int(len(s)/2)+1] if len(s)%2 == 0 else s[int(len(s)/2)]


#두 개 뽑아서 더하기.

number = [5,0,2,7]

t = []
for i in range(len(number)) :
    for j in range(len(number)) :
        if i!=j :
            t.append(number[i]+number[j])


print(sorted(list(set(t))))