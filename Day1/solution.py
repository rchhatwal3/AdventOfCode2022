##########
###PART 1###

def part1():
    maxSum = 0
    currentSum = 0

    with open ("input.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            if line.strip() == "": #line is empty
                maxSum = max(currentSum, maxSum)
                currentSum = 0
            else:
                currentSum += int(line)
    file.close()
    print(maxSum)

###############
### PART 2 ####

def part2():
    maxSums = []
    currentSum = 0

    with open ("input.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            if line.strip() == "": #line is empty
                maxSums.append(currentSum)
                currentSum = 0
            else:
                currentSum += int(line)

    file.close()
    maxSums.sort(reverse=True)
    print(maxSums[0] + maxSums[1] + maxSums[2])
