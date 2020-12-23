#7-1 은 from import as 만 알면 검색해서 사용하면 됨.
#그리고 나머지는 7-3의 패키지 만드는것만 실제로 적용하자. (나만의 함수들도 만들어서 쓸수 있음.)

import math

print(math.ceil(1.2))
print(round(1.5))
print(math.floor(1.8))



from math import floor, ceil

print(floor(1.7))
print(ceil(1.1))


import math as m

print(m.floor(1.7))


import os

print(os.name)


#time 은 delay 줄때 괜찮을듯.. (비동기에서 동기화 시킬때?)


import urllib as request

#html 소스 읽어오는구만..
target = request.urlopen("https://naver.com") 
output = target.read()

print(output)