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