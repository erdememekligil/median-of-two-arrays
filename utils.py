import argparse
from typing import List, Tuple, Union
from merge_sort import MergeSort

FloatInt = Union[float, int]


def parse_args() -> Tuple[List[FloatInt], List[FloatInt]]:
    parser = argparse.ArgumentParser(prog='Median of two',
                                     description='This script sorts the two given lists, '
                                                 'merges them and finds their median value.',
                                     epilog="usage: median_of_two.py -l1 3 7 5 4 -l2 2 4 6 8 5")
    parser.add_argument('-l1', '--list_1', nargs='*', type=float, help="First list of numbers", required=True)
    parser.add_argument('-l2', '--list_2', nargs='*', type=float, help="Second list of numbers", required=True)

    args = parser.parse_args()
    return args.list_1, args.list_2


def is_ordered(nums: List[FloatInt]) -> bool:
    if len(nums) == 0:
        return True
    prev = nums[0]
    for x in nums:
        if x < prev:
            return False
    return True


def pre_process_list(nums: List[FloatInt]) -> List[FloatInt]:
    list_type = int if all(x.is_integer() for x in nums) else float

    # if all elements is int, make the list integers.
    if list_type == int:
        nums = [int(x) for x in nums]

    if not is_ordered(nums):
        sorter = MergeSort()
        nums = sorter.merge_sort(nums)
    return nums
