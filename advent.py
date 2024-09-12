#!/usr/bin/env python3
import argparse

import day8.main


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="Advent2022",
        description="Executes code for given day"
    )
    parser.add_argument('day', type=int)
    day = parser.parse_args().day
    input_file = f'day{day}\\input.txt'
    match day:
        case 8:
            day8.main.run(input_file)
        case _: 
            pass

