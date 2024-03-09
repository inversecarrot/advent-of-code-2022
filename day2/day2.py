""" Script for day 2 solution """

SHAPE_VALUE: dict[str, int] = {"X": 1, "Y":2, "Z": 3}

def score_round(opp: str, input: str) -> int:
    """ 
        Takes two input throws as "A/B/C" for opp and "X/Y/Z" for input and returns round score
        Score is 1 for throwing rock, 2 for paper, 3 for scissors, + 6 for winning or 3 for draw
    """
    match input:
        case "X":
            match opp:
                case "A":
                    return SHAPE_VALUE[input] + 3
                case "B":
                    return SHAPE_VALUE[input] + 0
                case "C":
                    return SHAPE_VALUE[input] + 6
            return 0
        case "Y": 
            match opp:
                case "A":
                    return SHAPE_VALUE[input] + 6
                case "B":
                    return SHAPE_VALUE[input] + 3
                case "C":
                    return SHAPE_VALUE[input] + 0
        case "Z":
            match opp:
                case "A":
                    return SHAPE_VALUE[input] + 0
                case "B":
                    return SHAPE_VALUE[input] + 6
                case "C":
                    return SHAPE_VALUE[input] + 3
        case _:
            return 0
        
def score_resulted_round(opp: str, res: str) -> int:
    """ 
        Takes throw as "A/B/C" for opp and "X/Y/Z" for desired result and returns round score
        Score is 1 for throwing rock, 2 for paper, 3 for scissors, + 6 for winning or 3 for draw
    """
    match res:
        case "X":
            res_value = 0
            match opp:
                case "A":
                    return SHAPE_VALUE['Z'] + res_value
                case "B":
                    return SHAPE_VALUE['X'] + res_value
                case "C":
                    return SHAPE_VALUE['Y'] + res_value
            return 0
        case "Y": 
            res_value = 3
            match opp:
                case "A":
                    return SHAPE_VALUE['X'] + res_value
                case "B":
                    return SHAPE_VALUE['Y'] + res_value
                case "C":
                    return SHAPE_VALUE['Z'] + res_value
        case "Z":
            res_value = 6
            match opp:
                case "A":
                    return SHAPE_VALUE['Y'] + res_value
                case "B":
                    return SHAPE_VALUE['Z'] + res_value
                case "C":
                    return SHAPE_VALUE['X'] + res_value
        case _:
            return 0
        
def sum_total_scores(filename: str) -> int:
    score = 0
    with open(filename, encoding="utf-8") as rounds:
        for line in rounds:
            throws = [t for t in line.split() if not (t.isspace() or t == "\n")]
            score += score_round(throws[0], throws[1])
    return score

def sum_total_resulted_scores(filename: str) -> int:
    score = 0
    with open(filename, encoding="utf-8") as rounds:
        for line in rounds:
            inputs = [t for t in line.split() if not (t.isspace() or t == "\n")]
            score += score_resulted_round(inputs[0], inputs[1])
    return score


if __name__ == '__main__':
    print(sum_total_scores('day2\\input.txt'))
    print(sum_total_resulted_scores('day2\\input.txt'))