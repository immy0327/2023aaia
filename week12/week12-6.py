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
#上面都是week12-5

def gcd(a, b):
  print(a, b)
  if a==0: return b
  if b==0: return a
  return gcd(b, a%b)

a = 150000000
b = 200000000
print( gcd(a, b) )
# 有三種方法

程式大會考
最大公因數(2數)
a, b = list(map(int, input().split() ))

if a<0: a = -a
if b<0: b = -b

ans = 0
for i in range(1, a+1):
    if a%i==0 and b%i==0:
        ans = i
        
print(ans, end='')

第二種方法
def gcd(a, b):
  if a==0: return b
  if b==0: return a
  return gcd(b, a%b)
  
a, b = list(map(int, input().split() ))

if a<0: a = -a
if b<0: b = -b

print( gcd(a, b), end='' )