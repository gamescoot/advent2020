import advent_util

# Init constants by reading input and splitting it to groups of people's answers
FILE_TEXT = advent_util.read_file()
FORMS = FILE_TEXT.split('\n\n')


# Prints the sum of all the answers for each group.
# Get rid of the line breaks to make each group into a long string of letters, then convert the string of letters into a
# set of letters to dedupe it. Get the length of the set and then get the sum of those lengths and print it.
def part1():
    print(sum(map(lambda x: len(set(x.replace('\n', ''))), FORMS)))


# Prints the sum of all answers for each group where everyone agrees.
# Splits the elements of FORMS by their line breaks so we have each person's answers individually. Then does an
# intersection between all of the lists. Get the length of the resulting intersection and sum up those lengths.
def part2():
    print(sum(map(lambda m: len(set(m[0]).intersection(*m[1:])), map(lambda x: x.split('\n'), FORMS))))


# Print the 2 answers
part1()
part2()
