程式大會考

兩數之間的三倍整數
a, b = list(map(int, input().split() ))

ans = 0
for i in range(a, b+1):
    if i%3==0: ans += i