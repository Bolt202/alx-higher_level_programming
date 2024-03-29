#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    numeric_values = [
        roman_values[char] for char in roman_string.upper()
    ] + [0]
    result = 0

    for index in range(len(numeric_values) - 1):
        if numeric_values[index] >= numeric_values[index + 1]:
            result += numeric_values[index]
        else:
            result -= numeric_values[index]

    return result
