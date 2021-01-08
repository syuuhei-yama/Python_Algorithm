#最大値
# a = [1, 3, 10, 2, 8]
# max = a[0]
#
# for i in range(1,len(a)):
#
#     if (max < a[i]): #最小値はここをmin変更
#         max = a[i]
#
# print(max)

#データの交換
# a = 10
# b = 20
#
# t = a
# a = b
# b = t
#
# print("a=",a,",b=",b)

#サーチアルゴリズム
a = [10,3,1,4,2]

search_s = 4
findID = -1

for i in range(len(a)):
    if a[i] == search_s:
        findID = i
        break
print("見つかったID=",findID)

