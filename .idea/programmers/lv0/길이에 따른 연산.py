# https://school.programmers.co.kr/learn/courses/30/lessons/181879

def solution(num_list):
    if len(num_list) <= 10:
        a = 1;
        for i in num_list:
            a *= i
        return a
    else:
        return sum(num_list)