#k번째 수

array = [1,5,2,6,3,7,4]
commands = [[2,5,3], [4,4,1], [1,7,3]]



def solution(array, commands):
    answer = []
    for num in commands:
        answer.append(sorted(array[num[0]-1:num[1]])[num[2]-1])
    return answer

print(solution(array,commands))