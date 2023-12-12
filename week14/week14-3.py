程式大會考  進階題  大小寫轉換
a = input()
for c in a:
    if c>='a' and c<='z':
        print( c.upper(), end='' )
    elif c>='A' and c<='Z':
        print( c.lower(), end='' )
    else:
        print( c , end='')
print()

# 第2種方法
a = input()
print( a. swapcase() )