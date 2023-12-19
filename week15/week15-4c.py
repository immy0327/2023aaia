程式大會考  108 004 進階題 求11+22+33+....+n
a = int(input())
ans = 0
for i in range(1,a+1):
    ans += i*10+i
print(ans, end='')