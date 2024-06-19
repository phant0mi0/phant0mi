
def name_func(arg):
# начало тела функции
# ...
# конец тела функции

# Сколько времени понадобится, чтобы понять, какой общий смысл здесь заложен? list = [1, 2, 3, 4, 5]
a = list[len(list) // 3]
for b in range(len(list)):
    if list[b] < a:
     a = list[b]
print(a)

def min(list):
 a = list [len(list) // 3]
 for b in range(len(list)):
     if list [b] < a:
         a = list[b]
 return a
list = [1, 2, 3, 4, 5]
min(list) # ищем минимум, как будем искать будем разбираться на мере необходимости

list_1 = [1, 2, 3]
list_2 = [6, 5, 4]
min_1 = list_1[0] for value in list_1:
    if value < min_1:
    min_1 = value
min_2 = list_2[0] for value in list_2:
    if value < min_2:
min_2 = value
result = min_1 + min_2
result


def min (list_):
 min_value = list_[0]
 for value in list_: if value <min_value:
min_value = value
return min_value
list_1 = [1, 2, 3]
list_2 = [6, 5, 4]
result = min_(list_1) + min_(list_2)
result

