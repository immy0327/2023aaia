程式大會考  108 010 基礎題 水杯接水
a, b = list(map(int, input().split() ))

ans = a//b
if a%b>0: ans += 1

print(ans, end='')