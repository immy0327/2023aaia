最大公因數
a = 57
b = 76
ans = 0
for i in range(1, a+1):
  if a%i==0 and b%i==0:
    print( i, '有整除' )
    ans = i
print(ans, '是最大公因數')


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