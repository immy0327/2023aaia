程式大會考 判斷迴文 107 進階 014 奇數之和
N = int(input())
ans = 0

for i in range(1,N+1):
    if i%2==1: ans += i
        
print(ans, end='')