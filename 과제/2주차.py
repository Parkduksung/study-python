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

def solution(numbers):
    answer = []
    for i in range(len(numbers)) :
        for j in range(len(numbers)) :
            if i!=j :
                answer.append(numbers[i]+numbers[j])
    return sorted(list(set(answer)))



#수박수박수박~
#너무 쉽게 품..
def solution(n):
    answer = ''
    for i in range(n) :
        if i%2==0 :
            answer +="수"
        else:
            answer +="박"
    return answer


#3진법 뒤집기
def solution(n):
    return sum(
        int(3**(len(reverse3Notation(n))-1-i)) * reverse3Notation(n)[i] for i in range(len(reverse3Notation(n))))

def reverse3Notation(n) : 
    a = []
    while n :
        if n%3 == 0 :
            a.append(0)
        else:
            a.append(int(n%3))
        n = int(n/3)
    return a

#같은 숫자는 싫어
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(len(arr)-1) :
        if arr[i] == arr[i+1] :
            continue
        else:
            answer.append(arr[i+1])
    return answer

#자연수 뒤집어 배열로 만들기.
def solution(n):
    return list(reversed([int(i) for i in str(n)]))

#약수의 합
def solution(n):
    answer = 0
    for i in range(1,n+1) :
        if n%i ==0 :
            answer += i
    return answer

#문자열 정수로 바꾸기
def solution(s):
    answer = int(s)
    return answer

# #나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = [i for i in arr if i%divisor == 0]
    return sorted(answer) if len(answer)!=0 else [-1]


#짝수와 홀수
def solution(num):
    return "Even" if num%2==0 else "Odd"

#x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    return [x*i for i in range(1,n+1)]

#서울에서 김서방 찾기
def solution(seoul):
    return "김서방은 "+ str(seoul.index("Kim"))+"에 있다"
#format 으로 하는것도 생각
# => "김서방은 {}에 있다".format(seoul.index("Kim"))

#행렬의 덧셈
def solution(arr1, arr2):
    result = [[]]
    for i in range(0,len(arr1)) :
        if i!=0 :
            result.extend([[]])
        for j in range(0,len(arr1[0])) :
            result[i].append(arr1[i][j] + arr2[i][j])
    return result

#너무 어렵게 푼거같은데.. for i,j 이런식으로 해서 zip 이용해서도 풀어보아야 할 문제.

#핸드폰 번호 가리기
def solution(phone_number):
    return ''.join(["*" for i in range(0,len(phone_number)-4)])+phone_number[-4:]

#생각해보니 "*" * len(phone_number)-4 해도 되네.


#2016년
import datetime 
def solution(a, b):
    
    day_list = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return day_list[datetime.date(2016,a,b).weekday()]

#자릿수 더하기
def solution(n):
    return sum([int(i) for i in str(n)])

#정수 제곱근 판별
import math 
def solution(n):
    return (int(math.sqrt(n))+1)**2 if math.sqrt(n) == int(math.sqrt(n)) else -1

#제일 작은 수 제거하기
def solution(arr):
    t = min(arr)
    return [-1] if len(arr)<=1 else [i for i in arr if i != t]

#정수 내림차순으로 배치하기
def solution(n):
    return int("".join(sorted([i for i in str(n)],reverse=True)))

#list(str(n)) 이런식으로 해서 list 가 된다.


#이상한 문자 만들기
def solution(s):
    return " ".join([changeText(i) for i in s.split(" ")])

def changeText(text) :
    convertText = ""
    for i in  range(0,len(text)) :
        if i%2==0 :
            convertText += text[i].upper()
        else:
            convertText += text[i].lower()
    return convertText