程式大會考  108 008 進階題 從小到大排好
a = list(map(int, input().split() ))
 
 
a.sort()

for i in range(10-1, -1, -1):
    print(a[i], end=' ')