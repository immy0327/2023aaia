SOIT108_Advance_007：進階題：區間測速-超速之王
a = list(map(int, input().split() ))
feat = min(a)
for i in range(len(a)):
    if a[i]==feat:
       ansI = i + 1
       break
    
print( ansI, int(1.2*60*60/feat) )