學習總複習、寒假作業:

1-6 Python Input/Output

print('學習', 'Python', '真有事')
print('學習', 'Python', '真有事', sep='::')
print(30, end='Hello')

# 現在要練習Input
a = input('請輸入數字')
b = input('請再次輸入第2個數字')
ans = int(a) + int(b)
print('答案是',ans)

# chapter 2
#a = int(input())
a = int( '12345677' )
print( a + 999 )
# bol() False True
# int() 0 1 2 100 1999 -33
# float() 3.1415 2.7182 ..
# str() '單引號' "雙引號"
ans = type('12345')
print(ans)

# 2-4 字串
a = 'hello'
b = 'word'
print( a+b )
print( a*3 )
print( a[0], a[-1] )

a = list(map(int, '10 20 30'.split() ))
print(a)


print(a)
a = ['hello', 'world', 'very', 'good']
print( a[0]+a[1] )
print( '###'.join(a) )