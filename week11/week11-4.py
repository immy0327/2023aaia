程式會考:

計算餘數及列印
x, y= list(map(int, input().split() ))
# a[0] becomes x
# a[1] becomes y


print( 'Enter two numbers: The remainder is' , x % y )


判別正方形  # 要小心空格和跳行c和格式， it前面有兩個空格!
x, y = list(map(int, input().split() ))

if x==y:
    print( 'Enter two numbers:  It is a square ' , end='')
else:
    print( 'Enter two numbers:  It is not a square ' , end='')