MyList = ["one", "two", "Three"]  # 列表就像把所有類型的書本都塞進同一個書櫃，再根據書櫃的位置分類書本的類型
HeList = ["A", "B", "C"]  # 基本上可以套用在字串的用法都可以用在列表
print(f"{MyList[0]} {MyList[1]} {MyList[2]} esay to do ra me")
print(f"{HeList[0:3]} esay to {MyList[0:3]}")
print(MyList + HeList)  # 列表可以做相加，裡面的元素就會連起來

x = [1, 2, 1]
x[1] = 10  # 字串不能做索引值裡面的替換，但是列表可以! 列表可以! 列表可以!，重要說三次
print(x)
