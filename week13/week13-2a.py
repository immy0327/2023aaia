Fibonacci 費氏數列
a = [1, 1]
for i in range(2,100):
  a.append( a[i-1] + a[i-2] )
print(a)



#way2:

a = [0]*100 # 有100格,每隔都是0
a[0] = 1
a[1] = 1
for i in range(2,100):
  a[i] = a[i-1] + a[i-2]
print(a)