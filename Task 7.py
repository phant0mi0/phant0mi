
a = {1: 'x', 2: 'y', 3: 'z'}
for index, value in a.items():
 print(f'"Позичия: {index} -> значение: {value}"')

# Список list

for value in [1, 2, 3, 4, 5]:
 print(value)

# Кортеж tuple

for value in (1, 2, 3, 4, 5):
 print(value)

# Множество set

for value in {1, 2, 3, 4, 5}:
 print(value)

 numbers = [10, 20, 30, 40, 50]  # Объявление списка чисел
 total = 0 # TODO Заменить использование индексов на перебор значений списка
 for i in range(len(numbers)):
     total += numbers[i]
 print("Сумма чисел:", total)  # Сумма чисел: 150

 numbers = [10, 20, 30, 40, 50]  # Объявление списка чисел total = 0
 # TODO Заменить использование индексов на перебор значений списка
 for num in numbers:
     total += num
 print("Сумма чисел:", total)
 # Сумма чисел: 150

 for tuple in enumerate(["a", "6", "B"]):
     print(tuple)

for pos, value in enumerate("абв", start=1): # start можно указать любым целым числом
 print("Позиция:", pos, "->", "Значение:", value)

 # while условие:
 # Начало блока кода с телом цикла. Один отступ вправо от уровня объявления цикла
 # ...
 # Конец блока кода с телом цикла
 # Код который будет выполняться после цикла. Один отступ влево, чтобы закончить объявление цикла

# while some_expr:
# some_expr логическое выражение, которое определяет когда нужно остановить цикл
# Начало блока кода с телом цикла. Один отступ вправо от уровня объявления цикла
# Конец блока кода с телом цикла
# код который будет выполняться после цикла. Один отступ влево, чтобы закончить объявление цикла

count = 0
while count < 5:
 print("значение сount:", count)
count += 1

sum = 0
input_number = int(input("Bвeдите число: "))
while input_number != 0:
 sum += input_number
input_number = int(input("Bведите число: "))
print("OтBет:", sum)

num = 10
while num > 0:
    print (num)

