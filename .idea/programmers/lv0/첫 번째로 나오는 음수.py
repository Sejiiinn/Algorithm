# https://school.programmers.co.kr/learn/courses/30/lessons/181896

def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    else:
        return -1