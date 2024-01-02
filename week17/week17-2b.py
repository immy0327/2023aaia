
SOIT107_ADVANCE_012：進階題：星星等腰三角 
a = int(input())

for i in range(a):
    space = a-1 - i
    for k in range(space):
        print(' ',end='')
        
    star = i*2 + 1
    for k in range(star):
        print('*', end='')
    print()
    
SOIT107_Base_010：基礎題：平年月份的天數
a = int(input())
days = [0, 31,28,31,30,31,30,31, 31,30,31,30,31]

print( days[a], end='' )

SOIT107_Base_011：基礎題：整數二元四則運算
a, c, b = input().split()
a = int(a)
b = int(b)
if c=='+': ans = a+b
if c=='-': ans = a-b
if c=='*': ans = a*b
if c=='/': ans = a//b
print(ans, end='')
