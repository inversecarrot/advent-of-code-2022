
from day8.forest import Forest


def part1(forest: Forest) -> str:
    return forest.calculate_cover()

def part2() -> str:
    return ''

def run(filename: str):
    with open(filename, encoding='utf-8') as input:
        input_forest = Forest(input)
    
    print(part1(input_forest))
    # print(part2())

# filename = f'day{8}\\input.txt'

# if __name__ == '__main__':
#     with open(filename, encoding='utf-8') as input:
#         input_forest = Forest(input)
    
#     print(part1(input_forest))