from typing import List, Union

from merge_sort import MergeSort
from utils import parse_args, pre_process_list

FloatInt = Union[float, int]


def median_of_sorted(nums: List[FloatInt]) -> FloatInt:
    """
    Median of a sorted list.
    :param nums: sorted list.
    :return: median value.
    """
    if len(nums) == 0:
        raise ValueError("List is empty.")
    mid = len(nums) // 2
    if len(nums) % 2 == 1:
        return nums[mid]
    else:
        return (nums[mid] + nums[mid - 1]) / 2


def median_of_two_sorted(n1: List[FloatInt], n2: List[FloatInt]) -> FloatInt:
    """
    This method uses the same logic behind the merge method of merge sort. Check it first to understand the logic better
    The algorithm compares i'th and j'th elements in lists, the smaller number will be considered as a possible median.
    There are two while loops in the algorithm. First one considers both lists at once. Second loop starts when the
    one of the two lists are traversed completely.
    :param n1: first sorted list.
    :param n2: second sorted list.
    :return: median.
    """
    total_len = len(n1) + len(n2)
    if total_len == 0:
        raise ValueError("Both lists are empty.")

    def check_is_finished():
        """
        Helper function that checks the ending criteria.
        If lists have a total of an odd number of elements [1] is median. if even, ([0]+[1]) / 2 is median.
        """
        if len(medians) > 1:
            if is_odd:
                return medians[1]
            else:
                return (medians[0] + medians[1]) / 2
        else:
            return None

    is_odd = total_len % 2 == 1
    target_c = (total_len // 2) - 1
    i = j = c = 0
    medians = list()

    while i < len(n1) and j < len(n2):
        if n1[i] <= n2[j]:
            smaller_number = n1[i]
            i += 1
        else:
            smaller_number = n2[j]
            j += 1

        # add it to possible medians list if the counter says that we are in the middle of the array.
        if c >= target_c:
            medians.append(smaller_number)
        result = check_is_finished()
        if result is not None:
            return result
        c += 1

    # one array is finished. consider the other one
    r = i if i < len(n1) else j
    nr = n1 if i < len(n1) else n2

    while r < len(nr):
        if c >= target_c:
            medians.append(nr[r])
        r += 1

        result = check_is_finished()
        if result is not None:
            return result
        c += 1

    return medians[0]


if __name__ == "__main__":
    l1, l2 = parse_args()
    # Bonus: preprocess lists. Convert floats to int (to print prettier) and sort arrays if necessary.
    l1 = pre_process_list(l1)
    l2 = pre_process_list(l2)

    print("First list:", l1)
    print("Second list:", l2)

    # Solution takes O((N+M) / 2) = O(N+M) time to complete.
    med = median_of_two_sorted(l1, l2)
    print("Median:", med)

    # Bonus: alternative way: using merge function of merge sort.
    # This solution consumes O(N+M) memory, but its simpler.
    # Merged array is also sorted, so it is easier to calculate the median.
    merged = MergeSort.merge(l1, l2)
    med = median_of_sorted(merged)
    print("Median (alternative method):", med)
    if len(merged) % 2 == 1:
        log = med
    else:
        log = f"({merged[len(merged) // 2]-1} + {merged[len(merged) // 2]}) / 2 = {med}"
    print(f"<the merged array would be {merged}, the median would be {log}>")
