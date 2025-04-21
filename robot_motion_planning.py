# Md Alimoor Reza
# Assistant Professor of Computer Science
# md.reza@drake.edu
# April, 2025



import pdb
import numpy as np
from graphics import *

VISITED     = 1
NOT_VISITED = 0

# successor actions from a node: in clockwise direction (UP, RIGHT, DOWN, LEFT)
actions     = ['UP', 'RIGHT', 'DOWN', 'LEFT']
x_shifts    = [ 0, +1,  0, -1]
y_shifts    = [-1,  0, +1,  0]



def parse_symbol(my_str):

    str_split = my_str.split('=')
    symbol    = str_split[1]
    return symbol


def make_rectangle(window, topleft_x, topleft_y, bottomright_x, bottomright_y, color):
    
    topleft_point     = Point(topleft_x, topleft_y)
    bottomright_point = Point(bottomright_x, bottomright_y)
    rectangle         = Rectangle(topleft_point, bottomright_point)
    rectangle.setFill(color)
    rectangle.draw(window)




# -------------- Node class definition -------------------------

class Node:
    
    def __init__(self, x, y, f_value=-1, node_type='empty_state', color="white"):
        self.x     			= x
        self.y     			= y
        self.f_value        = f_value   
        self.h_value        = 0                 # h_value is sufficient for best first search
        self.g_value        = 0                 # g_value is useful for A* search  (not used in best_first_search)
        self.node_type  	= node_type        
        self.color     		= color
        self.parent_node 	= None
        
        

    def __str__(self):

        str_var = "Node ( " + str(self.x)  		    + ", " + \
                              str(self.y)  		    + ", " + \
                              str(self.f_value)     + ", " + \
                              str(self.h_value)     + ", " + \
                              str(self.g_value)     + ", " + \
                              self.node_type  	    + ", " + \
                              self.color   		    + ")"
        return str_var

    def get_parent_node(self):

        return self.parent_node


    def set_parent_node(self, parent_node):

    	self.parent_node = parent_node
        

    # sufficient for best first search   
    def get_f_value(self):

        return self.f_value

    def set_f_value(self, f_value):

        self.f_value = f_value


    # sufficient for best first search   
    def get_h_value(self):

        return self.h_value

    def set_h_value(self, h_value):

        self.h_value = h_value



    # useful for A-star search  
    def get_g_value(self):

        return self.g_value


    def set_g_value(self, g_value):

        self.g_value = g_value


    def get_color(self):
        return self.color


    def set_color(self, color):
        self.color = color



# -------------- PriorityQueueRobotNav class definition -------------------------

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
    # node with minimum f_value should be return when this method will be invoked
    def remove(self):

        try:


            index_min_val = 0
            
            node          = None

            # -------- TO DO: a) Find the index of node object with the minimum 'f_value' 
            #                 b) Eliminate that node object from 'self.priority_queue'
            #                 c) finally, Return that node object

            # Hint: it should be of the following form
            # for i in range(len(self.priority_queue)):

                # ------- YOUR CODE BEGINS HERE ------- 
                #
                # ...
                # ...
                # ...
                #
                # ------- YOUR CODE ENDS HERE   -------- 



            return node

        except IndexError:

            print('exception in priority queue')




# -------------- RobotWorld class definition -------------------------

class RobotWorld:
    
    def __init__(self, width=11, height=5):
        self.width   	= width
        self.height  	= height
        self.node_list 	= []
        self.init_node  = None
        self.goal_node  = None
        

    def __str__(self):
        str_var = "RobotWorld ( " +  str(self.width)  + ", " + \
                              		 str(self.height)  + ")"
        return str_var
        

    def set_width(self, width):
    	self.width = width


    def set_height(self, height):
    	self.height = height


    def add_node_to_robot_world(self, node):
    	self.node_list.append(node)


    def set_init_node(self, node):
    	self.init_node = node


    def set_goal_node(self, node):
    	self.goal_node = node



    def show_robot_world(self, title):


        # drawing block
        block_width     = 100
        block_height    = 100

        win = GraphWin(title, self.width*block_width, self.height*block_height)

        #win.setCoords(0, 0, 550, 250)
            
        for row_index in range(self.height):

            for col_index in range(self.width):

                cur_node = self.node_list[row_index][col_index]

                x1       = block_width*col_index

                y1       = block_height*row_index

                x2       = x1 + block_width

                y2       = y1 + block_height
                
                make_rectangle(win, x1, y1, x2, y2, cur_node.get_color())



        # drawing text: init state
        x1          = block_width*self.init_node.x
        y1          = block_height*self.init_node.y
        x2          = x1 + block_width
        y2          = y1 + block_height
        text_point  = Point((x1+x2)//2, (y1+y2)//2)
        text        = Text(text_point, "init state")
        text.setTextColor("white")
        text.setFace("courier")  
        text.draw(win)


        # drawing text: goal state
        x1          = block_width*self.goal_node.x
        y1          = block_height*self.goal_node.y
        x2          = x1 + block_width
        y2          = y1 + block_height
        text_point  = Point((x1+x2)//2, (y1+y2)//2)
        text        = Text(text_point, "goal state")
        text.setTextColor("white")
        text.setFace("courier")  
        text.draw(win)

        return win



    def trace_path_to_origin(self, end_node):


        # -------- TO DO: backtrack from end_node by following its parent node


        # Hint: it should be of the following form
        # while end_node.get_parent_node() != None:
            
            # ------- YOUR CODE BEGINS HERE ------- 
            #
            # ...
            # ...
            # ...
            #
            # ------- YOUR CODE ENDS HERE   -------- 


        return None


    def get_heuristic_values(self, file_name):

     	with open(file_name[:-4] + "_heuristic_values.txt", 'r') as f:

            all_lines 								= f.readlines()
            heuristic_function_name  				= all_lines[0].rstrip("\n")
            all_lines 								= all_lines[1:]




            # --------- initialize the matrix of h-values ---------
            height 			  = len(all_lines)
            width 			  = len(all_lines[0])
            robot_2d_h 	      = np.zeros((height, width))


            # --------- define the 2d grid that will keep track of the visited node objects
            robot_2d_visited  = np.zeros((height, width))




            # -------- TO DO: a) Parse the text file (eg, "robot1_heuristic_values.txt") and
            #                    fill in the matrix 'robot_2d_h'. This matrix holds the heuristic 
            #                    values which will be used later
            
            # ------- YOUR CODE BEGINS HERE ------- 
            #
            # ...
            # ...
            # ...
            #
            # ------- YOUR CODE ENDS HERE   -------- 





            return robot_2d_h, robot_2d_visited
   	


    def read_robot_world(self, file_name):


        node_color_code =  {'empty_state':      'white',
                            'obstacle_state':   'black',
                            'init_state':       'red',
                            'goal_state':       'green'}


        with open(file_name, 'r') as f:

            robot_2d_h, robot_2d_visited = self.get_heuristic_values(file_name)

            all_lines                               = f.readlines()
            dict_symbol_value                       = {}
            dict_symbol_value[parse_symbol(all_lines[0].rstrip("\n"))] = 'empty_state'
            dict_symbol_value[parse_symbol(all_lines[1].rstrip("\n"))] = 'obstacle_state'    
            dict_symbol_value[parse_symbol(all_lines[2].rstrip("\n"))] = 'init_state'
            dict_symbol_value[parse_symbol(all_lines[3].rstrip("\n"))] = 'goal_state'

            height                                  = int(parse_symbol(all_lines[4].rstrip("\n")))
            width                                   = int(parse_symbol(all_lines[5].rstrip("\n")))
            all_lines                               = all_lines[6:]
            

            self.set_width(width)
            self.set_height(height)

            
            # ---- initialize the self.node_list 
            # ---- this is a 2d list-of-list containing objects from 'Node' class
            for row_index in range(height):
                empty_node_list = []
                for col_index in range(width):
                    empty_node_list.append(None)
                self.node_list.append(empty_node_list)




            for row_index in range(0, len(all_lines)):

                cur_line  = all_lines[row_index]

                str_split = cur_line.rstrip("\n").split(',')

                for col_index in range(0, len(str_split)):


                    # -------- TO DO: a) Parse each symbol from the symbolic representation of the robot world (ie, last few lines in "robot1.txt")
                    #                 b) Create a Node object
                    
                    # ------- YOUR CODE BEGINS HERE ------- 
                    # Hint: a) Use the two dictionaries ie, 'dict_symbol_value' and 'node_color_code' 
                    #          to figure out the appropiate values
                    #       b) Replace the 'None' with appropriate thing in following four lines
                    
                    cur_symbol          = None
                    cur_state           = None
                    cur_color           = None
                    cur_node_object     = None

                    # ------- YOUR CODE ENDS HERE   ------- 
                    




                    # -------- add the node into the list
                    self.node_list[row_index][col_index] = cur_node_object


                    # -------- set init_node and goal_node
                    if cur_state == 'init_state':
                        self.set_init_node(cur_node_object)                        

                    elif cur_state == 'goal_state':
                        self.set_goal_node(cur_node_object)
                        

            return robot_2d_h, robot_2d_visited



    def plan_robot_motion(self, robot_2d_h, robot_2d_visited, motion_planning_method):

        init_node           = self.init_node
        goal_node           = self.goal_node

        if (init_node.x == goal_node.x) and (init_node.y == goal_node.y):
            return init_node


        fringe = PriorityQueueRobotNav()


        # -------- insert 'init_node' to the FRINGE -------- 

        # -------- TO DO: a) Get the h_value for init_node from the 'robot_2d_h' 
        #                    you can use 2D indexing of the form: 'robot_2d_h[init_node.y][init_node.x]'
        #                 b) Set the h_value, g_value, and f_value of 'init_node' by calling the appropriate methods 
        #                 c) Mark 'robot_2d_visited[...][...]' as a visited location. For example, you can use a value of 1 
        #                    to mark as visited. All 2D locations are marked as unvisited with a value of 0 by default
        #                 d) Set parent of init_node to None
    

        # ------- YOUR CODE BEGINS HERE ------- 
        # Hint: It should be of the following form:

        # h_value = ...
        # g_value = ...
        # f_value = ...

        # init_node.set_******
        # init_node.set_******
        # init_node.set_******

        # robot_2d_visited[...][...] = ...

        init_node.set_parent_node(None)
        fringe.insert(init_node)

        

        # -------- loop through the FRINGE until it is empty -------- 
        while not fringe.is_empty():

            # -------- extract the node 's_node' from the FRINGE (based on the lowest f_value)
            # ------- YOUR CODE IN THE LINE BELOW ------- 
            # s_node = ...


            # if 's_node' is the goal_node then return this node
            if (s_node.x == goal_node.x) and (s_node.y == goal_node.y):
                return s_node


            # -------- insert all the successor nodes that are reachable from 's_node'

            for action_index in range(len(actions)):

                successor_x_coord = s_node.x + x_shifts[action_index]
                successor_y_coord = s_node.y + y_shifts[action_index]


                # -------- the successor node falls within the boundary of 2d grid
                # -------- check for validity of the successor candidate
                #               1) NOT visited before
                #               2) NOT an obstacle node


                if (successor_x_coord >= 0 and successor_x_coord < self.width) and (successor_y_coord >= 0 and successor_y_coord < self.height):

                    # ------- YOUR CODE IN THE LINE BELOW ------- 
                    # successor_node = ...


                    if (robot_2d_visited[successor_y_coord][successor_x_coord] == NOT_VISITED) and \
                        (successor_node.node_type != 'obstacle_state'):
                    
                        # -------- insert the successor_node into the FRINGE  -------- 

                        # -------- TO DO: a) Get the h_value for successor_node from the 'robot_2d_h' 
                        #                    you can use 2D indexing of the form: 'robot_2d_h[...][...]'
                        #                 b) Set the h_value, g_value, and f_value of 'successor_node' by calling the appropriate methods 
                        #                 c) Mark 'robot_2d_visited[...][...]' as a visited location. For example, you can use a value of 1 
                        #                    to mark as visited. All 2D locations are marked as unvisited with a value of 0 by default
                        #                 d) Set parent of 'successor_node' to 's_node'
                    

                        # ------- YOUR CODE BEGINS HERE ------- 
                        # Hint: It should be of the following form:

                        #h_value = ...
                        #g_value = ... 
                        #f_value = ...

                        #successor_node.set_******
                        #successor_node.set_******
                        #successor_node.set_******

                        #robot_2d_visited[...][...] = ...

                        successor_node.set_parent_node(s_node)
                        fringe.insert(successor_node)


        return None


def main():
    

    #motion_planning_method = "a_star_search"    
    motion_planning_method = "best_first_search"    


    robotworld_obj 	        = RobotWorld()


    # ------------- read 2D robot world information from the given input text file --------------
    file_name 		                = "robot_world1.txt"
    robot_2d_h, robot_2d_visited 	= robotworld_obj.read_robot_world(file_name)
    


    # ------------- show the 2D robot world ---------------------
    win_before = robotworld_obj.show_robot_world('Robot World (before motion planning)')
    


    # ------------- compute the path planning for the robot ---------------------       
    destination_node = robotworld_obj.plan_robot_motion(robot_2d_map, robot_2d_h, robot_2d_visited, motion_planning_method)
    robotworld_obj.trace_path_to_origin(destination_node)



    
    
    # ------------- show the 2D robot world ---------------------

    win_after = robotworld_obj.show_robot_world('Robot World (after motion planning)')

    pdb.set_trace()

    del win_before
    del win_after

    
main()