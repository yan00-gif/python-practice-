# -*- coding: utf-8 -*-
"""0501.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kWjmYiqdHeN2ao0m--dOOGk6WKfxYil9
"""

firstNUM=20
secondNUM=6

ans=firstNUM / secondNUM
print(ans)
#ans = firstNUM % secondNUM



# 字符串 (string)
name = "Ray"
print(name)

name2 = "Liu"
print(name + name2)

# 數字 (number)
age = 16
print(age)

# 布爾值 (boolean)
is_student = True
print(is_student)

# 列表  (list)
scores = [90, 80, 70, 85]
print(scores)

# 字典 (dictionary)
grades = {
    'Math': 90,
    'English': 80,
    'Physics': 70,
    'Chemistry': 85
}
print(grades)

def wordTransForm(string1, string2):
    return string1.upper() + string2.upper()

# 測試範例
result = wordTransForm("hello", "world")
print(result)

zoo_animals = ["Dog", "Cat", "Bird", "Tiger", "Elephant"]

for animal in zoo_animals:
    print(animal)

import nltk
nltk.download('book')  # 下載書籍

from nltk.book import *  # 載入書籍

# 查找 "whale" 出現在原文中的句子
text1.concordance("whale")

# 看看跟 "ship" 類似語境的字
text1.similar("ship")

# 計算 "whale" 出現幾次
print(text1.count("whale"))

animal1 = "cat"
animal2 = "dog"
print(animal1 + " & " + animal2)

b = "apple
if b ="apple":
  print ()