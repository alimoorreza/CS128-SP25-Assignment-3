# CS128-SP25-Assignment-3:
## Robot Motion Planning

For this assignment, you are going to implement graph search algorithms to perform robot motion planning.
## The Data :bar_chart: 
You will use two given text files as inputs:
* _robot_world1.txt_ (attached in this repository)
* _robot_world1_heuristic_values.txt_ (attached in this repository)

The goal of this robot motion planning assignment is to complete the implementation of __Best First Search__ and __A* Search__ to find a path from the robot's _initial state_ to the _goal state_ in the given _robot_world1.txt_. The heuristic values for each cell in the robot world are provided in _robot_world1_heuristic_values.txt_ (you do not need to compute them).

## The Exercises:

**Part 1 (Priority Queue): [2 points]** You must finish class __PriorityQueueRobotNav__.  Implementations for most of the methods are provided. I will be looking for the following to be included in your submission:
* _remove()_ method: This should remove a node from the __FRINGE__ based on priority. The *Node object* with the minimum *f_value* should be returned when this method is invoked. Node class is given with full implementation and you don't need to change anything. You should do the following to finish _remove()_ method:
  * Find the index of *Node object* with the minimum *f_value*
  * Eliminate that *Node object* from *self.priority_queue*
  * Finally, return that *Node object*
 
**Part 2 (Robot World): [6 points]** You must finish <span style="color:blue">class __RobotWorld__ </span>. Implementations for many of the methods are provided. I will be looking for the following to be included in your submission:
* _read_robot_world()_ method: This method should read the text file. You should do the following to finish this method:
  * Parse each symbol from the symbolic representation of the robot world (ie, last few lines in _"robot1.txt"_)
  * Create a *Node object*
* _get_heuristic_values()_ method: This method should parse the text file (ie, _"robot1_heuristic_values.txt"_) and fill in the matrix _'robot_2d_h'_. This matrix holds the heuristic values which will be used later.
* _plan_robot_motion()_ method: This method should do the following:
  * Get the h_value for _init_node_ from the 'robot_2d_h'. You can use 2D indexing of the form: 'robot_2d_h[init_node.y][init_node.x]'
  * Set the h_value, g_value, and f_value of 'init_node' by calling the appropriate methods
  * Mark 'robot_2d_visited[...][...]' as a visited location. For example, you can use a value of 1 to mark as visited. All 2D locations are marked as unvisited with a value of 0 by default
  * Set parent of *init_node* to None
 


Lastly, as always, use a Markup cell to put your name at the top of the file.

## Rubric :ballot_box_with_check:

## :white_check_mark: Grading: 
I will update the following rubric with your grade after you have completed the assignment.
### Rubric:
| Exercise #  | Points Awarded  | Notes |
| --------- | ------------------- | --------- |
| 1: Priority Queue::_remove()_                  |      /2  |    | 
| 2.1: Robot World::_read_robot_world()_           |      /2  |    |
| 2.2: Robot World::_get_heuristic_values()_       |      /2  |    | 
| 2.3: Robot World::_plan_robot_motion()_          |      /2  |    |  
| <b>Total                            |     /8 | </b>   |
