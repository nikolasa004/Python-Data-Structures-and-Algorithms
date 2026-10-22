# Data Structures and Algorithms in Python

This repository contains a collection of data structures and algorithms I implemented while studying software engineering. Most of these started as university exercises or assignments, and I kept them as a record of the problems I worked through and the concepts I was learning at the time.

The goal was to understand how these structures and algorithms work internally, rather than rely entirely on Python's built-in collections or existing implementations. These are educational exercises, not production-ready libraries.

## Contents

### Data structures

| File | Topics |
| --- | --- |
| `data_structures/dynamic_array.py` | Resizable array using `ctypes` |
| `data_structures/singly_linked_list.py` | Nodes, insertion, deletion, traversal |
| `data_structures/doubly_linked_list.py` | Bidirectional links and list operations |
| `data_structures/circular_queue.py` | Circular buffer and capacity growth |
| `data_structures/heap.py` | Min-heap, sift-up and sift-down |
| `data_structures/tree.py` | General tree, depth, height and traversals |
| `data_structures/priority_queues.py` | Sorted and unsorted priority queues |
| `data_structures/hash_maps.py` | Separate chaining and linear probing |

### Algorithms

| File | Topics |
| --- | --- |
| `algorithms/sorting.py` | Merge sort and quicksort |
| `algorithms/binary_search.py` | Recursive binary search |

### Arithmetic expression evaluator

The `expression_evaluator/` folder contains one of my university assignments: a stack-based arithmetic expression evaluator. It converts expressions from infix to postfix notation, then evaluates the resulting expression. It supports the operators and input formats covered by the original assignment, so it is not intended as a general-purpose mathematical parser.

Example:

```text
$ python expression_evaluator/expression_evaluator.py
Unesite izraz: 2+3*4
['2', '3', '4', '*', '+']
14
14
```

The `tokenizer.py` module was provided as part of the assignment; **I did not write that module**.

### Additional exercise

- `additional_exercises/custom_range.py` - an exercise recreating part of Python's `range` behavior.

## Running the code

Python 3 is required. The exercises use only Python's standard library.

Individual examples can be run directly:

```bash
python data_structures/heap.py
python data_structures/tree.py
python algorithms/sorting.py
python expression_evaluator/expression_evaluator.py
```

The scripts are independent exercises, rather than parts of a single application. Several files include small demonstrations under `if __name__ == "__main__":`.

## Background

I wrote these exercises while learning about algorithmic problem-solving and data structures. Some tasks were based on material presented during university classes, but this repository focuses on the implementations I practiced myself. I've preserved the general approach and structure of my original work, with limited corrections where needed.
