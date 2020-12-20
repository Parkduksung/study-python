#chapter4,5


array = [244,32,103,"문자열", True , False]

print(array[-1])

array[0] ="211"

print(array[0])

array1 = [[1,2],
         [3,4]]

array2 = [[1,3],
         [4,3]]



print(array1+array2)
print(array1[0])
print(array1[0][1])

print(len(array1))

array1.append(123)
print(array1)

array1[0].insert(0,10)
print(array1)

array1.insert(0,10)
print(array1)

array1.extend(array2)

print(array1)

del array1[-1]

print(array1)

array1.pop(-1)

print(array1)

print(10 in array1)

print(10 in array1[1])

print(10 in array1[2])

print(10 not in array1[2])


# 0 - 99 까지 출력됨.
for i in range(100) :
    print(i)


for i in array1 : 
    print(i)



#4-1장 문제

numbers = [273,103,5,32,65,9,72,800,90]

for num in numbers :
    if num >=100 :
        print(num)


for num in numbers :
    if num %2 == 0 :
        print("0" , num)
    else:
        print("1" , num)


# 요거 좀 다양하게 나올수도. 형변환은 중요함.
print(len(numbers))
for num in numbers :
    print("num : ", len(str(num)))


list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9],
]

for x in list_of_list : 
    for y in x :
        print(y)


numbers = [1,2,3,4,5,6,7,8,9]
output = [[], [], []]

for num in numbers :
    output[num%3-1].append(num)

print(output)


star = "*"

for i in range(5) :
    print(star)
    star += "*"


# 먼가 mutableMap 이랑 느낌이 비슷함.


dictinory = {
    "name" : "duksung",
    "height" : 186,
    "age" : 29,
    "height" : "188",
    "like" : ["exercise", "eat food", "coding" , "drinkding"]
}

print(dictinory["name"])
print(dictinory["age"])
print(dictinory["height"])
print(dictinory["like"][1])



del dictinory["name"]
del dictinory["like"]

dictinory["title"] = 1

for key in dictinory : 
    print(dictinory[key])

#4-2 연습문제

pets = [
    {"name" : "a" , "age" : 5},
    {"name" : "b" , "age" : 6},
    {"name" : "c" , "age" : 7},
    {"name" : "d" , "age" : 8}
]

for key in pets:
    print(key["name"],key["age"])


#3번 모르겠음 다시푸셈. 풀긴했는데 나오는 키 순서가 좀 다른디..
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter ={}

for x in numbers :
    sum = 0
    for y in numbers :
        if x == y :
            sum +=1 
    counter[str(x)] = sum

print(counter)

char = {
    "name" : "kisa",
    "level" : 12,
    "items" : {
        "sword" : "fire sword",
        "armor" : "plate"
    },
    "skill" : ["t", "k", "o"]
}

# int, str 구분하려고 한건데 else 로 하나로 묶어도 될듯...
for key in char :
    if type(char[key]) is dict :
        for x in char[key] :
            print(x, ":" , char[key][x])
    elif type(char[key]) is list :
        for x in char[key] :
            print(key, ":" , x)
    elif type(char[key]) is str :
        print(key, ":", char[key])
    else :
        print(key, ":", char[key])
    

key_list = ["name" , "hp" , "mp", "level" ]
value_list = ["gisa", 200, 30, 5]
t = {}

if len(key_list) == len(value_list) :
    for i in range(0, len(key_list)) : 
        t[key_list[i]] = value_list[i]

print(t)

limit = 10000
i=1

sum_value = 0

while sum_value < limit :
    sum_value += i
    i+=1

print("{} {} {}".format(i-1,limit,sum_value))


max_value = 0
a = 0
b = 0

for i in range(1,100) :
    j = 100 - i
    if max_value < i*j :
        max_value = i*j
        a = i
        b = j

print("{} {} {}".format(a,b,max_value))



print("{:b}".format(6))
print(int("110",2))

output = ["{:b}".format(i).count('0') == 1 for i in range(1,101)]

output = [i for i in range(1,101)
    if "{:b}".format(i).count('0') == 1]

print(output)