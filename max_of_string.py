
def find_max_valued_char(string):
    max_valued_char = ''
    max_value = 0

    for char in string:
        if ord(char) > max_value:
            max_valued_char = char
            max_value = ord(char)

    return max_valued_char
input_str = input()
output_char = find_max_valued_char(input_str)
print(output_char)