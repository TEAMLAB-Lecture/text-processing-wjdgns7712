def normalize(input_string):
    normalized_string = ' '.join(input_string.lower().split())
    return normalized_string

def no_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    no_vowel_string = input_string
    for i in no_vowel_string:
        if i in vowels:
            no_vowel_string = no_vowel_string.replace(i, '')
    return no_vowel_string