def rom_int(x: str) -> int:

    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    num = 0
    last = 'I'

    for n in x[::-1]:
        if romans[n] < romans[last]:
            num -= romans[n]
        else:
            num += romans[n]
        last = n
    return num


def int_to_rom(x):
    numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman = ['I', '1V', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

    i = 12
    rom_num = ''

    while x != 0:
        if numbers[i] <= x:
            rom_num += roman[i]
            x = x - numbers[i]
        else:
            i -= 1
    return rom_num
