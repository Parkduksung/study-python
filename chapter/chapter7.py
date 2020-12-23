
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


target = request.urlopen("https://naver.com") 
output = target.read()

print(output)