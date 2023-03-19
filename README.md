# Median of two sorted lists

## Solution
The algorithm uses the logic behind the merge function of the merge sort. 
It has a time complexity of O(N+M) and space complexity of O(1).

I also provided a bonus solution that directly uses the merge function of the merge sort algorithm.
It has a time complexity of O(N+M) and space complexity of O(N+M), but it's a simpler approach.

## How to run
The two lists must be given as command line arguments. 

These can be provided with -l1, -l2 or --list_1, --list_2 parameters.

Each element must be split with a space character. Here is an example:
```bash
python median_of_two.py -l1 1 4 9 -l2 2 3 5 6 7 12
```

You don't need to provide the lists sorted, it also works with unordered lists. 
It uses a merge sort algorithm (written by me as a bonus) to sort these values:
```bash
python median_of_two.py -l1 5 3 6 5 -l2 1.3 2.3 3.8 4.5
```

## Unit tests
To run the unit tests pytest should be installed:
```bash
pip install -r requirements.txt
```
Unit tests can be run with this command: 
```bash
pytest .
```
