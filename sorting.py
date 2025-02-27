import time  
import random  
import matplotlib.pyplot as plt  
size = 50000

def bubble_sort(arr):
  
    n = len(arr) 
    for i in range(n, 0, -1):  # Outer loop: starts from n and decreases to 1
        swapped = False
        for j in range(i - 1):  # Inner loop: goes from 0 to i-1
            if arr[j] > arr[j + 1]:  # Swap if elements are out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True  
        if not swapped:  # Stop if no swaps occurred (optimization)
            break  


def generate_random_array(size):
    ##Creates a list of random numbers from 1 to 1,00,000.
    arr = []
    for _ in range(size):
        arr.append(random.randint(1, 100000))
    return arr



def test_sorting_and_plot():
    """Tests Bubble Sort on different array sizes and plots the results."""
    array_sizes = [1000, 5000, 10000, 25000, 50000 , 100000]  # Different array sizes
    times = []  # List to store execution times

    for size in array_sizes:
        arr = generate_random_array(size)  # Generate a random array
        
        arr_copy = arr[:]  # Make a copy for fair testing

        start_time = time.time()  # Start time
        bubble_sort(arr_copy)  # Sort the array
        end_time = time.time()  # End time
        
        elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
        times.append(elapsed_time)  # Store time taken
        
        print(f"Bubble Sort with {size} elements took {elapsed_time:.2f} ms")  

    # Plot the graph
    plt.figure(figsize=(8, 5))
    plt.plot(array_sizes, times, marker='o', linestyle='-', color='b', label="Bubble Sort")
    plt.xlabel("Array Size")
    plt.ylabel("Time (ms)")
    plt.title("Bubble Sort: Time vs Array Size")
    plt.legend()
    plt.grid(True)
    plt.show()  # Display the graph

# Run the testing function
test_sorting_and_plot()  
