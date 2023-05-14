# 1번째

# 10 ~ 15 까지의 각 숫자의 개수를 구해보자
# 와.. 어찌 이렇게 짜지.. 대단하다..
import math
from collections import defaultdict
count = {x: 0 for x in range(0, 10)}

for x in range(1, 1001):
    for i in str(x):
        count[int(i)] += 1

print(count)

# 2번째

d = defaultdict(int)
for n in range(1, 1001):
    for x in str(n):
        d[x] += 1


# 주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.

# 이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌

names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌".split(
    ",")

# 1
a = [i[0] for i in names]
print("김씨 : %d\n이씨 : %d\n" % (a.count("김"), a.count("이")))

# 2
print(names.count("이재영"))

# 3
uniq_names = list(set(names))
print(uniq_names)

# 4
uniq_names.sort()
print(uniq_names)


# A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지수를 리턴하는 프로그램이 필요하다고 한다.

입력: 총건수(m), 한페이지에 보여줄 게시물수(n)(단 n은 1보다 크거나 같다. n >= 1)
출력: 총페이지수


m = int(input('총건수: '))
n = int(input('한페이지에 보여줄 게시물수: '))

print(math.ceil(m/n))


def page(m, n):
    page = m // n
    if m % n > 0:
        page += 1
    return page
