# # 1번째 문제  https://school.programmers.co.kr/learn/courses/30/lessons/181952
str = input()

print(str)


# 2번째 문제 https://school.programmers.co.kr/learn/courses/30/lessons/181944

a = int(input())

if a % 2 == 0:
    print(f'{a} is even')
else:
    print f'{a} is odd')


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
    list_sum=0
    total=1
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
    total=1
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
        answer=[i + k for i in arr]
    else:
        answer=[i * k for i in arr]

    return answer


def solution(arr, k):
    answer=[]
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


# 문제 21 https://school.programmers.co.kr/learn/courses/30/lessons/181849
# 한번더 생각해보기 '123455' 이걸 리스트로 만들면 '1','2','3' 이런씩으로 된다는걸 왜 까먹었을까.. 사소한건데 ㅠ
def solution(num_str):
    return sum(int(n) for n in num_str)


def solution(num_str):
    return sum(map(int, list(num_str)))


def solution(num_str):
    answer=0
    for i in num_str:
        answer += int(i)
    return answer

# 문제 22 https://school.programmers.co.kr/learn/courses/30/lessons/181853


def solution(num_list):
    return sorted(num_list)[:5]


# 문제 23 https://school.programmers.co.kr/learn/courses/30/lessons/181951
# 다시한번 확인하기
a, b=map(int, input().split())
print("a =", a)
print("b =", b)

# 문제 24 https://school.programmers.co.kr/learn/courses/30/lessons/181843


def solution(my_string, target):
    if target in my_string:
        return 1
    else:
        return 0

# 문제 25 https://school.programmers.co.kr/learn/courses/30/lessons/181839


def solution(a, b):
    if a % 2 == 1 and b % 2 == 1:
        return a ** 2 + b ** 2
    elif a % 2 == 1 or b % 2 == 1:
        return 2 * (a + b)
    else:
        return abs(a - b)

# 문제 26 https://school.programmers.co.kr/learn/courses/30/lessons/181863


def solution(rny_string):
    return rny_string.replace('m', 'rn')

# 문제 27 https://school.programmers.co.kr/learn/courses/30/lessons/181930


def solution(a, b, c):
    if a != b and b != c and a != c:
        return a + b + c
    elif a == b and a != c:
        return (a + b + c) * (a**2 + b**2 + c**2)
    elif a == c and b != c:
        return (a + b + c) * (a**2 + b**2 + c**2)
    elif b == c and a != c:
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)

# 문제 28 https://school.programmers.co.kr/learn/courses/30/lessons/181869


def solution(my_string):
    words=my_string.split()
    return words

# 문제 29 https://school.programmers.co.kr/learn/courses/30/lessons/181939


def solution(a, b):

    if int(str(a) + str(b)) >= int(str(b) + str(a)):
        return int(str(a) + str(b))
    else:
        return int(str(b) + str(a))

# 문제 30 https://school.programmers.co.kr/learn/courses/30/lessons/181926
# 아예모르겠음.. control은 어찌하라는 거징..
# 이렇게 생각하는거구나.... 가릿!
def solution(n, control):
    for c in control:
        if c == 'w':
            n += 1
        elif c == 's':
            n -= 1
        elif c == 'd':
            n += 10
        elif c == 'a':
            n -= 10

    return n


# 문제31 https://school.programmers.co.kr/learn/courses/30/lessons/181906
# 아에 처음부터 확인하는 메서드가 있었구나..
def solution(my_string, is_prefix):
    if my_string.startswith(is_prefix):
        return 1
    else:
        return 0

def solution(my_string, is_prefix):
    if my_string[:len(is_prefix)] == is_prefix:
        return 1
    else:
        return 0

import re

text="Hello, World!"
pattern=r"World"
match=re.search(pattern, text)
if match:
    index=match.start()
    print(index)  # 출력: 7

# 문제 32 https://school.programmers.co.kr/learn/courses/30/lessons/181908
# 기억하자 뒤에서부터는 이렇게 진행된다는걸
def solution(my_string, is_suffix):
    if my_string[-len(is_suffix):] == is_suffix: return 1
    return 0

# 문제 33 https://school.programmers.co.kr/learn/courses/30/lessons/181905
# 뒤집기 잘 생각하자.
# 문자열 my_string에서 인덱스 s부터 인덱스 e까지의 부분 문자열을 슬라이싱하여 가져옵니다. 이때, [::-1]을 사용하여 문자열을 뒤집습니다.
def solution(my_string, s, e):
    answer=my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return answer

def solution(my_string, s, e):
    substr=reversed(list(my_string[s:e+1]))
    return my_string[:s] + ''.join(substr) + my_string[e+1:]

# 문제 34 https://school.programmers.co.kr/learn/courses/30/lessons/181927?language=python3
# append를 return에 append로 해버리면 none이 나와버림.
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1] * 2)

    return num_list

# 문제 35 https://school.programmers.co.kr/learn/courses/30/lessons/181949
# 무진장 어려웠는데 왜 1점밖에 안주는지.. 모르겠지만.. 머... 풀었으니 만족해야지
# input 할때 항상 기억하자..
str=input()

def solution(str):
    result=''
    for i in str:
        if i.islower():
            result += i.upper()
        elif i.isupper():
            result += i.lower()
        else:
            result += i
    return result

output_str=solution(str)
print(output_str)
# 미친 이렇게 푸는 것도 있었어..
print(input().swapcase())
# 이런풀이도.. 왜이렇게 어렵게 생각했을까~~
str=input()
a=''

for s in str:
    if (s.isupper()):
        a=a + s.lower()
    else:
        a=a + s.upper()

print(a)

# 문제 36 https://school.programmers.co.kr/learn/courses/30/lessons/181948

print('!@#$%^&*(\\\'\"<>?:;')

# 문제 37 https://school.programmers.co.kr/learn/courses/30/lessons/181902
def solution(my_string):
    answer=[0]*52
    for x in my_string:
        if x.isupper():
            answer[ord(x)-65] += 1
        else:
            answer[ord(x)-71] += 1
    return answer
# 미친 배우자. ord는 유니코드로 각 자리에 추가하는것을 말한다... 기억하자.

# 문제 38 https://school.programmers.co.kr/learn/courses/30/lessons/181904

def solution(my_string, m, c):
    result=''
    for i in range(c-1, len(my_string), m):
        result += my_string[i]
    return result
# 어이가 없구만ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 이렇게 쉽게 풀리는걸.. 그래 최대한.. 쉽게 생각하는걸로 하자..
def solution(my_string, m, c):
    return my_string[c-1::m]

# 문제 39 https://school.programmers.co.kr/learn/courses/30/lessons/181950

a, n=input().strip().split(' ')
n=int(n)

result=a * n
print(result)


# 문제 40 https://school.programmers.co.kr/learn/courses/30/lessons/181947

a, b=map(int, input().strip().split())

c=a + b
print(f"{a} + {b} = {c}")

# 문제 41 https://school.programmers.co.kr/learn/courses/30/lessons/181920

def solution(start, end):
    num_list=[]
    for num in range(start, end + 1):
        num_list.append(num)
    return num_list

def solution(start, end):
    return list(range(start, end + 1))

# 문제 42 https://school.programmers.co.kr/learn/courses/30/lessons/181852

def solution(num_list):
    sorted_num=sorted(num_list)
    answer=sorted_num[5:]
    return answer

def solution(num_list):
    num_list.sort()
    answer=num_list[5:]
    return answer

def solution(num_list):
    return sorted(num_list)[5:]

# 문제 43 https://school.programmers.co.kr/learn/courses/30/lessons/181873

def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())


def solution(my_string, alp):
    return my_string.replace(alp, alp.swapcase())

def solution(my_string, alp):
    answer=''
    for i in my_string:
        if i == alp:
            answer += i.upper()
        else:
            answer += i
    return answer

# 문제 44 https://school.programmers.co.kr/learn/courses/30/lessons/181874
# 넘 어렵다.. 이런 ㅠ

못품.. 다시

# 문제 45 https://school.programmers.co.kr/learn/courses/30/lessons/120850

def solution(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))



def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])

def solution(my_string):
    result=[]

    for i in my_string:
        if i.isdigit():
            result.append(int(i))

    return sorted(result)

# 문제 46  https://school.programmers.co.kr/learn/courses/30/lessons/181928

def solution(num_list):
    odd_sum=""
    even_sum=""

    for num in num_list:
        if num % 2 == 0:
            even_sum += str(num)
        else:
            odd_sum += str(num)

    return int(odd_sum) + int(even_sum)


# 문제 47

def solution(n):
    if n % 2 == 1:
        odd_sum=sum(range(1, n+1, 2))
        return odd_sum
    else:
        even_sum=sum([i**2 for i in range(2, n+1, 2)])
        return even_sum


# 문제 48 https://school.programmers.co.kr/learn/courses/30/lessons/181942

def solution(str1, str2):
    sum_str=''

    for i in range(len(str1)):
        sum_str += str1[i] + str2[i]

    return sum_str

# 문제 49 https://school.programmers.co.kr/learn/courses/30/lessons/181914

def solution(number):
    number_sum=0
    for digit in str(number):
        number_sum += int(digit)
    remainder=number_sum % 9
    return remainder
