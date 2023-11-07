a = [1, 3, 5, 7, 9, 11, 13, 15, 17,]
N = len(a)
for i in range(N-1):
  d = a[1] - a[0] # 基礎的差距
  if a[i+1] - a[i] != d:
    print('出錯了')





a = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]
N = len(a)
print(a) #使用前
for i in range(N-1):
  if a[i+1] < a[i]:
    a[i], a[i+1] = a[i+1], a[i]
print(a) #使用後