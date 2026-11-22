# Problem: Rank Elements in an Array
# Source: https://leetcode.com/problems/rank-transform-of-an-array/
# Topic: Array, Sorting
# Note: Replace every number with its rank (its position among the sorted unique values).
#
# What it does, in simple words:
#   The smallest number gets rank 1, the next bigger number gets rank 2, and so on.
#   Equal numbers always get the same rank, and ranks have no gaps.
#
# How it works:
#   1. Remove duplicates with set(), then sort the unique values from small to large.
#      This sorted list is our "ranking ladder": the value at index 0 is rank 1, etc.
#   2. For each number in the original array, find where it sits on the ladder
#      (rank.index(num)) and add 1, because ranks start at 1 but indexes start at 0.
#
# Example:
#   Input:  40 10 20 30 10
#   Ladder: [10, 20, 30, 40]
#   Output: 4 1 2 3 1
#
# Time complexity: O(n log n + n * k), where n is the array length and k is the number
#   of unique values. Sorting costs O(k log k), and each rank.index() call scans the
#   ladder, so the worst case (all values distinct) is O(n^2).
#   (Storing the ladder in a dict {value: rank} would make each lookup O(1).)
# Space complexity: O(n) for the ladder and the result list.

n = int(input('Enter the number of elements: '))
print('Enter the elements: ', end='')
arr = list(map(int, input().split()))

rank = sorted(list(set(arr)))

res = []
for num in arr:
    res.append(rank.index(num) + 1)

print(f"Ranks: {' '.join(map(str, res))}")