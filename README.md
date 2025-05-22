# Search-Algorithms-in-Python
This project contains Python implementations of common search algorithms used in artificial intelligence and graph theory. Each algorithm is demonstrated on a sample graph.

## Implemented Algorithms

1. **DFS (Depth-First Search)**
2. **BFS (Breadth-First Search)**
3. **DLS (Depth-Limited Search)**
4. **IDS (Iterative Deepening Search)**
5. **UCS (Uniform Cost Search)**

## Project Structure

- `search_algorithms.py`: Contains all search algorithm functions.
- `graph.py`: Defines the sample unweighted and weighted graphs.
- `main.py`: Runs and tests the algorithms with example input.

## How to Run

Clone the repository and run:

```bash
python main.py

DFS:
A B D E F

BFS:
A B C D E F

DLS:
A B D E F

IDS:
Depth limit: 0
A 
Depth limit: 1
A B C 
Depth limit: 2
A B D E F

UCS:
A B C E F
Reached F with cost 4
