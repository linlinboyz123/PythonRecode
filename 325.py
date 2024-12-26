x = {'name': 'Grace', 'age': 26}
print(x.keys())  # 顯示字典當中key的值，return一個值，可以在Loop做使用
print(x.values())  # 顯示字典當中value的值，return一個值，可以在Loop做使用
print(x.items())  # 字典裡的key值跟value值分別用一個大字典包起來

# 在python當中的字典，在被存到我們電腦Ram的時候，都經過了特殊的步驟，他會經過hashed
# python裡面的字典不會因為資料量大，所以就變得難找
