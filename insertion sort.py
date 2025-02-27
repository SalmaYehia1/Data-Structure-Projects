import random
import time

def generate_random_array(size, min_val=1, max_val=1000):
    """Generates a random array of given size."""
    return [random.randint(min_val, max_val) for _ in range(size)]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

def test_sort_performance(size):
    arr = generate_random_array(size)

    start_time = time.perf_counter()  # High-precision timing
    insertion_sort(arr)
    end_time = time.perf_counter()

    time_taken_ms = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"Size: {size}, Time taken: {time_taken_ms:.3f} ms\n")

# Test with different sizes
test_sizes = [1000, 25000, 50000]

for size in test_sizes:
    test_sort_performance(size)
