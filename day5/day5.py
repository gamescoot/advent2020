import advent_util

FILE_TEXT = advent_util.read_file()


# Part 1: Parse the input into a list of seat numbers. If you replace the R's and B's with 1 and L's and F's with 0,
# then you can just cast it directly to an integer using base 2 cast.While on each line it iterates through the string
# and converts the letters to 1s or 0s, then casts the string result.
def part1():
    return [int(''.join('1' if (j == 'R') | (j == 'B') else '0' for j in i), 2) for i in FILE_TEXT.split('\n')]


# Part 2: Finds our seat number. The list of numbers is a range of numbers from (max_num-length-1) to max_num, so we
# should be able to find our seat by subtracting the triangle number of max from the triangle number of the lower number
# and then subtracting the sum of all the numbers in our list of seat numbers.
def part2(nums, max_num):
    print(int(((max_num * (max_num + 1)) / 2) - (((max_num - len(nums) - 1) * (max_num - len(nums))) / 2) - sum(nums)))


# Get the seat nums from part1 and then print the max and then use the nums and max to get our seat in part 2.
seat_nums = part1()
max_seat_num = max(seat_nums)
print(max_seat_num)
part2(seat_nums, max_seat_num)
