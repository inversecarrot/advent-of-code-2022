from filetree import FileTree

def get_size(tree: FileTree) -> str:
    return tree.get_sum_of_large_directories()

def part1(tree: FileTree) -> str:
    return get_size(tree)

def part2(tree: FileTree) -> str:
    return tree.get_smallest_big_directory(70000000, 30000000)

if __name__ == '__main__':
    with open('day7\\input.txt', encoding='utf-8') as commands:
        command_tree = FileTree(commands)
        print(part1(command_tree))
        print(part2(command_tree))