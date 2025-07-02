#!/usr/bin/env python3

# Bucket Sort distributes elements into several buckets based on value ranges:
# - Each element is placed into a bucket corresponding to its value range
# - Each bucket is then sorted individually (using insertion sort, quicksort, or any efficient sorting algorithm)
# After sorting, all buckets are concatenated in order to produce the final sorted array
# This method works best when input is uniformly distributed over a known range, resulting in near-linear performance.

def bucketSort(arr, l):
    pass

def main():
    array = [1, 4, 5, 3, 9, 4]
    length = len(array)

    bucketSort(array, length)
    print(array)

if __name__ == "__main__":
    main()