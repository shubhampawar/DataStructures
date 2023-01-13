# def solve(nums, k):
#     nums = sorted(nums)
#     p = len(nums) - k
#     m = nums[-1] - nums[0]
#     for i in range(0, len(nums) - p + 1):
#         if nums[i + p - 1] - nums[i] < m:
#             m = nums[i + p - 1] - nums[i]
#     return m
#
#
# nums = [8,7,4,1]
# k = 2
# print(solve(nums, k))
# def solution(A, K):
#     n = len(A)
#     lmin, lmax = A[:], A[:]
#     rmin, rmax = A[:], A[:]
#
#     for i in range(1, n):
#         lmin[i] = min(lmin[i], lmin[i - 1])
#         lmax[i] = max(lmax[i], lmax[i - 1])
#
#     for i in range(n - 2, -1, -1):
#         rmin[i] = min(rmin[i], rmin[i + 1])
#         rmax[i] = max(rmax[i], rmax[i + 1])
#     amp = min(rmax[K] - rmin[K], lmax[~K] - lmin[~K])
#
#     for i in range(n - K - 1):
#         cand = max(lmax[i], rmax[i + K + 1]) - min(lmin[i], rmin[i + K + 1])
#         amp = min(amp, cand)
#
#     return amp
import math


def remove_k_elements(A, k, memo={}):
    n = len(A)
    min_amplitude = float('inf')  # initialize min_amplitude to infinity

    # base case: if k is 0, return the amplitude of the original array
    if k == 0:
        return max(A) - min(A)

    # check the memoization table to see if we have already calculated this subproblem
    if (n, k) in memo:
        return memo[(n, k)]

    # iterate through the array and try removing each element
    for i in range(n):
        remaining = A[:i] + A[i + 1:]  # remove the ith element from the array
        print(A[:i] , A[i + 1:])
        amplitude = remove_k_elements(remaining, k - 1, memo)  # recursive call to remove k-1 more elements
        min_amplitude = min(min_amplitude, amplitude)  # update min_amplitude if necessary

    # store the result in the memoization table
    memo[(n, k)] = min_amplitude

    return min_amplitude


nums = [3, 5, 1, 3, 9, 8]
k = 4
print(remove_k_elements(nums, k))
