因數整除
a = 120
# 1 2 3 4 5 6 10 12 15 ... for迴圈
ans = 0 # 迴圈前面,ans是0
for i in range(a+1): # 包含1....a本身
  if a%1==0:
    print( i, end=' ')
    ans += 1 # # 迴圈前面,ans增加
print('有幾個整除? ', ans) # 迴圈後面,把ans拿出來