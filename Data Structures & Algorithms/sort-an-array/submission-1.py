import random
class Solution:
    def quicksort(self, A: List[int], lo: int, hi:int):
        if lo>= 0 and hi >= 0 and lo < hi:
            p = self.partition(A, lo, hi)
            self.quicksort(A, lo, p)
            self.quicksort(A, p +1, hi)

    def partition(self, A: List[int], lo: int, hi:int):
        r = random.randint(lo, hi)
        A[lo], A[r] = A[r], A[lo]
        pivot = A[lo]
        i = lo -1
        j = hi +1
        while True:
            i = i+1
            while A[i] < pivot:
                i = i+1
            j = j-1
            while A[j] > pivot:
                j = j-1
            if i >= j:
                return j
            A[i], A[j] = A[j], A[i]

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums