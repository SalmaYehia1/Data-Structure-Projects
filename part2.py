import random

def partition(arr, low, high):
    # Choose a random pivot and swap it with the last element
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]  # Pivot is now the last element
    
    i = low  # Start i from low
    
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]  # Swap smaller element with arr[i]
            i += 1  # Move i to next position for smaller elements

    # Swap pivot with arr[i], now ivot is in the right place
    arr[i], arr[high] = arr[high], arr[i]
    
    return i  # Pivot index

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)  # Partition the array
        quick_sort(arr, low, pivot_index - 1)  # Recursively sort left part
        quick_sort(arr, pivot_index + 1, high)  # Recursively sort right part




# Function to perform merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return  # Base case: If the array has 1 or no elements, it's already sorted

    # Find the middle index to split the array
    mid = len(arr) // 2  
    left_half = arr[:mid]  # Left half of the array
    right_half = arr[mid:]  # Right half of the array

    # Recursively sort both halves
    merge_sort(left_half)
    merge_sort(right_half)

    # Merge the sorted halves back together
    merge(arr, left_half, right_half)

# Function to merge two sorted halves , 
# MERGING IN PLACE FOR BETTER SPACE COMPLEXITY
def merge(arr, left_half, right_half):
    
    i = j = k = 0  # Pointers for left_half, right_half, and main array

    # Compare elements from both halves and place them in the correct order
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1  # Move to the next element in left_half
        else:
            arr[k] = right_half[j]
            j += 1  # Move to the next element in right_half
        k += 1  # Move to the next position in the main array

    # Copy any remaining elements from left_half
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Copy any remaining elements from right_half
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
################################################

def heapify(arr, n, i):
    """
    This function maintains the max-heap property.
    It ensures that the largest value is at the root.
    """
    largest = i  # Assume root is the largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def build_max_heap(arr):
    """
    This function converts an unsorted array into a max-heap.
    It starts from the last non-leaf node and moves up.
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):  # Start from the last non-leaf node
        heapify(arr, n, i)

def heap_sort(arr):
    """
    This function sorts an array using heap sort.
    It repeatedly extracts the max element and re-heapifies the array.
    """
    n = len(arr)

    # Step 1: Build a max-heap
    build_max_heap(arr)

    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap max element to end
        heapify(arr, i, 0)  # Restore heap property on the reduced heap

# Example usage




# Example usage
arr1 = [0,10, 7, 8, 9,-100,1000 ,1, 5]
quick_sort(arr1, 0, len(arr1) - 1)
print("quick sort result: Sorted array:", arr1)
print("...........................")

arr2 = [0,10, 7, 8, 9,-100,1000 ,1, 5]
merge_sort(arr2)
print("Merge sort result: Sorted array:", arr2)
arr3 = [0,10, 7, 8, 9,-100,1000 ,1, 5]
print("..................................")
heap_sort(arr3)
print("Heap sort result: Sorted array:", arr3)

