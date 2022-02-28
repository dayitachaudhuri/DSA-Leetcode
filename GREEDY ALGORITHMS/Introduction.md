# GREEDY ALGORITHMS

An algorithmic paradigm that follows the problem solving approach of making the **locally optimal choice** at each stage in hopes that it will lead to the **globally optimal solution**.

Not all problems can be solved by Greedy Algorithms.

## Properties of Greedy Algo Problems :
- GREEDY CHOICE PROPERTY - Global Optimum can be arrived at by selecting local optimum.
- OPTIMUM SUBSTRUCTURE - Optimal solution to problem contains optimal solution to subproblems.

Greedy algorithm never reconsiders its choices unlike Dynamic Programming.

|Greedy Algorithm Problems             |Link to Question                |
| :------------------------------------|-------------------------------:|
|[1. Activity Selection Problem](#activity-selection-problem)|[Link](https://practice.geeksforgeeks.org/problems/activity-selection-1587115620/1/)|
|[2. Properties](#properties-of-binary-trees)|[Link](https://practice.geeksforgeeks.org/problems/activity-selection-1587115620/1/)|
|[3. Types](#types-of-binary-trees)|[Link](https://practice.geeksforgeeks.org/problems/activity-selection-1587115620/1/)|
|[4. Tree Traversals](#tree-traversals)|[Link](https://practice.geeksforgeeks.org/problems/activity-selection-1587115620/1/)|

# Activity Selection Problem


**You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.**

### Solution Statement

_The greedy choice is to always pick the next activity whose finish time is least among the remaining activities and the start time is more than or equal to the finish time of the previously selected activity._

1. Sort the activities in order of end time.
2. Select the first activity from the sorted array and print it. 
3. For remaining activities, if the start time of this activity is greater than or equal to the finish time of the previously selected activity then select this activity and print it.

### Python Code

