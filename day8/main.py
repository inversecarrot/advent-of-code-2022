
from day8.forest import Forest


def part1(forest: Forest) -> str:
    return forest.calculate_cover()

def part2(forest: Forest) -> str:
    return forest.find_max_visibility()

def run(filename: str):
    with open(filename, encoding='utf-8') as input:
        input_forest = Forest(input)
    
    print(part1(input_forest))
    print(part2(input_forest))