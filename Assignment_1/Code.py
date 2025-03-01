import random
import time
import matplotlib.pyplot as plt

# Generate a random array
def generate_random_array(size, min_val=1, max_val=None):
    if max_val is None:
        max_val = size * 10
    return [random.randint(min_val, max_val) for _ in range(size)]

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key: # if sorted not 
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1): 
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap only once per iteration

# Bubble Sort
def bubble_sort(arr):
    n = len(arr) 
    for i in range(n, 0, -1):  
        swapped = False
        for j in range(i - 1): 
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True  
        if not swapped:  
            break  

# to measure sorting time
def measure_time(sort_function, arr):
    arr_copy = arr.copy()
    start_time = time.perf_counter()
    sort_function(arr_copy)
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000

def test_sorting_and_plot():
    array_sizes = [1000, 2500, 5000, 10000, 25000, 50000,75000,100000,125000,150000]
    insertion_times = []
    selection_times = []
    bubble_times = []

    for size in array_sizes:
        arr = generate_random_array(size)

        insertion_times.append(measure_time(insertion_sort, arr))
        selection_times.append(measure_time(selection_sort, arr))
        bubble_times.append(measure_time(bubble_sort, arr))

        print(f"\nArray Size: {size}")
        print(f"Insertion Sort Time: {insertion_times[-1]:.2f} ms")
        print(f"Selection Sort Time: {selection_times[-1]:.2f} ms")
        print(f"Bubble Sort Time: {bubble_times[-1]:.2f} ms")

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(array_sizes, insertion_times, marker='o', linestyle='-', color='r', label="Insertion Sort")
    plt.plot(array_sizes, selection_times, marker='s', linestyle='-', color='g', label="Selection Sort")
    plt.plot(array_sizes, bubble_times, marker='^', linestyle='-', color='b', label="Bubble Sort")

    plt.xlabel("Array Size")
    plt.ylabel("Time (ms) (log scale)")
    plt.yscale("log")  
    plt.title("Sorting Algorithms: Time Complexity Analysis")

    plt.legend()
    plt.grid(True)
    plt.show()

test_sorting_and_plot()
