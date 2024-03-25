def merge_sort(arr, level=0):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, level + 1)
        merge_sort(R, level + 1)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            print(f"{'  ' * level}Swap occurred: {arr}")
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort_first_iteration(arr, low, high):
    if low < high:
        pi = split(arr, low, high)
        print(f"First iteration result: {arr}")
        return arr

def split(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# Array to be sorted
arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
print("Original array:", arr)

# Merge Sort
print("\nStarting Merge Sort:")
merge_sort(arr)
print("Merge Sorted array:", arr)

# Quick Sort - First Iteration
arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]  # Reset array to original
quick_sort_first_iteration(arr, 0, len(arr) - 1)

