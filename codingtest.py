# # 1번째 문제  https://school.programmers.co.kr/learn/courses/30/lessons/181952
str = input()

print(str)


# 2번째 문제 https://school.programmers.co.kr/learn/courses/30/lessons/181944

a = int(input())

if a % 2 == 0:
    print(f'{a} is even')
else:
print(f'{a} is odd')


# 문제 3 https://school.programmers.co.kr/learn/courses/30/lessons/181937

def solution(num, n):
    if num % n == 0:
        return 1
    else:
        return 0


print(solution(33, 3))


# 문제 4 https://school.programmers.co.kr/learn/courses/30/lessons/181941

def solution(arr):
    return ''.join(arr)

# 문제 5 https://school.programmers.co.kr/learn/courses/30/lessons/181848


def solution(n_str):
    return int(n_str)

# 문제 6 https://school.programmers.co.kr/learn/courses/30/lessons/181936


def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0

# 문제 7 https://school.programmers.co.kr/learn/courses/30/lessons/181840?language=python3


def solution(num_list, n):
    if n in num_list:
        return 1
    else:
        return 0


# 문제 8 https://school.programmers.co.kr/learn/courses/30/lessons/181876?language=python3

def solution(myString):
    return myString.lower()

# 문제 9 https://school.programmers.co.kr/learn/courses/30/lessons/181877


def solution(myString):
    return myString.upper()


# 문제 10  https://school.programmers.co.kr/learn/courses/30/lessons/181929

def solution(num_list):
    list_sum = 0
    total = 1
    for i in num_list:
        list_sum += i
        total *= i
    if total < list_sum ** 2:
        return 1
    else:
        return 0

# 문제 11 https://school.programmers.co.kr/learn/courses/30/lessons/181850


def solution(flo):
    return int(flo)

# 문제 12 https://school.programmers.co.kr/learn/courses/30/lessons/181845


def solution(n):
    return str(n)

# 문제 13 https://school.programmers.co.kr/learn/courses/30/lessons/181933
# flag의 Ture , Flase는 따로 정해주는거


def solution(a, b, flag):
    if flag:
        return a + b
    else:
        return a - b

# 문제 14 https://school.programmers.co.kr/learn/courses/30/lessons/181879


def solution(num_list):
    total = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for i in num_list:
            total *= i
        return total

# 문제 15 https://school.programmers.co.kr/learn/courses/30/lessons/181835
# 너무 시간 잡아 먹음... 아흐 그래도 계속 고민하고 고민해서 만드는것. 리스트를 생성해야 하는 것에 대해서 생각해님


def solution(arr, k):
    if k % 2 == 0:
        answer = [i + k for i in arr]
    else:
        answer = [i * k for i in arr]

    return answer


def solution(arr, k):
    answer = []
    if k % 2 != 0:
        for i in arr:
            answer.append(k*i)
    else:
        for i in arr:
            answer.append(i+k)
    return answer


def solution(arr, k):
    if k % 2 != 0:
        return list(map(lambda x: x * k, arr))

    return list(map(lambda x: x + k, arr))

# 문제 16 https://school.programmers.co.kr/learn/courses/30/lessons/181940


def solution(my_string, k):
    return my_string * k

# 문제 17 https://school.programmers.co.kr/learn/courses/30/lessons/181889


def solution(num_list, n):
    return num_list[:n]

# 문제 18 https://school.programmers.co.kr/learn/courses/30/lessons/181910


def solution(my_string, n):
    return my_string[-n:]

# 문제 19 https://school.programmers.co.kr/learn/courses/30/lessons/181907


def solution(my_string, n):
    return my_string[:n]

# 문제 20 https://school.programmers.co.kr/learn/courses/30/lessons/181896
# return 하는 것을 잘 생각해야 한다. 꼭 다시보기!


def solution(num_list):
    for i in num_list:
        if i < 0:
            return num_list.index(i)
    return -1
