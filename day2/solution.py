
def solution1(input_file, score_table, outcome_table):

    total_score = 0

    with open(input_file, "r") as fp:
        puzzle = [line.split(" ") for line in fp.read().splitlines()]
        for round in puzzle:
            total_score += (score_table[round[1]] + outcome_table["".join(round)])
            
    return total_score


def solution2(input_file, score_table, outcome_table, end_table):

    total_score = 0

    with open(input_file, "r") as fp:
        puzzle = [line.split(" ") for line in fp.read().splitlines()]
        for round in puzzle:
            for key, value in outcome_table.items():
                if round[0] == key[0] and end_table[round[1]] == value:
                    total_score += (score_table[key[1]] + value)
                    break
    
    return total_score


# A=Rock, B=Paper, C=Scissors, X=Rock, Y=Paper, Z=Scissors
score_table = {
    "X":1,
    "Y":2,
    "Z":3
}
outcome_table = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3
}
end_table = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

print(f"Answer1: {solution1('input', score_table, outcome_table)}")
print(f"Answer2: {solution2('input', score_table, outcome_table, end_table)}")