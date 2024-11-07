def get_ascii_char(number):
    try:
        return chr(number)
    except ValueError:
        return "Invalid input. Please provide a number between 0 and 127."

# Examples
print(get_ascii_char(65))  # Output: 'A'
print(get_ascii_char(97))  # Output: 'a'
print(get_ascii_char(48))  # Output: '0'
