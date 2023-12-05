程式大會考
輸入整數反序列印
a = list(map(int, input().split() ))

N = len(a)-1

for i in range(N-1, -1, -1):
    print(a[i], end=' ')
    
print()