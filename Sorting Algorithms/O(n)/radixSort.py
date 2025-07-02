#!/usr/bin/env python3

# Radix Sort processes each digit of the numbers starting from the least significant digit (LSD) to the most significant digit (MSD):
# - In each pass, the list is sorted based on the current digit using a stable sorting algorithm (commonly Counting Sort)
# - Elements are grouped into buckets based on their current digit and reassembled after each pass
# The process is repeated for each digit place until all digits have been processed
# This results in a fully sorted array in linear time relative to the number of digits.

def radixSort(arr, l):
    pass

def main():
    array = [121, 432, 511, 372, 949, 404]
    length = len(array)

    radixSort(array, length)
    print(array)

if __name__ == "__main__":
    main()