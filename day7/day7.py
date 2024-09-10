from filetree import FileTree

def get_size(filename: str) -> str:
    with open(filename, encoding='utf-8') as commands:
        tree = FileTree(commands)
    return tree.get_sum_of_large_directories()

def part1(filename: str) -> str:
    return get_size(filename)

def part2(filename: str) -> str:
    return ''

if __name__ == '__main__':
    print(part1('day7\\input.txt'))
    print(part2('day7\\input.txt'))