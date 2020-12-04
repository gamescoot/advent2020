from advent_util import advent_util
FILE_NAME='input'
FILE_TEXT = advent_util.read_file(FILE_NAME)


# Traverses through the file text using an equation to figure out the position
# of each character we need to count.
def part1(horizontal_travel, vertical_travel):

    line_width = FILE_TEXT.find('\n') + 1  # Character count including \n
    slope_width = line_width - 1  # Character count excluding \n
    travel_dist = (line_width * vertical_travel) + horizontal_travel  # Distance we travel every step
    step_count = int(FILE_TEXT.count('\n') / vertical_travel)  # Amount of times we want to step

    tree_count = 0

    # Now we just go through each step and add up the trees
    for pos in range(step_count):
        # Get the character we need from the file text and compare it to # then cast the resulting bool to an int to add
        # either 0 if it's . or 1 if it's #. We will decide what character from the string to get each step by using an
        # equation. The equation is just using the line slope f(x) = x * travel distance to traverse the slope, but
        # eventually we will hit the edge of the text and need to wrap around like pacman. To wrap around we determine
        # how many times we've needed to wrap so far by doing int((pos * horizontal_travel) / slope_width) and then
        # we multiply that by the width of the slope to determine how much we need to subtract to wrap around. Then we
        # subtract the original line slope by the width we determined to wrap back around.
        tree_count += int(FILE_TEXT[pos * travel_dist - int((pos * horizontal_travel)/slope_width)*slope_width] == '#')
    return tree_count


# Multiplies answers from part 1 with various horiz and vert travel
def part2():
    return part1(1, 1) * part1(3, 1) * part1(5, 1) * part1(7, 1) * part1(1, 2)


print(part1(3, 1))
print(part2())
