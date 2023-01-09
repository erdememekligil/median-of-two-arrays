import random

from median_of_two import median_of_sorted, median_of_two_sorted


class TestMergeSort:

    def test_median_of_sorted_odd(self):
        med = median_of_sorted([1, 2, 3, 5, 6, 7, 9])
        assert 5 == med

    def test_median_of_sorted_even(self):
        med = median_of_sorted([1, 2, 3, 5, 6, 7, 9, 11])
        assert 5.5 == med

    def test_median_of_two_sorted_odd(self):
        med = median_of_two_sorted([3, 5, 8, 9, 11], [4, 10, 12, 13])
        assert 9 == med

    def test_median_of_two_sorted_even(self):
        med = median_of_two_sorted([3, 5, 8, 9, 11], [4, 10, 12, 13, 15])
        assert 9.5 == med

    def test_median_of_two_sorted_err(self):
        try:
            med = median_of_two_sorted([], [])
            assert None is med
        except ValueError:
            assert True
