# Простые
# Хранит в себе только одно значение.
# • Целое число (int)
# • Вещественное число (float)
# • Комплексное число (complex)
# • Булевое значение (bool)
# • Специальный тип None
a = 1 # целое число
a = 1.0 # вещественное число
a = 1 + 1 # комплексное число
a = True # булевое значение
a = None # пустой тип


# Составные
# Хранит в себе несколько значений (как одного типа, так и разного).
# Может быть пустым (нет ниодного элемента) или хранить от 1 и более значений.
# Строка (str) Список (list) Кортеж (tuple)
# • Множество (set, frozenset) • Словарь (dict)
# • Байты (bytes)
# Последовательность байтов (bytearray)
a = 'hello' # строка
a = [1, 1.0, 'hello'] # список
a = (1, 1.0, 'hello') # кортеж
a = {1, 1.0, 'hello'} # множество
a = frozenset({1, 1.0, 'hello'}) # неизменяемое множество
a = {'a': 1, 'b': 2} # словарь
a = b'hello' # байтовый тип
a = bytearray(b'hello')

# Неизменяемые
# Неизменяемыми могут быть как простые, так и составные типы.
# Все простые являются неизменяемыми.
# Для составного типа Python не позволяет изменить значения Внутри объекта или структуру (допустим было два значения, а стало три значения).
# • Неизменяемые простые:
# • Целое число (int)
# • Вещественное число (float)
# • Комплексное число (complex)
# • Булевое значение (bool)
# • Специальный тип None
# Неизменяемые составные:
# • Строка (str)
# • Кортеж (tuple)
# • Байты (bytes)
# • Неизменяемое множество (frozenset)

# Изменяемые
# Тип может быть только составным.
# Python позволяет изменить как значение внутри объекта, так и структуру (наполнение) объекта.
# • Список (list)
# • Множество (set)
# • Словарь (dict)
# • Последовательность байтов (bytearray)

# Вызываемые
# В Python есть специальный вызываемый тип Callable. Ему соответствуют большинство встроенные команд, например:
# • help()
# • print()
# • input()
# • len()
# • min() или мах()
# • type()
а = [1, 1.0, 'hello'] # создаем список
help(a) # выводим информацию об 'а'
print(a) # выводим значение "а" в консоль
b = input('Введи число') # в консоль выводится сообщение и ожидается когда пользователь введет число
len(a) # сколько объектов в 'а'
min(a) # минимальное значение в 'а'
max(a) # максимальное значение в "а"
type(a) # тип объекта 'а'

# Типизация в Python
# Тип переменной определяется во время выполнения программы, а не заранее, когда вы пишете код.
# То есть, вы можете сначала присвоить переменной число, а потом - строку, и Python без проблем это примет.
a = 1
a = 'новое значение переменной а'

# Неявная типизация
# Вам не нужно явно указывать тип переменной, когда вы её создаёте.
# Python сам понимает, какого типа значение вы ей присваиваете.
some_var :int = 1
other_var :str = 'Hello World'
# Явно тип указывать не нужно поэтому Python понимает что за тип у переменной.
some_var = 1
other_var = 'Hello World'