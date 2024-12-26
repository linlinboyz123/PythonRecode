myString = "Hello"
print(myString[-1])
print(myString[-2])
print(myString[-3])
print(myString[-4])
print(myString[-5])
# 負的索引值是從-1開始算起的，因此想要找出作後一個字可以用索引值-1來找

y = "12345678"
print(y[2:6])  # 字串切割，第一個索引值包含他本身，第二個不包含，因此會出現3~6
print(y[::-1])  # 反轉用法，不寫索引值他會都跑一次，最後一個是一次跑幾格，-1代表從尾跑到頭
