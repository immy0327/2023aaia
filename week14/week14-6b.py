程式大會考  進階題 2位數轉10位數
a = int(input())

b = a%10
c = a//10%10
d = a//100%10
e = a//1000%10

print( b*1+ c*2 + d*4 + e*8)