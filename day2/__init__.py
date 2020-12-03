import re
from functools import reduce
from decimal import Decimal

PATTERN = r'(\d*)-(\d*) (\w): (\w*)'  # Finds a number, another number, a letter, and a word from the format given
INPUT_FILENAME = 'input'
READWRITE_MODE = 'r'

# Prints out the amount of valid passwords
def part1():
    file_text = read_file(INPUT_FILENAME)
    parsed_array = parse_text(file_text)
    filtered_array = list(filter(is_valid_password1_boring, parsed_array))

    print(len(filtered_array))


# Returns true if given password is valid (it works but it's booooring)
def is_valid_password1_boring(password_line):
        c = password_line.password_string.count(password_line.letter)
        is_long_enough = c >= password_line.num1
        is_short_enough = c <= password_line.num2
        return is_short_enough & is_long_enough


# Prints out the amount of valid passwords
def part2():
    file_text = read_file(INPUT_FILENAME)
    parsed_array = parse_text(file_text)
    filtered_array = list(filter(is_valid_password2, parsed_array))

    print(len(filtered_array))


# Returns true if given password is valid
def is_valid_password2(password_line):
    return (password_line.password_string[password_line.num1-1] ==
            password_line.letter) != \
           (password_line.password_string[password_line.num2-1] ==
            password_line.letter)


# Parses text
def parse_text(text):
    parsed_array = []
    for match_obj in re.finditer(PATTERN, text):
        password_line = PasswordLine(match_obj.group(1),
                                     match_obj.group(2),
                                     match_obj.group(3),
                                     match_obj.group(4))
        parsed_array.append(password_line)
    return parsed_array


# Reads file with given filename and returns the entire text of the file
def read_file(filename):
    file = open(filename, READWRITE_MODE)
    file_text = file.read()
    file.close()
    return file_text


class PasswordLine:
    """ A password policy and a password """
    def __init__(self, num1, num2, letter, password_string):
        self.num1 = int(num1)
        self.num2 = int(num2)
        self.letter = letter
        self.password = []
        self.password[:0] = password_string  # Converts the string to a list of chars (e.g. pass->['p','a','s','s'])
        self.password_string = password_string


# The alphabet but converted to its corresponding prime number
LETTER_TO_PRIME = {'a': 2,
                   'b': 3,
                   'c': 5,
                   'd': 7,
                   'e': 11,
                   'f': 13,
                   'g': 17,
                   'h': 19,
                   'i': 23,
                   'j': 29,
                   'k': 31,
                   'l': 37,
                   'm': 41,
                   'n': 43,
                   'o': 47,
                   'p': 53,
                   'q': 59,
                   'r': 61,
                   's': 67,
                   't': 71,
                   'u': 73,
                   'v': 79,
                   'w': 83,
                   'x': 89,
                   'y': 97,
                   'z': 101}


# fun and exciting solution that works mathematically but is wrong for 1 line
# of the input due to floating point precision of VERY large numbers.
# This would work if you used a large number float library like bigfloat, but
# I'm tired and want to sleep. lol.
def is_valid_password1_fun(password_line):
    prime = LETTER_TO_PRIME[password_line.letter]
    test = [1] + password_line.password
    password_product = reduce(is_valid_password_helper, test)
    dec1 = Decimal(password_product) / Decimal(prime ** password_line.num1)
    is_long_enough = dec1 - dec1.to_integral_exact() == 0

    dec2 = Decimal(password_product) / Decimal(prime ** (password_line.num2 + 1))

    is_short_enough = dec2 - dec2.to_integral_exact() != 0
    return is_long_enough & is_short_enough


# Converts the given letter to its prime
def is_valid_password_helper(previous_product, letter):
    return previous_product * LETTER_TO_PRIME[letter]


part1()
part2()
