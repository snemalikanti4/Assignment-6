import random

# Deterministic Selection Algorithm (Median of Medians)
def median_of_medians(arr, k):
    """
    Select the kth smallest element in an array using the Median of Medians algorithm.
    This algorithm ensures worst-case linear time complexity (O(n)).

    Parameters:
    arr (list): The input array
    k (int): The order statistic (1-based index)

    Returns:
    int: The kth smallest element
    """
    if len(arr) <= 5:
        return sorted(arr)[k-1]

    # Divide the array into groups of 5
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    # Recursively call the median_of_medians on the medians
    pivot = median_of_medians(medians, len(medians) // 2 + 1)

    # Partition the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_list = [x for x in arr if x == pivot]

    # Return the kth smallest based on the partition
    if k <= len(low):
        return median_of_medians(low, k)
    elif k > len(low) + len(pivot_list):
        return median_of_medians(high, k - len(low) - len(pivot_list))
    else:
        return pivot_list[0]

# Randomized Selection Algorithm (Randomized Quickselect)
def randomized_quickselect(arr, k):
    """
    Select the kth smallest element in an array using the Randomized Quickselect algorithm.
    This algorithm achieves O(n) time complexity on average.

    Parameters:
    arr (list): The input array
    k (int): The order statistic (1-based index)

    Returns:
    int: The kth smallest element
    """
    if len(arr) == 1:
        return arr[0]

    # Randomly choose a pivot
    pivot = random.choice(arr)

    # Partition the array around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_list = [x for x in arr if x == pivot]

    # Determine the position of the pivot and recurse accordingly
    if k <= len(low):
        return randomized_quickselect(low, k)
    elif k > len(low) + len(pivot_list):
        return randomized_quickselect(high, k - len(low) - len(pivot_list))
    else:
        return pivot_list[0]

# Helper function to test the algorithms
def test_selection_algorithms():
    arr = [12, 3, 5, 7, 19, 2, 17, 6, 14, 4]
    k = 5
    print(f"Original array: {arr}")
    print(f"{k}th smallest element using Median of Medians: {median_of_medians(arr, k)}")
    print(f"{k}th smallest element using Randomized Quickselect: {randomized_quickselect(arr, k)}")

# Run the test function
test_selection_algorithms()
