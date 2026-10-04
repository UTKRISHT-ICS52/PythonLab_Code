# Implementation of Bubble sort in python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # optimization: track if any swap happened
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # no swaps → already sorted
            break
    return arr

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", data)
    print("Sorted:  ", bubble_sort(data))
    




