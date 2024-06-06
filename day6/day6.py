def part1(filename: str) -> str:
    return parse(filename, 4)

def part2(filename: str) -> str:
    return parse(filename, 14)

def parse(filename: str, marker_size: int) -> str:
    with open(filename, encoding='utf-8') as datastream:
        char_count = 1
        next_bit = datastream.read(1)
        last = ['' for x in range(0, marker_size -1)]
        while next_bit != '\n':
            if not next_bit in last and char_count >= 4 and len(set(last)) == marker_size - 1:
                print(next_bit)
                print(last)
                return char_count
            last[char_count % (marker_size - 1)] = next_bit
            char_count += 1
            next_bit = datastream.read(1)

    return char_count

if __name__ == '__main__':
    print(part1('day6\\input.txt'))
    print(part2('day6\\input.txt'))