a = 1000000000
b = 2000000000
ans = 0
for i in range(1, a+1):
  if a%i==0 and b%i==0:
    print( i, '有整除' )
    ans = i
print(ans, '是最大公因數')
# 很慢


a = 150000000
b = 200000000
c = a%b
print(a, b ,c)
while c!=0:
  a = b
  b = c
  c = a%b
  print(a, b, c)
print(b)
# 比較快