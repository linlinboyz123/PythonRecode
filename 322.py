friends = ["Funein", "Roren", "reo", "KK"]
friends.insert(4, "leozn")  # 在列表插入元素，第一個值為要插入的位置，如果是4的話就是差在KK前面，第二個值為要插入的內容
friends.remove("reo")  # 在列表刪除元素
friends.clear()  # 清空所有列表的值，回傳空列表
print(friends)

FavorAnimal = ["monkey", "turtle", "cat", "dog"]
FavorAnimal.sort()  # 排列列表，英文由a為最優先排到z，數字則最小優先排到最大
FavorAnimal.reverse()  # 列表內容全部顛倒，變為由索引-1排在第一個
print(FavorAnimal)
