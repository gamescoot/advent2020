import advent_util
import re

# Day 4: Password Processing

# Read the file as always.
FILE_TEXT = advent_util.read_file()

# Separate the passports into separate strings for processing.
PASSPORTS = FILE_TEXT.split('\n\n')

# RegEx to match for specific regex strings. We can both search for the string and validate it at the same time.

# Part1's pattern. Finds anything with one of the 8 keys and returns it.
# Matches the format <key>:<non-separating-characters> with no non-separating-characters before or after.
PARTIAL_PATTERN = r'\b(byr|iyr|eyr|hgt|hcl|ecl|pid):[^ \n]+\b'

# Part2's patterns. This is where the input validation is done. We'll combine these together to make one big pattern.
# Matches the format byr:<number-between-1920-and-2002>
BIRTH_YEAR_PATTERN = r'(?:byr):(?:19[2-9][0-9]|200[0-2])'
# Matches the format iyr:<number-between-2010-and-2020>
ISSUE_YEAR_PATTERN = r'(?:iyr):20(?:1[0-9]|20)'
# Matches the format eyr:<number-between-2020-and-2030>
EXPIRATION_YEAR_PATTERN = r'(?:eyr):20(?:2[0-9]|30)'
# Matches the format hgt:<number-between-150-and-193-for-cm-or-59-and-76-for-in><cm-or-in>
HEIGHT_PATTERN = r'(?:hgt):(?:1(?:[5-8][0-9]|9[0-3])cm|(?:59|6[0-9]|7[0-6])in)'
# Matches the format hcl:#<6-of-any-number-between-0-and-9-or-letter-between-a-and-f>
HAIR_COLOR_PATTERN = r'(?:hcl):#[0-9a-f]{6}'
# Matches the format ecl:<exactly-amb,blu,brn,gry,grn,hzl,-or-oth>
EYE_COLOR_PATTERN = r'(?:ecl):(?:amb|b(?:lu|rn)|gr(?:y|n)|hzl|oth)'
# Matches the format pid:<9-digit-number>
PASSPORT_ID_PATTERN = r'(?:pid):[0-9]{9}'

# Join the patterns together with ORs to make a full pattern. Then set a boundary \b around the whole thing to make sure
# that it only matches one "word" with no extra characters outside.
FULL_PATTERN = r'\b%s\b' % advent_util.re_join(BIRTH_YEAR_PATTERN,
                                               ISSUE_YEAR_PATTERN,
                                               EXPIRATION_YEAR_PATTERN,
                                               HEIGHT_PATTERN,
                                               HAIR_COLOR_PATTERN,
                                               EYE_COLOR_PATTERN,
                                               PASSPORT_ID_PATTERN)

# A passport needs all these keys to be valid.
VALID_KEYS = {'byr', 'iyr', 'eyr', 'ecl', 'hgt', 'hcl', 'pid'}


# Print out the number of partially valid passports (complex one liners need more than one line of comments, lol).
# Prints the length of a list of passports.
# We filter that list by passports that contain all valid keys by using the filter function with a set equality lambda.
# We the key set from the passport by using the partial pattern regex above and putting that into a set.
def part1():
    print(len(list(filter(lambda x: set(re.findall(PARTIAL_PATTERN, x)) == VALID_KEYS, PASSPORTS))))


# Print out the number of fully valid passports (did this one in a complex one liner as well. This challenge was fun!).
# Prints out the length of the list of valid passports.
# We get the valid passport list by filtering a list of passports by a lambda for if they contain valid keys.
# We get which keys the passport contains using the full pattern regex above and putting the first 3 characters of each
# match into a set (by mapping the lambda y[0:3] function onto the list of regex matches).
def part2():
    print(len(list(filter(lambda x: VALID_KEYS == set(map(lambda y: y[0:3], re.findall(FULL_PATTERN, x))), PASSPORTS))))


# Print the 2 answers
part1()
part2()
