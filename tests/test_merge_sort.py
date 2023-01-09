from merge_sort import MergeSort
import random


class TestMergeSort:

    def test_merge_sort_simple(self):
        sorter = MergeSort()
        result = sorter.merge_sort([5, 1, 6, 3, 2, 7, 9])
        assert result == [1, 2, 3, 5, 6, 7, 9]

    def test_merge_sort_float(self):
        sorter = MergeSort()
        nums = [random.random() * 1000 for _ in range(100)]
        result = sorter.merge_sort(nums)
        assert result == sorted(nums)

    def test_merge_sort_sorted(self):
        sorter = MergeSort()
        result = sorter.merge_sort(list(range(100)))
        assert result == list(range(100))

    def test_merge_sort_inverse_sorted(self):
        sorter = MergeSort()
        result = sorter.merge_sort(list(range(99, -1, -1)))
        assert result == list(range(100))
