# 剝皮法 week08-4
a = 1234
ans = 0 # 答案,要把你剝下來,慢慢塞進去
while a>0:
  ans = ans * 10 + a%10
  print('現在的a是', a, '剝出來的皮%10是', a%10, '現在的 ans 就變成', ans)
  a = a // 10