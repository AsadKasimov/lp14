def addition(a, b):
    c = hex(a + b)
    print(c.replace('0x', ''))


def subtraction(a, b):
    c = hex(a - b)
    print(c.replace('0x', ''))


def multiplication(a, b):
    c = hex(a * b)
    print(c.replace('0x', ''))


def division(a, b):
    c = hex(a / b)
    print(c.replace('0x', ''))


def translation_binary_to_sixteenth(a):
    c = int(a, 2)
    print(hex(c).replace('0x', ''))


def conversion_sixteen_to_decimal(hexadecimal_string):
    # Creating the Dictionary
    dictionary_hexa_to_decimal = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                  'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    # hexadecimal_string = input("Please enter the hexadecimal value: ").strip().upper()
    decimal = 0

    length = len(hexadecimal_string.strip().upper()) - 1

    for digit in hexadecimal_string:
        decimal += dictionary_hexa_to_decimal[digit] * 16 ** length
        length -= 1

    return decimal


def convert_decimal_to_hex(a):
    v = hex(a).split('x')[-1]
    return v


def equal(a, b):
    print(a == b)


def notequal(a, b):
    print(a != b)


def greater_than_or_equal(a, b):
    print(a >= b)


def less_than_or_equal(a, b):
    print(a <= b)


def greater(a, b):
    print(a > b)


def less(a, b):
    print(a > b)
