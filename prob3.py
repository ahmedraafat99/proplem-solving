def replace_with_vowels(arr):
    # ASCII values for lowercase vowels
    vowel_codes = {97: 'a', 101: 'e', 105: 'i', 111: 'o', 117: 'u'}
    
    # Replace numbers with corresponding vowels if they match the ASCII values
    return [vowel_codes[num] if num in vowel_codes else num for num in arr]
print(replace_with_vowels([97, 98, 99, 101, 120, 105]))  
# Output: ['a', 98, 99, 'e', 120, 'i']
