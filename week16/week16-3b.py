程式大會考 判斷迴文 107 進階 010
a = input()
N = len(a)
bad = 0 # not bad
for i in range(N):
    if a[i] != a[N-1-i]:
        bad = 1 # bad!!
if bad==0: print('YES', end='')
else: print('NO', end='')