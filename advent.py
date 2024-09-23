#!/usr/bin/env python3
import argparse

import day8.main


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
    match args.day:
        case 8:
            day8.main.run(input_file)
        case _: 
            pass

