#!/usr/bin/env python3

# Counting Sort is a non-comparative sorting algorithm that works by counting the number of occurrences
# of each unique element in the input list:
# - A count array is created where the index represents the element value, and the value at that index represents the frequency of that element
# - The count array is used to place each element in its correct position in the output array
# After processing the count array, the elements are placed back in sorted order in the original array.
# This process results in a stable sort with a time complexity of O(n + k), where n is the number of elements and k is the range of the input.

def countingSort(arr):
    pass

def main():
    array = [1, 4, 5, 3, 9, 4]

    countingSort(array)
    print(array)

if __name__ == "__main__":
    main()