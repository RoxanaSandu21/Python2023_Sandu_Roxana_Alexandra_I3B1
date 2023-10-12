import re


# Exerciutiul 1
def gcd_multiple(*numbers):
    gcd = numbers[0]
    for num in numbers[1:]:
        while num != 0:
            gcd, num = num, gcd % num
    return gcd


countOfArray = int(input('1. Enter he count of numbers: '))
numbers1 = []
for x in range(countOfArray):
    print(f'Enter a number: ')
    number = int(input())
    numbers1.append(number)
print(gcd_multiple(*numbers1))


# Exercitiul 2
def calculate_number_of_vowels(string_to_calculate):
    vowel_count = 0
    for i in range(len(string_to_calculate)):
        if (
                (string_to_calculate[i] == "a")
                or (string_to_calculate[i] == "e")
                or (string_to_calculate[i] == "i")
                or (string_to_calculate[i] == "o")
                or (string_to_calculate[i] == "u")
        ):
            vowel_count += 1
    return vowel_count


stringToCalculateVowels = str(input('2. Enter a string: '))
print(calculate_number_of_vowels(stringToCalculateVowels))


# Exercitiul 3

string1 = str(input('3. Enter 2 strings: '))
string2 = str(input())
print('the number of occurrences of the first string in the second: ', string2.count(string1))


# Exercitiul 4
def upper_to_underscore(string_with_uppercase):
    snake_case = ""

    for char in string_with_uppercase:
        if char.isupper():
            snake_case += "_"
        snake_case += char.lower()

    if snake_case.startswith('_'):
        snake_case = snake_case[1:]

    return snake_case


stringWithUpperCase = input('Enter a string with uppercase words (e.g., UpperCamelCase): ')
print(upper_to_underscore(stringWithUpperCase))



# Exercitiul 5
def matrix_in_spiral_order(matrix_to_read_from):
    result = []
    while matrix_to_read_from:
        result += matrix_to_read_from[0]
        matrix_to_read_from = list(zip(*matrix_to_read_from[1:]))[::-1]
    return ''.join(result)


matrixIndex = int(input('5. Enter the index of a square matrix: '))
matrix = []
for b in range(matrixIndex):
    row = []
    for c in range(matrixIndex):
        row.append(str(input()))
    matrix.append(row)
print(matrix_in_spiral_order(matrix))


#Exerctiul 6
def is_palindrome(number_is_palindrome):
    num_str = str(number_is_palindrome)
    return num_str == num_str[::-1]


numberToVerify = int(input('6. Enter a number u want to verify if it is a palindrome: '))
print(is_palindrome(numberToVerify))


#Execitiul 7
def extract_number(text):
    match = re.search(r'\d+', text)

    if match:
        return int(match.group())
    else:
        return None


stringToExtractFrom = str(input('7. Enter a string that eventually contains a number: '))
print(extract_number(stringToExtractFrom))


#Exercitiul 8
def count_ones_bits(number8):
    count = 0
    binary_str = bin(number8)
    for bit in binary_str:
        if bit == '1':
            count += 1
    return count


numberToVerify = int(input('8. Enter a number u want to to see how many 1 bits it has: '))
print(count_ones_bits(numberToVerify))


#Exercitiul 9
def most_common_letter(string):
    string = string.lower()

    letter_count = {}

    for char in string:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    most_common = max(letter_count, key=letter_count.get)

    return most_common


stringCommonLetter = str(input('9. Enter a string u want to see which is the most common letter: '))
print(extract_number(stringCommonLetter))


#Exercitiul 10
def count_words(string):
    words = string.split()
    return len(words)


text = str(input('10. Enter a string u want to see the number of words: '))
print(count_words(text))
