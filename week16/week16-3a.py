程式大會考 判斷迴文 107 進階 006

a = input()
N = len(a)
for i in range(N):
    if a[i] != '2':
        print(a[i], end='')
print()

程式大會考 判斷迴文 107 進階 010
a = input()
N = len(a)
bad = 0 # not bad
for i in range(N):
    if a[i] != a[N-1-i]:
        bad = 1 # bad!!
if bad==0: print('YES', end='')
else: print('NO', end='')

程式大會考 判斷迴文 107 進階 014 奇數之和
N = int(input())
ans = 0

for i in range(1,N+1):
    if i%2==1: ans += i
        
print(ans, end='')

程式大會考 判斷迴文 107 進階 015 兩數之間可被7整除的數
a,b = list(map(int, input().split() ))

for i in range(a, b+1):
    if i%7==0:
       print(i, end=' ')
       
       
程式大會考 判斷迴文 107 進階 016 數字之和
a = list(map(int, input().split() ))
N = len(a)
print(N-1, end='')