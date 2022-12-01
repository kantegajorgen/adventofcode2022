
def solution1(input_file):

    most_calories = []

    with open(input_file, "r") as fp:
        for cals in fp.read().split("\n\n"):
            most_calories.append(sum([int(i) for i in cals.split("\n") if i != ""]))
    
    return sorted(most_calories)[-1]


def solution2(input_file):
    
    most_calories = []

    with open(input_file, "r") as fp:
        for cals in fp.read().split("\n\n"):
            most_calories.append(sum([int(i) for i in cals.split("\n") if i != ""]))
    
    return sum(sorted(most_calories)[-3:])

print(f"Answer1: {solution1('input')}")
print(f"Answer2: {solution2('input')}")