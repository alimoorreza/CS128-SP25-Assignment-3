# CS128-SP25-Assignment-3:
## Robot Motion Planning

For this assignment, you are going to implement graph search algorithms to perform robot motion planning.
## The Data :bar_chart: 
You will use two given text files as inputs:
* _robot_world1.txt_ (attached in this repository)
* _robot_world1_heuristic_values.txt_ (attached in this repository)

The goal of this robot motion planning assignment is to complete the implementation of __Best First Search__ and __A* Search__ to find a path from the robot's _initial state_ to the _goal state_ in the given _robot_world1.txt_. The heuristic values for each cell in the robot world are provided in _robot_world1_heuristic_values.txt_ (you do not need to compute them).

## The Exercises:
**Part 1(Priority Queue): [2 points]** You must finish <span style="color:blue">class __PriorityQueueRobotNav__ </span>. Implementations for most of the methods are provided. I will be looking for the following to be included in your submission:
* remove() method: This should remove a node from the __FRINGE__ based on priority. The node with the minimum *f_value* should be returned when this method is invoked. You should do the following:
  * Find the index of node object with the minimum *f_value*
  * Eliminate that node object from *self.priority_queue*
  * Finally, return that *Node* object
  

**Part 2: [1 point]** Normalize the data and run a k-Nearest-Neighbor algorithm on it (use the StandardScalar from sklearn).

**Part 3: [1 point]** Use a Markup cell to answer the following questions:
* What algorithm performed better? kNN or Decision Trees? Why do you think this was the case?
* What effect did normalizing the data have on your results? Explain. 

Lastly, as always, use a Markup cell to put your name at the top of the file. Rename your file LastnameNotebook4.ipynb and submit it to this submission form. You do not need to submit a copy of the data.

## Rubric :ballot_box_with_check:

## :white_check_mark: Grading: 
I will update the following rubric with your grade after you have completed the assignment.
### Rubric:
| Exercise #  | Points Awarded (out of 1)  | Notes |
| --------- | ------------------- | --------- |
| 1.1: knn           |        |    |
| 1.2: wKNN          |        |    | 
| 1.3: Decision Tree |        |    |
| 2: Normalize       |        |    | 
| 3: Conclusions     |        |    |
| <b>Total           |    /5 | </b>   |
