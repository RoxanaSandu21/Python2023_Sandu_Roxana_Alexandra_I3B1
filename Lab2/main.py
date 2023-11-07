# Exercitiul 1
def generate_fibonacci(n):
    fibonacci_sequence = []
    if n <= 0:
        return fibonacci_sequence
    elif n == 1:
        return [0]
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence


number = 10 #int(input('1. Enter how many numbers from the Fibonacci sequence u want to see: '))
print("Exercitiul 1: ")
print(generate_fibonacci(number))


#Exercitiul 2

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True


def find_primes_in_list(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


#length = int(input('2. Enter the length of the list: '))
numbersArePrime = [1, 2, 3, 4, 5 , 6 , 7, 9, 10] #[]
#for i in range(length):
#    number = int(input('Enter a number: '))
#    numbersArePrime.append(number)
print("Exercitiul 2: ")
print(find_primes_in_list(numbersArePrime))


# Exercitiul 3

def list_operations(a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    difference_a_b = list(set(a) - set(b))
    difference_b_a = list(set(b) - set(a))

    return intersection, union, difference_a_b, difference_b_a


#length_a = int(input('3. Enter the length of the first list: '))
list_a = [1, 2, 3, 4, 5] #[]
#for i in range(length_a):
#    number = int(input('Enter a number: '))
#    list_a.append(number)

#length_b = int(input('Enter the length of the second list: '))
list_b = [4, 5, 6, 7] #[]
#for i in range(length_b):
#    number = int(input('Enter a number: '))
#    list_b.append(number)

intersection, union, diff_a_b, diff_b_a = list_operations(list_a, list_b)

print("Exercitiul 3: ")
print("Intersection:", intersection)
print("Union:", union)
print("Difference A - B:", diff_a_b)
print("Difference B - A:", diff_b_a)


# Exercitiul 4

def compose(notes, moves, start_position):
    song = []
    current_position = start_position
    for move in moves:
        move = move % len(notes)
        song.append(notes[current_position])
        current_position = (current_position + move) % len(notes)
    while len(song) < len(notes):
        song.append(notes[current_position])
        current_position = (current_position + 1) % len(notes)
    return song


#length_of_notes = int(input('4. Enter the length of the notes list: '))
notes = ["do", "re", "mi", "fa", "sol"] #[]
#for i in range(length_of_notes):
#    note = str(input('Enter a note: '))
#    notes.append(note)

#length_of_moves = length_of_notes - 1
moves = [1, -3, 4, 2] #[]
#for i in range(length_of_moves):
#    move = int(input('Enter a move: '))
#    moves.append(move)

start_position = 2 #int(input('Enter a start position: '))
print("Exercitiul 4: ")
print(compose(notes, moves, start_position))


# Exercitiul 5

def replace_below_diagonal_with_zeros(matrix):
    num_rows = len(matrix)
    if num_rows > 0:
        num_cols = len(matrix[0])
    else:
        num_cols = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if i > j:
                matrix[i][j] = 0
    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result_matrix = replace_below_diagonal_with_zeros(matrix)
print("Exercitiul 5: ")
for row in result_matrix:
    print(row)


# Exercitiul 6

def find_items_appearing_x_times(x, *lists):
    item_counts = {}
    for lst in lists:
        for item in lst:
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1
    result = [item for item, count in item_counts.items() if count == x]
    return result


list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [4, 1, "test"]
x = 2
print("Exercitiul 6: ")
print(find_items_appearing_x_times(x, list1, list2, list3, list4))


# Exercitiul 7

def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]


def find_palindromes(numbers):
    palindrome_count = 0
    greatest_palindrome = None
    for num in numbers:
        if is_palindrome(num):
            palindrome_count += 1
            if greatest_palindrome is None or num > greatest_palindrome:
                greatest_palindrome = num
    return (palindrome_count, greatest_palindrome)


number_list = [121, 123, 1331, 45654, 789]

result = find_palindromes(number_list)
print("Exercitiul 7: ")
print(result)


#Exercitiul 8

def generate_ascii_lists(x=1, strings=[], flag=True):
    result_lists = []
    for string in strings:
        char_list = []
        for char in string:
            ascii_code = ord(char)
            if (flag and ascii_code % x == 0) or (not flag and ascii_code % x != 0):
                char_list.append(char)
        result_lists.append(char_list)
    return result_lists


x = 2
strings = ["test", "hello", "lab002"]
flag = False
print("Exercitiul 8: ")
print(generate_ascii_lists(x, strings, flag))


# Exercitiul 9

def find_seats_with_blocked_view(matrix):
    blocked_seats = []
    num_rows = len(matrix)
    if num_rows > 0:
        num_cols = len(matrix[0])
    else:
        num_cols = 0
    for col in range(num_cols):
        for row in range(1, num_rows):
            spectator_height = matrix[row][col]
            can_see_game = True
            for prev_row in range(row):
                if matrix[prev_row][col] >= spectator_height:
                    can_see_game = False
                    break
            if not can_see_game:
                blocked_seats.append((row, col))
    return blocked_seats
stadium = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]
print("Exercitiul 9: ")
print(find_seats_with_blocked_view(stadium))


# Exercitiul 10

def merge_lists(*lists):
    min_length = min(len(lst) for lst in lists)
    merged_result = []
    for i in range(min_length):
        merged_tuple = tuple(lst[i] for lst in lists)
        merged_result.append(merged_tuple)
    return merged_result


list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]
print("Exercitiul 10: ")
print(merge_lists(list1, list2, list3))


# Exercitiul 11

def custom_sort(item):
    if len(item[1]) >= 3:
        return item[1][2]
    else:
        return ''


input_tuples = [('abc', 'bcd'), ('abc', 'zza')]

sorted_list = sorted(input_tuples, key=custom_sort)
print("Exercitiul 11: ")
print(sorted_list)


# Exercitiul 12


def group_by_rhyme(words):
    rhyme_groups = {}
    for word in words:
        rhyme = word[-2:]
        if rhyme in rhyme_groups:
            rhyme_groups[rhyme].append(word)
        else:
            rhyme_groups[rhyme] = [word]
    grouped_words = list(rhyme_groups.values())
    return grouped_words


word_list = ['ana', 'banana', 'carte', 'arme', 'parte']
print("Exercitiul 12: ")
print(group_by_rhyme(word_list))
