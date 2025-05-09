#!/usr/bin/env python3
import argparse
import day6.day6 as day6
import day7.day7 as day7
import day8.day8 as day8


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="Advent2022",
        description="Executes code for given day"
    )
    parser.add_argument('day', type=int)
    parser.add_argument('-t', '--test-mode', action="store_true")
    args = parser.parse_args()
    if args.test_mode:
        input_file = f'day{args.day}\\test_input.txt'
    else:
        input_file = f'day{args.day}\\input.txt'
    with open(input_file, encoding='utf-8') as input:
        match args.day:
            case 6:
                day = day6.Day6(input)
            case 7:
                day = day7.Day7(input)
            case 8:
                day = day8.Day8(input)
            case _: 
                pass
        print(day.part1())
        print(day.part2())

