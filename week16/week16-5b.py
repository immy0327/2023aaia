程式大會考 判斷迴文 108 進階 014 計算級數的值
a = int(input())
ans = 0
for i in range(1, 2*a+1+1, 2):
    ans += i
print(f'f({a})={ans}', end=''