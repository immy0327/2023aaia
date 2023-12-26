程式大會考 判斷迴文 108 進階 014B 拆解輸入的正整數
a = int(input())

ten = 1
while a>0:
   now = a%10 * ten
   print(now, end=' ')
   a = a//10
   ten = ten *10