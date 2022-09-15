import math


def CountSpecialsPairs_NT(x, y):
    count = 0

    for i in range(1, int(math.sqrt(x)) + 1):
        count+= max(0,min(y, int(x/i) - 1) - i)
    return count

n = int(input())
for i in range(n):
    s = input().split()
    x = int(s[0])
    y = int(s[1])
    print(CountSpecialsPairs_NT(x,y))

