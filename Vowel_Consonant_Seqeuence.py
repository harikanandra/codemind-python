def generate_vowel_consonant_sequence(string):
    vowels = 'aeiou'
    sequence = ''
    n = len(string)
    prev_type = 'C' if string[0] not in vowels else 'V'
    sequence += prev_type
    for i in range(1, n):
        current_type = 'C' if string[i] not in vowels else 'V'
        if current_type != prev_type:
            sequence += current_type
            prev_type = current_type
    output = sequence.upper()
    
    return output
input_string =input()
output_string = generate_vowel_consonant_sequence(input_string)
print(output_string)
