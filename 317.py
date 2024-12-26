test = "you girl is so hot"
print(len(test))  # 回傳總長度

name = "Linlinboyz"
print(name.upper())  # 物件導向的意思是指每一個資料類型都可以是一個物件，那妳可以用物件的一些方法來調整這個物件，例如upper全部變大寫
print(name.lower())  # python的method只是暫時改變那個變數，如果你要永久改變的話需要把它存進一個變數裡，全部變小寫
print(name.upper().isupper())
# 可以method再加method，isupper()是確認你有沒有大寫，如果有的話回傳True
print(name.index("b"))  # 找到這個值在索引值的哪個位置
