
def separate_string(s):
    letters = ""
    numbers = ""
    for char in s:
        if char.isalpha():
            letters += char
        elif char.isdigit():
            numbers += char

    return letters, numbers

def converted(letters, numbers):
    even_numbers = ""
    even_numbers_ascii = ""
    for digit in numbers:
        if int(digit) % 2 == 0:
            even_numbers += digit + " "
            even_numbers_ascii += f"{digit}({ord(digit)})"

    uppercase_letters = ""
    uppercase_letters_ascii = ""
    for lett in letters:
        if lett.isupper():
            uppercase_letters += lett + " "
            uppercase_letters_ascii += f"{lett}({ord(lett)})"

    return even_numbers.strip(), even_numbers_ascii.strip(), uppercase_letters.strip(), uppercase_letters_ascii.strip()

s = "56aAWW1984sktr235270aYmn145ss785fsq31D0"

letters, numbers = separate_string(s)

even_numbers, even_numbers_ascii, uppercase_letters, uppercase_letters_ascii = converted(letters, numbers)

print("Letters :", letters)
print("Numbers :", numbers)
print("Even numbers:", even_numbers)
print("Even numbers in ASCII :", even_numbers_ascii)
print("Uppercase Letters:", uppercase_letters)
print("Uppercase Letters in ASXII :", uppercase_letters_ascii)