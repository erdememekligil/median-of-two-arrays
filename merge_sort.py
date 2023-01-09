from typing import List, Union

FloatInt = Union[float, int]


class MergeSort:

    @staticmethod
    def merge(n1: List[FloatInt], n2: List[FloatInt]) -> List[FloatInt]:
        """
        Merge two sorted lists.
        :param n1: first sorted list.
        :param n2: second sorted list.
        :return: merged sorted list.
        """
        result = list()

        i = j = 0
        while i < len(n1) and j < len(n2):
            if n1[i] < n2[j]:
                result.append(n1[i])
                i += 1
            else:
                result.append(n2[j])
                j += 1

        # add remaining
        r = i if i < len(n1) else j
        nr = n1 if i < len(n1) else n2

        while r < len(nr):
            result.append(nr[r])
            r += 1

        return result

    def __divide(self, nums: List[FloatInt], l: FloatInt, r: FloatInt) -> List[FloatInt]:
        if l > r:
            return []
        elif l == r:
            return [nums[l]]

        mid = (l + r) // 2 + 1

        l1 = self.__divide(nums, l, mid - 1)
        l2 = self.__divide(nums, mid, r)

        return self.merge(l1, l2)

    def merge_sort(self, nums: List[FloatInt]) -> List[FloatInt]:
        return self.__divide(nums, 0, len(nums) - 1)
