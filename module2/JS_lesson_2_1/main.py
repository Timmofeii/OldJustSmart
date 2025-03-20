# sys.stdout.write("GeeksforGeeks ")
# sys.stdout.write("is best website for coding!")
# alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
#             "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
# user = ("Tom", 22, False)
#
# #a = [3, 5, 6, 1, 2]
#
# #a = [3, 5, 6, 1, 2]
# b = list()
# for i in a: b.append(i ** 2)
#
# #a = [3, 5, 6, 1, 2, 5, 2]
# for i in a:
#     if i == 5:
#         a.remove(i)

#
# a = (34, 26, 3, 45, 3, 8)
#
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         print(a[i])
# a = [34, 26, 3, 45, 3, 8]
# print(a[1:4])

a = [23, 43, 32, 11, 11, 22, 33, 44]


def sum_list(lst):
    return sum(lst)


a = [23, 43, 32, 11, 11, 22, 33, 44]


def sum_for_cut(lst, start_cut, finish_cut):
    #return sum(lst[star_cut, finish_cut])
    summa = 0
    for i in list[start_cut:finish_cut]:
        summa += i
    return summa

def list_power(lst,lst_powers):
    if len(lst)!=len(lst_powers):
        return 0;
    for iter in range(len(lst)):
        lst[iter]**=lst_powers[iter]
    return lst
    # return [x**y for x,y in zip(lst,powers)]

my_list = [1, 2, 3, 4, 5, 6, 7]

powers = [8, 9, 10, 11, 12, 13, 14]
print(list_power(my_list,powers))
print(powers)
