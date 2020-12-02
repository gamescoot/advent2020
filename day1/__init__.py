# Day1 p1
import day1.day1.py
def part1(numFind, x):
    f = open("day1", "r")
    pastNums = {}
    y = 0
    for currNumString in f:
        if x != y:
            currNum=int(currNumString)
            if str(currNum) in pastNums:
                    return currNum * (numFind - currNum)
            else:
                newNumString = str(numFind - currNum)
                pastNums[newNumString] = currNum
        y += 1

def part2(numFind):
    f = open("day1", "r")
    pastNums = {}
    x = 0
    for firstNumString in f:
        numFind = 2020 - int(firstNumString)
        p1 = part1(numFind, x)
        if p1 is not None:
            return (p1*int(firstNumString))
        x+=1

print(part2(2020))