name = "linlinboyz"
print(name.replace("boyz", "Toyz"))  # 把變數裡的值替化成你指定的值，第一個是你在變數裡要替換的值，第二個為新替換的值

sentence = "Today is a good day."
print(sentence.split(" "))  # 他可以分開字串的值，並把他們分別加入list(列表)裡面
print(list(sentence))  # list可以把變數裡的每個字都變成一個獨立的字串，可用在專題!

test = "I have the dream {} {} {}".format(
    "it is a videogamer", "This is True", "not a lie")
# 在format括號裡面的值，會顯示在大括號裡面，可以有多個括號，且他有索引值，可以改變順序，format2k6的好處是就不用再轉型別
print(test)

today = "Sunday"
emotion = "Happy"
print(f"today is a {today} so my emtion is {emotion} ")  # f""的用法是format的精簡版
