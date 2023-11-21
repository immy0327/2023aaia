程式會考:

分開整數的每個數
 #sep='   '中間有三格空格
 #end=''結束不要有跳行
 a = input()

print( a[0], a[1], a[2], a[3], a[4] , sep='   ', end='' )

我們與惡的距離
a = int(input())

if a-2 >0:
	print( a-2 , end = '' )
else:
    print( 2-a , end = '' )