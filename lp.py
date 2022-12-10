import moduls

# Задача 1
footing = moduls.conversion_sixteen_to_decimal('AE')
degree = moduls.conversion_sixteen_to_decimal('A')
b = footing ** degree
print(f'Ответ первой задачи в десятиной  {footing ** degree}')
a = moduls.convert_decimal_to_hex(b)
print(f'В шестнацетичной {a}')

# Задача 2
array = ['F', 'E', 'C']
array1=[]
array2=[]
for dec in array:
    a = moduls.conversion_sixteen_to_decimal(dec)
    array1.append(a)
sor=array1.sort()
print(f'В десятичной {array1}')

for hi in array1:
    b=moduls.convert_decimal_to_hex(hi)
    array2.append(b)
sor2=array2.sort()
print(f'В шестнацетичной {array2}')



print('\n')
# подпрограммы
moduls.addition(45, 12)  # сложение

moduls.subtraction(45, 12)  # вычитание

moduls.multiplication(45, 12)  # умножение

moduls.translation_binary_to_sixteenth('0010110')  # из двоичной системы счисления в шестнадцатеричную

moduls.conversion_sixteen_to_decimal('AE')  # из шестнадцатеричной системы счисления в десятичную

moduls.equal(45, 12)  # равно

moduls.notequal(45, 12)  # не равно

moduls.greater_than_or_equal(45, 12)  # больше или равно

moduls.less_than_or_equal(45, 12)  # меньше или равно

moduls.greater(45, 12)  # больше

moduls.less(45, 12)  # меньше
