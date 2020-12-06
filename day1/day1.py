import advent_util

# Day 1: Sum to 2020

# Parse the input file.
INPUT_LINES = advent_util.read_file().split('\n')
NUM_FIND = 2020


# Iterates through the input one time and finds two numbers that add to 2020 and returns their product.
def part1(num_find,x):

    # Initialize variables.
    past_nums = {}
    y = 0

    # Iterate through the lines and if we're not on the line x, then check if it and a number we've already passed will
    # add up to 2020, then multiply the two and return them.
    for curr_num_string in INPUT_LINES:
        # Skip lines that match line number x.
        if x != y:
            # Get the number to check and see if its match is in the ones we've passed so far and return the product of
            # it and its match.
            curr_num = int(curr_num_string)
            if str(curr_num) in past_nums:
                return curr_num * (num_find - curr_num)
            else:
                # If the number is not in the passed numbers then add its match to the list
                new_num_string = str(num_find - curr_num)
                past_nums[new_num_string] = curr_num
        y += 1  # Increment the line to match with x


# Finds two numbers in the input that add to 2020 and returns their product.
def part2(num_find_p2):

    # Initialize variables
    x = 0

    # Iterate through the lines and subtract the line from the num_find_2 and then pass it to part 1 to find 2 nums that
    # we can add with first_num to get the num_find_p2. Multiply the 3 together (Part 1 will multiply its 2 together).
    for first_num_string in INPUT_LINES:
        num_find_p1 = num_find_p2 - int(first_num_string)
        p1 = part1(num_find_p1, x)
        if p1 is not None:
            return p1 * int(first_num_string)
        x += 1  # Increment the line to match with x


# Print the 2 answers.
print(part1(NUM_FIND, -1))  # Negative one means it won't skip any lines
print(part2(NUM_FIND))
