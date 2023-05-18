import random


def kth_largest(nums, k):
    if not nums:
        return
    pivot = random.choice(nums)
    left = [x for x in nums if x > pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x < pivot]

    L, M = len(left), len(mid)

    if k <= L:
        return kth_largest(left, k)
    elif k > L + M:
        return kth_largest(right, k - L - M)
    else:
        return mid[0]