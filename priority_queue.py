# -------------- PriorityQueueRobotNav class definition -------------------------
from node import *

class PriorityQueueRobotNav:

    def __init__(self):
        self.priority_queue = []


    def is_empty(self):
        return len(self.priority_queue) == 0


    def get_size(self):
        return len(self.priority_queue)


    # insert a node into the FRINGE
    def insert(self, node):
        self.priority_queue.append(node)



    # remove a node from the FRINGE based on priority
    # node with minimum f_value should be returned when this method is invoked
    def remove(self):

        try:


            index_min_val = 0
            
            node          = None

            # -------- TO DO: a) Find the index of node object with the minimum 'f_value' 
            #                 b) Eliminate that node object from 'self.priority_queue'
            #                 c) finally, Return that node object


            # ------- YOUR CODE BEGINS HERE ------- 
            # Hint: it should be of the following form
            # for i in range(len(self.priority_queue)):

            #
            # ...
            # ...
            # ...
            #
            # ------- YOUR CODE ENDS HERE   -------- 



            return node

        except IndexError:

            print('exception in priority queue')



# ---------------- test ---------------------

node_a  = Node(x=0, y=0, f_value=10)
node_b  = Node(x=1, y=0, f_value=20)
node_c  = Node(x=2, y=0, f_value=30)


# create an object of PriorityQueueRobotNav()
my_priority_queue = PriorityQueueRobotNav()

# insert a bunch of Node objects into the priority queue
my_priority_queue.insert(node_a)
print("inserted node_a: ", node_a)
my_priority_queue.insert(node_b)
print("inserted node_b: ", node_b)
my_priority_queue.insert(node_c)
print("inserted node_c: ", node_c)

min_node_1 = my_priority_queue.remove()
print("Remove min Node: ", min_node_1)
min_node_2 = my_priority_queue.remove()
print("Remove min Node: ", min_node_2)

# -------------------------------------------



