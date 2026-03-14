# Assignment-6
# Selection Algorithms and Core Data Structures
Project Overview

This project explores the implementation and analysis of important algorithms and data structures used in computer science. The project is divided into two main components: selection algorithms for identifying the kth smallest element in a dataset, and the implementation of fundamental data structures. The objective is to demonstrate how algorithm design and data structure choice influence computational efficiency and performance in practical applications.

# Project Files

The project contains the following main files:

selection_algorithms.py – Implements algorithms used to find the kth smallest element in an unsorted list. The file includes the Median of Medians algorithm and the Randomized Quickselect algorithm.

elementary_data_structures.py – Contains implementations of core data structures including arrays, stacks, queues, and linked lists, along with their key operations.

# Selection Algorithms

Two algorithms were implemented and tested using the dataset:

[12, 3, 5, 7, 19, 2, 17, 6, 14, 4]

The objective was to determine the 5th smallest element.

# Median of Medians
A deterministic selection algorithm that guarantees O(n) worst-case time complexity. It works by dividing the dataset into groups of five, computing the medians of each group, and recursively selecting a pivot to partition the array.

Randomized Quickselect
A probabilistic algorithm that selects a random pivot and partitions the dataset similarly to QuickSort. It achieves O(n) average-case complexity but may degrade to O(n²) in rare cases.

Both algorithms correctly identified 6 as the 5th smallest element.

# Data Structures

The file elementary_data_structures.py demonstrates basic operations and time complexity of several common data structures:

Arrays – Provide constant time O(1) access but require O(n) time for deletion due to shifting elements.

Stacks – Follow the Last-In-First-Out (LIFO) principle with O(1) push, pop, and peek operations.

Queues – Operate using First-In-First-Out (FIFO) ordering with O(1) enqueue and dequeue operations.

Linked Lists – Allow efficient insertion and deletion in O(1) time but require O(n) traversal for searching.

#How to Run the Code

Ensure Python 3.x is installed.

Place both files in the same directory.

Run the scripts individually:

# python selection_algorithms.py

# python elementary_data_structures.py

Each script will demonstrate the implemented algorithms or data structure operations and display the results.

# Summary

The results show that Randomized Quickselect performs faster on average, while Median of Medians guarantees stable worst-case performance. The data structure implementations highlight how different structures optimize different types of operations in computing systems.
