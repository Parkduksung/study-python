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


list_a = [0,1,2,3,4,5,6,7]

list_a.extend(list_a)
print(list_a)
list_a.append(10)
print(list_a)
list_a.insert(3,0)
print(list_a)
list_a.remove(3)
print(list_a)
list_a.pop(3)
print(list_a)
list_a.clear()