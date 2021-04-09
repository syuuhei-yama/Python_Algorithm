# who = '猫'
# who = int(who)
# text = '我輩は'
# text = int(text)
#
# text += who
#
# print(text)

# s = abs(-3.7)
# print(s)
#
# a = min(2,9,21,-2,5)
# print(a)

# a = "ABCDEFG"
# s = a.count("A")
#  print(s)

# sum = 20 + 40 + 10
# limit = 100
#
# if sum >= limit:
#     result = '合格'
# else:
#     result = '不合格'
#     result += "/" + str(sum - limit)
#
# print(sum)
# print(result)

# from random import randint
# size = randint(5, 20)
# weight = randint(20, 40)
#
# if size >= 10:
#     if weight >= 25:
#         result = "合格"
#     else:
#         result = "不合格"
# else:
#     result = "不合格"
#
# text = f"サイズ{size},重量{weight}:{result}"
# print(text)

# point = randint(0,100)

# if point >= 80:
#     result = "Aクラス"
# elif point >= 60:
#     result = "Bクラス"
# elif point >= 30:
#     result = "Cクラス"
# else:
#     result = "不適合者"
#
# print(f"{point}点:{result}")

# name = ""
#
# if not name:
#     name = "匿名"
# print(name)

from random import randint
# a = randint(0,10)

# if num%2:
#     result = "奇数"
# else:
#
#     result = "偶数"
#
# print(num,result)

# if 5 <= a <= 8:
#     print(a,"合格")
# else:
#     print(a,"不合格")

# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# tikets = 5
# point = 0
# fmt = "{:>3}"
#
# while tikets>0:
#     v = randint(1,20)
#     print(fmt.format(v))
#     point += v
#     tikets -= 1
# print("-" * 3)
# print(fmt.format(point))

# while True:
#     a = randint(1, 13)
#     b = randint(1, 13)
#     c = randint(1, 13)
#
#     if (a+b+c) == 21:
#         break
# print(a,b,c)

# miss = 0 #間違えた数
# correct = 0 #正解数
# print('問題１！3回間違えたら終了。qで止める')
# while miss<3:
#     a = randint(1, 100)
#     b = randint(1, 100)
#     ans = a + b
#     #問題を出題し、キーボードからの入力待ちにする
#     question = f"{a} + {b}は？"
#     value = input(question)
#     #qを入力すると中断
#     if value == "q":
#         break
#
#     if value == str(ans):
#         correct += 1
#         print('正解です')
#     else:
#         miss += 1
#         print('間違い！',"✖️" * miss)
# print("-" * 20)
# print("正解:", correct)
# print('間違い:',miss)

# numbers = []
#
# while len(numbers) < 10:
#     n = randint(1, 100)
#     if n in numbers:
#         continue
#     numbers.append(n)
#
# print(numbers)


# numbers = []
#
# while len(numbers) < 10:
#     n = randint(-10, 90)
#     if n<0:
#         print("中断されました")
#         break
#     if n in numbers:
#         continue
#     numbers.append(n)
# else:
#     print(numbers)

# colors = ["blue",'pink',"green","red"]
#
# for name in colors:
#     print(name)

# for i in range(5, 10):
#     print(i)

# for i in range(3):
#     print("i =", i)
#     for j in range(2):
#         print(" ", "j= ", j)

# for i in range(4):
#     print()
#     for j in range(3):
#         x = j*2
#         y = i*3
#         print(f"({x}, {y})", end="")
# print()

# numlist = [3, 4.2, 10,"x",1,9]
# sum = 0
# for num in numlist:
#     if not isinstance(num, (int,float)):
#         print(num,"数値ではありません")
#         break
#     sum += num
#     print(num, "/", sum)

# for i in range(4):
#     for j in range(4):
#         if i<j:
#             print("." * j)
#             break
#         print(f"i={i},j={j}")

# numlist = [3, 4.2, 10,'x',1.9]
# sum = 0
#
# for num in numlist:
#
#     if not isinstance(num, (int, float)):
#         print(num,"数値ではありません")
#         continue
#     sum += num
#     print(num, "/",sum)

# numlist = [3, 4.2, 10,1,9]
# sum = 0
#
# for num in numlist:
#
#     if not isinstance(num, (int, float)):
#         print(num,"数値ではないものが含まれている")
#         break
#     sum += num
# else:
#     print("合計",sum)

# while True:
#     num = input("何個ですか？(qで終了)")
#     if num == "q":
#         print("終了しました")
#         break
#
#     try:
#         price = 120 * int(num)
#         print("金額",price)
#     except:
#         print("エラーです。正しく入力して下さい")

# num = 0
# try:
#     value = 120 / num
#     print(value)
# except:
#     print("エラーです")
# finally:
#     print("終わり")

# sum = 7600
# while True:
#     num = input("何人ですか？(qで終了)")
#     if num == "q":
#         break
#
#     try:
#         price = round(sum / int(num))
#         if price < 0:
#             continue
#         print("一人当たりの金額",price)
#     except ValueError:
#         print("数値を入れて下さい")
#     except ZeroDivisionError:
#         print("0以外の数値を入力して下さい")

# sum = 7600
# while True:
#     num = input("何人ですか？(qで終了)")
#     if num == "q":
#         print("終了します")
#         break
#     try:
#         price = round(sum / int(num))
#     except Exception as error:
#         print("エラーになりました")
#         print(error)
#     else:
#         if price < 0:
#             continue
#         print("一人当たりの金額",price)

#リスト
# data = [
#     11, 22, 33, 44, 55,
#     66,77,
#     88, 99, 100
# ]
# print(data)

# nums = [0]*10
# print(nums)
#
# strs = ["xy"]*5
# print(strs)
#
# result = [False]*5
# print(result)
#
# data = [1,2,3]
# s = data*5
# print(s)

#1/22
# thelist = list(range(-5, 6))
# print(thelist)
#
# evenlist = list(range(0, 10, 2))
# print(evenlist)
#
# oddlist = list(range(1,10,2))
# print(oddlist)
#
# list_x3 = list(range(0, 20, 3))
# print(list_x3)
#
# list_happy = list("happy")
# print(list_happy)
#
# week = list("日月火水木金土")
# print(week)
#
# newlist = list()
# print(newlist)

# colors = ["red","blue","grenn","yellow"]
# colors[2] = "block"
# print(colors)
#
# list_a = [["apple","peach","orenge"],["cabbage","carrot","potato"]]
# list_b = [[["p","y"],["t","h"]],[["o","n"],["3","note"]]]
#
# print(list_a[1][0])
# print(list_b[1][1][1])

# pos = int(input())
# colors = ["blue","red","green","yellow"]
# length = len(colors)
#
# if -length <= pos < length:
#     item = colors[pos]
#     print(item)
# else:
#     print("エラーになりました")

# pos = int(input())
# colors = ["blue","red","green","yellow"]
#
# try:
#     item = colors[pos]
#     print(item)
# except IndexError:
#     print("インデックスエラーになりました")
# except Exception as error:
#     print(error)

#リストに追加,挿入
# data = []
# data.append(10)
# data.append(20)
# print(data)
# data.append(30)
# print(data)

# data = ["a","b","c","d","e","f"]
# data.insert(3, "new")
# print(data)

# fruits = ["apple","orange","banana","peach"]
# dessert = fruits.pop()
# print(dessert)
# print(fruits)

# fruits = ["apple","orange","banana","peach"]
# dessert = fruits.pop(0)
# print(dessert)
# print(fruits)

# fruits = []
# dessert = fruits.pop(0)

# fruits = []
# if fruits :
#     dessert = fruits.pop()
#     print("デザートは" + dessert)
# else:
#     print(fruits)

# fruits = []
# try:
#     dessert = fruits.pop()
#     print("デザートは" + dessert)
#     print(fruits)
# except:
#     print("エラーになりました")

# colors = ["blue","red","yellow","red","green"]
# print("削除前",colors)
# target = "yellow"
#
# if target in colors:
#     colors.remove(target)
# print("削除後",colors)

# colors = ["blue","red","yellow","red","green"]
# print("削除前",colors)
# target = "red"
#
# while target in colors:
#     colors.remove(target)
# print("削除後",colors)

#split

# message = "may the force be with you !"
# words = message.split()
# print(words)

# fruits = "apple, orange, banana, mango"
# fruits_list = fruits.split(", ")
# print(fruits_list)

# colors = "red,blue, green, white, black"
# colors = colors.replace(" ","")
# color_list = colors.split(",")
# print(color_list)

# members = "佐藤、 栗田、 内村、 岡田"
# members_list = members.split("、")
# print(members_list)

# result = "23,45,56,87,90,123,231,256,321"
# result_list = result.split(",", 3)[:3]
# print(result_list)

#join
# menbers = ["Tom", "jerry", "spike"]
# name = " and ".join(menbers)
# print(name)


# abc = ["a","b","c"]
# xyz = ["x","y","z"]
# az = abc + xyz
# print(az)
#
# colors = []
# colors += ["red"]
# colors += ["white","black"]
# print(colors)
#
# data = [1, 3, 5]
# newdata = [2, 4, 6]
# data.extend(newdata)
# print(data)

# colors = ["blue","red","green","yellow","pink","black","white"]
# print(colors[:])
# print(colors[3:])
# print(colors[:3])
# print(colors[3:6])
# print(colors[-1:])
# print(colors[:-1])

# data = [10, 21, 35, 49, 51, 60, 77, 81, 92, 100]
# n = 3
# data1 = data[:n]
# data2 = data[n:]
# print(data1)
# print(data2)

# latters = ["a","b","c","d","e","f","g","h","i","j"]
# print(latters[::2])
# print(latters[1::2])
# print(latters[1:5][::2])
# print(latters[1:5:2])

# list_a = [1, 2, 3]
# list_b = list_a
# list_c = [1,2,3]
# print(list_a is list_b)
# print(list_a is not list_c)

# list_mother = [10, 20, 30, 40, 50]
# list_work = list_mother.copy()
# print(list_work)
# print(list_work is list_mother)

# numbers = [15,23,43,22,41,21]
# numbers.sort(reverse=True)
# print(numbers)
#
# laters = ["s","f","o","c","a"]
# laters.sort()
# print(laters)

# numbers = [15, 23, 4, 42, 8, 16]
# numbers_ascend = sorted(numbers, reverse=True)
# print(numbers_ascend)
# print(numbers)

# numbers = [15, 23, 4, 42, 8, 16]
# numbers.reverse()
# print(numbers)

# import random
# numbers = list(range(10))
# random.shuffle(numbers)
# print(numbers)

#リスト内包表記
# words = ["chest","wind","holiday","knight","silence","hot"]
# words.sort(key=len)
# print(words)

# words = ["peach","ver3","Python","Pokemon","ver2"]
# new_words = sorted(words,key=str.lower)
# print(new_words)

# names = ["鈴木","田中","栗林","山岡"]
# for who in names:
#     print(who + "さん")
# print(names)
#
# numbers = [2, 6, -3, 5, -1, 7]
# sum = 0
# for num in numbers:
#     if num > 0:
#         sum += num
# print(sum)

# names = ["鈴木","田中","栗林","山岡"]
# for i, who in enumerate(names,1):
#     print(f"{i}: {who}さん")
#
# name1 = ["鈴木","田中"," 赤尾","佐々木","高田"]
# name2 = ["世奈","悠美","恵子","薫子","幸恵"]
# langname = []
#
# for n1, n2 in zip(name1,name2):
#     langname.append(n1+n2)
# print(langname)

# nums = [1, 2, 3, 4, 5, 6]
# # nums_double = [num*2 for num in nums]
# # print(nums_double)
# nums_double = []
# for num in nums:
#     nums_double.append(num*2)
# print(nums_double)

# import math
# num_list = [5.1, 4.3, 8.2, 6.3, 9.6, 10.2, 2.3]
# result = [math.floor(num) for num in num_list]
# print(result)
#
# numbers = [num for num in range(1,10)]
# print(numbers)
#
# group_list = [str+"組" for str in "ABCDEFG"]
# print(group_list)
#
# name1 = ["鈴木","田中"," 赤尾","佐々木","高田"]
# name2 = ["世奈","悠美","恵子","薫子","幸恵"]
# langname = [n1+n2 for n1, n2 in zip(name1,name2)]
# print(langname)

# numbers = [2.1, 0.2, 0.3, 1.4, 3.1, 0.3, 1.6]
# result = [num for num in numbers if 1<=num<2]
# print(result)

# numbers = [2.1, 4, "", 2.2, "1", 3]
# numbers = [num for num in numbers if isinstance(num, (int, float))]
# print(numbers)

# numbers = [4, 12, 21, 32, 8, 6, 11, 16]
# result = [num for num in numbers if num>=5 if num%2==0]
# print(result)

# data = [[1,2, 3, 4], [5, 6], [7, 8, 9]]
# # result = [num*2 for alist in data for num in alist]
# # print(result)
# result = [[num*2 for num in alist] for alist in data]
# print(result)

# data = [[1,2, 3, 4], [5, 6], [7, 8, 9]]
# result = []
# for alist in data:
#     temp = []
#     for num in alist:
#         temp.append(num*2)
#     else:
#         result.append(temp)
# print(result)

# colors = ["blue","red","green","yellow"]
# print("green" in colors)
# print("block" in colors)

# names = ["鈴木裕子","田中里美","桜木ハヤタ"]
# # print("田中" in names)
# name = "里美"
# result = False
# for item in names:
#     if name in item:
#         result = True
#         break
# print(result)

# id_list = ["a2345","a1236","b7656","f0987"]
# # print(id_list.index("a1236"))
# while True:
#     id = input("idを入力して下さい(qで終了):")
#     if id == "q":
#         print("終了しました")
#         break
#     try:
#         pos = id_list.index(id)
#         print(str(pos+1) + "番目のメンバーです。")
#     except:
#         print("メンバーではありません。")

# numbers = [1, 3, 4, 5, 5, 15, 12, 57]
# print(numbers.count(2))
# print(numbers.count(5))
#
# latters = ["a", "ax", "b", "b", "bx"]
# print(latters.count("a"))

# result = [1, 1, 0, 0, 1, 0, 1, 1]
# half = len(result)/2
# point = result.count(1)
# if point >= half:
#     print("合格")
# else:
#     print("不合格")

# import random
# import secrets
# fruits = ["apple", "orange","banana","peach"]
# # dessrt = random.choices(fruits)
# dessert = secrets.choice(fruits)
# print(dessert)

# data = [56, 45, 83, 67, 59, 41, 77]
# print(sum(data))
# print(max(data))
# print(min(data))
#
# judge = [8.7, 8.8, 9.0, 9.1, 8.5]
# result = sum(judge) - max(judge) - min(judge)
# print(result)

#タプル
# a = (1, 2)
# b = ("PY",3.6)
# c = (89,56,75)
# d = ((10,20),(30,40))
# print(a)

# data = (
#     11, 12, 13,
#     20, 27,
#     34, 35, 39
# )
# print(data)
#
# a = (10, 20)
# b = (20, 30)
# c = a + b
# print(c)
#
# data = (1, 2)
# data += (3,)
# print(data)

# data = tuple(range(-5, 6))
# print(data)
#
# week = tuple("月火水木金土日")
# print(week)
#
# color = ["blue","black","green"]
# data = tuple(color)
# print(data)

# data = ("blue","black","green")
# color = list(data)
# print(color)

# data = (1,2,3,4,5,6,7,8,9)
# top3 = data[:3]
# print(top3)
#
# skip = data[::2]
# print(skip)

# color = ("green","red","blue","yellow")
# print(color[0])
# print(color[1])
# print(color[-1])
# for item in color:
#     print(item)
# for i, item in enumerate(color,1):
#     print(i, item)

# (a, b) = (100, 200)
# print(a)
# a, b = 100, 200
# print(a)
# print(b)
#
# data = (12, 15)
# (boy, girl) = data
# all = boy + girl
# print(boy,girl,all)

# numbers = (4, 8, 15, 16, 23, 42)
# num = int(input("受験番号を入力して下さい。:"))
# if num in numbers:
#     print("合格")
# else:
#     print("不合格")

# data = (56, 45, 83, 67, 59, 41, 77)
# print(sum(data))
# print(max(data))
# print(min(data))

# a = (1, 2, 3)
# b = a
# c = (1, 2, 3)
# print(a == b)
# print(a is b)
# print(a == c)
# print(a is c)

# x = [1,2,3]
# y = [4,5,6]
# z = [7,8,9]
# xyz_opj = zip(x,y,z)
# xyz = list(xyz_opj)
# print(xyz)

# name1 = ["鈴木","田中","赤尾","佐々木","高田"]
# name2 = ["世奈","悠美","恵子","薫子","幸恵"]
# langname = []
# for n1, n2 in zip(name1,name2):
#     langname.append(n1+n2)
# print(langname)

# name1 = ["鈴木","田中","赤尾","佐々木","高田"]
# name2 = ["世奈","悠美","恵子","薫子","幸恵"]
# zip_obj = zip(name1,name2)
# print(list(zip_obj))

#集合(セット)
# color_setA = {"blue","yellow","red"}
# color_setB = {"green","blue","black"}
#
# set1 = {
#     11,22,33,44,55,
#     111, 222
# }
# set2 = {
#     33, 66, 99
# }
# print(f"set1: {set1}")
# print(f"set2: {set2}")
#
# color_set = {"blue","pink","orange","white","black"}
# # print(len(color_set))
# print("red" not in color_set)

# num2set = set(range(0, 20, 2))
# num3set = set(range(0, 20, 3))
# print(num2set)
# print(num3set)

# empty_set = set()
# print(empty_set)
#
# data = [101,103,103,115,167,167,189]
# dataset = set(data)
# print(dataset)

# dataset = {101, 167, 103, 115, 167, 167, 189}
# datalist = list(dataset)
# print(datalist)
# datalist.sort()
# print(datalist)
#
# happyset = set("happy")
# print(happyset)

# fruits = set()
# fruits.add("apple")
# fruits.add("orange")
# print(fruits)

# color_set = {"blue","yellow","red"}
# color_set.discard("green")
# print(color_set)
# color_set.discard("red")
# print(color_set)
#
# dataset = {0.1, 0.2, 0.5, 1.3, 1.6}
# dataset.clear()
# print(dataset)

# color_set = {"red", "green","blue"}
# item = color_set.pop()
# print(item)
# print(color_set)
#
# datatest = frozenset(["a","b","c"])
# datatest.add("x")
# print(datatest)

# numbers = [1, 2, 3, 4, 5, 6]
# num_set = {num*2 for num in numbers}
# print(num_set)

# numbers = [-1.3, 1.2, -1.2, 1.1, 1.5, -1.1, 1.2, 1.1, 1.4]
# num_set = {num for num in numbers if num >0}
# print(num_set)

# a = {"リンゴ","みかん","桃","いちご"}
# b = {"いちご","スイカ","みかん","バナナ"}
# c = a | b
# print(c)

# a = {"リンゴ","みかん","桃","いちご"}
# b = {"いちご","スイカ"}
# c = {"みかん","バナナ"}
# d = a | b | c
# print(d)
#
# set1 = {1, 2, 3}
# list1 = [2, 4, 6, 8]
# list2 = [3, 6, 9]
# data = set1.union(list1,list2)
# print(data)

# a = {"リンゴ","みかん","桃","いちご"}
# b = {"いちご","スイカ","みかん","バナナ"}
# c = {"いちご","リンゴ"}
# d = a.intersection(b, c)
# print(d)
#
# data = {"red","blue"}
# data2 = {"blue","yellow"}
# data3 = {"blue","green"}
# data |= data2
# data |= data3
# print(data)

# data = {"red","blue","green","yellow"}
# data2 = {"blue","black","yellow"}
# # data &= data2
# # data.difference_update(data2)
# # data -= data2
# # data.symmetric_difference_update(data2)
# data ^= data2
# print(data)

# a = {1, 2, 3}
# b = {3, 2, 1}
# c = {1, 2, 3, 4}
# # print(a == b)
# # print(a == c)
# print(a != b)

# a = {"earth","wind","fire"}
# b = {"sky","sea"}
# c = {"fire","water"}
# print(a.isdisjoint(b))

# a = {1999,2011,2013,2014,2016,2017}
# b = {2011, 2013, 2014}
# print(a.issuperset(b))
# print(a >= b)

#辞書
# stock = {"S": 7,"M": 12,"L":3}
# result = {"t1":True,"t2":False, "t3":True}
# point = {10: 5.37,20: 5.56, 30: 5.05, 40: 5.16}
#
# metoro = {
#     "G": "銀座線",
#     "M": "丸の内線",
#     "H": "日比谷線",
#     "T": "東西線",
#     "C": "千代田線",
#     "Z": "半蔵門線",
#     "N": "南北線",
#     "F": "副都心線",
# }
# print(metoro)

# fruit = {"apple": 2, "orange":8, "mango": 2, "peach":1}
# print(fruit)

# data = dict([("yellow",3), ("blue",6), ("green",5)])
# print(data)

# keys = ["yellow","blue","green"]
# values = [3, 6, 5]
# data = dict(zip(keys, values))
# print(data)
#
# data = dict((["yellow", 3],["blue",6],["green",5]))
# print(data)

# stock = dict.fromkeys(['S','M', 'L'], 0)
# print(stock)
#
# data = dict.fromkeys("abcd")
# print(data)

# data = {"yellow": 3,"blue": 6, "green":5}
# data["blue"] = 10
# data["white"] = 5
# print(data)

# data = {"yellow": 3,"blue": 6, "green":5}
# print(data.setdefault("blue",10))
# print(data.setdefault("white",10))
# print(data)
#
# d1 = {}
# d2 = dict()
# print(d1)
# print(d2)

# number = {}
# number["one"] = 1
# number["tow"] = 2
# number["three"] = 3
# number["four"] = 4
# print(number)
#
# data = {"a":10, "b":20, "c":30}
# newdata = {"a":15, "d":99}
# data.update(newdata)
# print(data)

# fruit = {"apple":7, "orange":5, "mango":3}
# del fruit["mango"]
# print(fruit)

# fruit = {"apple":7, "orange":5, "mango":3}
# fruit.clear()
# print(fruit)

# from random import randint
# keys = ["green", "red", "blue", "yellow"]
# data = {key: randint(1, 100) for key in keys}
# print(data)
#
# unicode = {letter:ord(letter) for letter in "hello"}
# print(unicode)

# data = {"a":100, "b":200, "c":300}
# data_b = data
# data_b["c"] = 0
# print(data_b)
# print(data)

# data = {"a":100, "b":200, "c":300}
# data_b = data.copy()
# data_b["c"] = 0
# print(data_b)
# print(data)
#
# fruit = {"apple": 7, "orange": 5, "mango": 3, "peach": 6}
# fruit2 = dict.fromkeys(fruit, 0)
# print(fruit2)
#
# import pprint
# from random import random
# data = {key:random() for key in "abcdefg"}
# print(pprint.pprint((data)))

# menbers = {"東京": 21, "大阪": 16, "福岡": 11}
# print(menbers["東京"])

# city = input("調べる地区名:")
# menbers = {"東京": 21, "大阪": 16, "福岡": 11}
#
# try:
#     value = menbers[city]
#     print(f"{city}の値は{value}です")
# except KeyError :
#     print(f"{city}のデータはありません")
# except Exception as error:
#     print(error)

# members = {"東京": 21, "大阪": 16, "福岡": 11}
# print(members.get("福岡"))
# print(members.get("京都"))

# user = {"id": "ad123", "name": "蒼井ソラ", "age":27}
# print("age" in user)
#
# fruit = {"apple": 7, "orange": 5, "mango": 3, "peach":6}
# for key in fruit:
#     value = fruit[key]
#     print(f"{key}が{value}")

# fruit = {"apple": 7, "orange": 5, "mango": 3, "peach":6}
# print(fruit.keys())
#
# keys = list(fruit.keys())
# print(keys)
#
# keys = [key.capitalize() for key in fruit.keys()]
# print(keys)

# fruit = {"apple": 7, "orange": 5, "mango": 3, "peach":6}
# print(fruit.values())
# values = list(fruit.values())
# print(values)
# print(sum(values))

# fruit = {"apple": 7, "orange": 5, "mango": 3, "peach":6}
# print(fruit.items())
# print(list(fruit.items()))

# fruit = {"apple": 7, "orange": 5, "mango": 3, "peach":6}
# for key, value in fruit.items():
#     print(f"{key}が{value}個")

# fruit = {"apple": 7, "orange": 5, "mango": 3, "peach":6}
# print(fruit.pop("apple"))
# print(fruit)

# fruit = {"apple": 7, "orange": 5, "peach": 6}
# while fruit :
#     key = input("どのフルーツを取り出すか？ (qで終了):")
#     if key == "":
#         continue
#     elif key == "q":
#         print("終了しました")
#         break
#     try:
#         value = fruit.pop(key)
#         print(f"{key}は{value}個")
#     except KeyError:
#         print(f"{key}はありません")
#     except Exception as error:
#         print(error)
#         break
# else:
#     print("空っぽです")

# fruit = {"apple": 7, "orange": 5, "peach": 6}
# print(fruit.popitem())
# print(fruit)

fruit = {"apple": 7, "orange": 5, "peach": 6}
while fruit:
    ans = input("フルーツを取り出しますか? (y/n):")
    if ans == "y":
        key, value = fruit.popitem()
        print(f"{key}は{value}個")
    elif ans == "n":
        print("終了しました")
        break
else:
    print("もう空っぽです")
