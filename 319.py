myString = "Today is a good Good day"
print(myString.lower().count("good"))
# 抓取變數裡面重複的字有幾個，大小寫有差，如果要抓大寫需先在前面寫一個lower()

print(myString.find("fjoiewa"))  # 用法跟index一樣，回傳值的索引值，唯一不同的是如果找不到值會顯示-1
print(myString.startswith("T"))  # 開始是不是輸入的值，如果是就回傳True，不是則是Fasle
print(myString.startswith("y"))  # 結束是不是輸入的值，如果是就回傳True，不是則是Fasle
