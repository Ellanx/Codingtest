# 문제 1 https://school.programmers.co.kr/learn/courses/30/lessons/12951
# 틀림  다시 해봐야함 결과는 맞는데 테스틑 틀리다고 나옴

def solution(s):
    answer = ''
    words = s.split()  # 문자열을 공백을 기준으로 단어로 분리
    
    for i in range(len(words)):
        if words[i][0].isalpha():  # 단어의 첫 문자가 알파벳인 경우
            words[i] = words[i][0].upper() + words[i][1:].lower()  # 첫 문자는 대문자, 나머지는 소문자로 변환
        else:
            words[i] = words[i].lower()  # 첫 문자가 알파벳이 아닌 경우, 모두 소문자로 변환
        
    answer = ' '.join(words)  # 단어들을 다시 공백으로 연결하여 문자열로 변환
    return answer

# 문제 2 https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    fib = [0, 1]  
    
    for i in range(2, n+1):
        fib.append((fib[i-1] + fib[i-2]) % 1234567) 
    
    return fib[n] 

def fibonacci(num):
    answer=[0,1]
    for i in range(2,num+1):
        answer.append(answer[i-1]+answer[i-2])
    return answer[-1]
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))
