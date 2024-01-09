SOIT106_BASE_004：基礎題：計程車資計算
a = int(input())
if a<=2000: ans = 100
else: 
    ans = 100+(a-2000)//500*5
    if (2-2000)%500>0: ans += 5
print(ans)