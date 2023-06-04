def reverse_vowels(string):
    vowels = 'aeiouAEIOU'
    string = list(string)
    i, j = 0, len(string) - 1

    while i < j:
        if string[i] in vowels and string[j] in vowels:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        elif string[i] in vowels:
            j -= 1
        else:
            i += 1

    return ''.join(string)
input_str = input()
output_str = reverse_vowels(input_str)
print(output_str)