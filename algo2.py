# print('Good moring')
#
# num = 1
# print(num)

# #数値型
# num01 = 123
# print(type(num01))
#
# #文字列
# string_a = "Hello"
# print(string_a)
#
# #ブール型
# a = 10
# b = 1
# bool01 = (a > b)
# print(bool01)

#リスト
# a = [["sato","suzuki"],["takahashi","tanaka"]]
# print(a[0][0])
# print(a[0][1])
# print(a[1][0])
# print(a[1][1])

#論理演算子
# x = 8
# y = 3
# print(x == 3 or y == 3)
# print(x == 1 or y == 1)

#代入演算子
# x = 8
# y = 12
# z = 20
#
# x += x + y
# print(x)

#条件分岐
# age = 22
#
# if age >= 20:
#     print("adult")
# else:
#     print("child")

# age = 0
#
# if age >= 20:
#     print("adult")
# elif age == 0:
#     print("baby")
# else:
#     print("child")

#繰り返し
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# for i in range(3):
#     for j in range(3):
#         print(i,j, sep="-")

#関数
# def number(gretting):
#     print(gretting)
#
# hello = number
# hello("goodmoring")

# def add(num1, num2, num3):
#     return(num1 + num2 + num3)/3
#
# dev_resoult = add(9, 4, 2)
# print(dev_resoult)

#クラス
# class Student():
#
#     def __init__(self,name):
#         self.name = name
#
#     def avg(self,math,english):
#         print((math + english)/2)
#
# a001 = Student("satou") #インスタンス化
# # a001.avg(80, 70)
# # a001.name = "sato"
# print(a001.name)
#
# a002 = Student("tanak")
# # a002.name = "tanaka"
# print(a002.name)se

class Student:

    def __init__(self,name):
        self.name = name

    def calculate_avg(self,date):
        sum = 0

        for num in date:
            sum += num

        avg = sum/len(date)
        return avg

    def jedge(self,avg):

        if(avg >= 60):
            result = "passed"
        else:
            result = "failed"
        return result

a001 = Student("sato")
date = [70,65,50,90,30]
avg = a001.calculate_avg(date)
result = a001.jedge(avg)

print(avg)
print(a001.name + " " + result)