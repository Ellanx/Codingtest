# 문제1 https://school.programmers.co.kr/learn/courses/30/lessons/12944

def solution(arr):
    return sum(arr) / len(arr)

# 문제 2 https://school.programmers.co.kr/learn/courses/30/lessons/12937

def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# 문제 3 https://school.programmers.co.kr/learn/courses/30/lessons/12931

def solution(N):
    digit_sum = 0
    for digit in str(N):
        digit_sum += int(digit)
    return digit_sum

# 문제 4 https://school.programmers.co.kr/learn/courses/30/lessons/12912

def adder(a, b):
    sum=0
    for i in range(min(a,b),max(a,b)+1):
        sum+=i
    return sum

print( adder(3, 5))

# 문제 5 https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    total_sum = 0

    for num in range(left, right + 1):
        divisor_count = 0
        
        for i in range(1, num + 1):
            if num % i == 0:
                divisor_count += 1
    
        if divisor_count % 2 == 0:
            total_sum += num
        else:
            total_sum -= num

    return total_sum


# 문제 6 https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    
    s = s.lower()
    
    p_count = s.count('p')
    y_count = s.count('y')
    
    return p_count == y_count

#문제 7 https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    count = 0  

    while num != 1:
        if num % 2 == 0:  
            num //= 2
        else: 
            num = num * 3 + 1
        
        count += 1

        if count == 500:  
            return -1

    return count

#문제 8 https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    x = 1  # 자연수 x 초기값 설정

    while True:
        if n % x == 1:  # n을 x로 나눈 나머지가 1인 경우
            return x
        
        x += 1


# 문제 9 https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    digit_sum = sum([int(digit) for digit in str(x)])  
    
    if x % digit_sum == 0:  
        return True
    else:
        return False