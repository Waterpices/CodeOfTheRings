# CodeOfTheRings
Codingame - Optimisation Problem

See https://www.codingame.com/multiplayer/optimization/code-of-the-rings for the rules of the optimisation challenge.

# Find the most optimal way to loop n times
`CodeOfTheRingLoopIteration.py` goal is to find what the best way to do n loops in the least amount of character.
For each n, where 26 >= n >= 2, it gives the offset of the counter and the change to apply to the counter at the end of each loop.

The result will be used to make a map that return the offset and the increment needed for a given number of loop needed.

# Find the recuring patern inside a string
`loopDetection.py` is composed of 2 function :
```py
def count_biggest_substring_replication(string):
```
This function return the largest substring that's countained multiple time in a row

```py
def longest_substring_replication_chain(string):
```
This function identifies and returns the repeating substring forming the longest consecutive chain of characters within the given input string.

Both of those function are tested with : `testsLoopDetection.py`.
