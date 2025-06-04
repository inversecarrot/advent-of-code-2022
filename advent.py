#!/usr/bin/env python3
import argparse
import day1.day1 as day1
from day11 import day11
from day12 import day12
import day2.day2 as day2
import day3.day3 as day3
import day4.day4 as day4
import day5.day5 as day5
import day6.day6 as day6
import day7.day7 as day7
import day8.day8 as day8
import day9.day9 as day9
import day10.day10 as day10


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
            case 1:
                day = day1.Day1(input)
            case 2:
                day = day2.Day2(input)
            case 3:
                day= day3.Day3(input)
            case 4:
                day = day4.Day4(input)
            case 5:
                day = day5.Day5(input)
            case 6:
                day = day6.Day6(input)
            case 7:
                day = day7.Day7(input)
            case 8:
                day = day8.Day8(input)
            case 9:
                day = day9.Day9(input)
            case 10:
                day = day10.Day10(input)
            case 11:
                day = day11.Day11(input)
            case 12:
                day = day12.Day12(input)
            case _: 
                pass
        print(day.part1())
        print(day.part2())

