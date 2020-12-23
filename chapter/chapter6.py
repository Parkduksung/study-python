
list_input_a = ["52","273","32","스파이","103"]

list_number = []

for i in list_input_a :
    try :
        list_number.append(int(i))
    except :
        pass

#아래에서 else,finally 제외 가능하다. 
# try :
#     예외가 발생할 가능성 코드
# except :
#     예외 발생했을때 실행할 코드
# else :
#     예외가 발생하지 않았을 때 실행할 코드
# finally :
#     무조건 실행할 코드

try:
    pass   
except expression as identifier:
    pass
else:
    pass
finally:
    pass

print(list_number)

#6-1 연습문제.

numbers= [52,273,32,103,90,10,275]

number = 10000

try :
    print("{} {}".format(number, numbers.index(number)))
except :
    print("내부없음")


# 6-2 에서 굳이 valueException 이런거 할필요가잇음?? 그냥 Exception 떨어지면 log 나 메세지로 어떤 error 떴는지만 보여주면 되지않나..?
#그리고 raise 는 비동기에서도 좋을려나....? tensorflow 는 학습시키는거에 취중되는건데 머 거기서 많은 신경망들이 구현되어 있어도 예외는 항상 발생하니 필요는 하겠다만... 
#모르겠음 raise 가 실제 서비스에서 어떻게 사용될지는...