程式大會考

正整數平方總和
a = int(input())

ans = 0
for i in range(1,a+1):
    ans += i*i
    
print(ans, end='')