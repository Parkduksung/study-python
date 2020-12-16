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

