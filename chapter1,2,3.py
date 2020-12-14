# chapter1,2,3,4,5 확인문제.

#--------------chapter 1-----------------
#   1-1번
print("Hello Python")


#--------------chapter 2-----------------

print("# 연습문제")
print("\\\\\\\\")   # \ 4개만 나옴.
print("-" * 8)      # - 8번 찍힘.

print("abcde"[1])   # b
print("abcde"[1:])   # bcde
print("abcde"[1:2])   # b
print("abcde"[:1])   # a
print("abcde"[:4])   # a

print(4**4)          # 제곱연산자. 4의 4승임.
print(4,"*",4,"=",4*4)       # 16
print(2+2-2*2/2*2)   # 0


str_input1 = input("숫자 입력>")
num_input1 = float(str_input1)

print()
print(num_input1, "inch")
print(num_input1 * 2.54, "cm")

str_input1 = input("원의 반지름 입력>")
num_input1 = float(str_input1)

print()
print("반지름", str_input1)
print("둘레", 2*3.14*str_input1)
print("넓이", 3.14 * str_input1**2)

a = "abcd"
b = "dcba"

print(a,b)

# swap
tmp = a
a = b
b = tmp

print(a,b)


a = "1 2 3 4 5 6".split(" ")
print(a)


num1 = input("입력해봐 숫자 > ")



last_num = int(num1)

if last_num == 0 :
    print("o")
else:
    print("x")

# \ 를 써서 줄바꿈해준다.
if int(num1) == 0 \
    or num1 == 2 \
    or num1 == 4 \
    or num1 == 6 \
    or num1 == 8 : 
    print("0")
else:
    print("x")

if str(num1) in "02468" :
    print("o")
else:
    print("x")




