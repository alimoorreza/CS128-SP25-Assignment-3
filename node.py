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

        str_var = "Node ( x="       + str(self.x)  		    + ", " + \
                          "y="      + str(self.y)  		    + ", " + \
                          "f="      + str(self.f_value)   + ", " + \
                          "g="      + str(self.h_value)   + ", " + \
                          "h="      + str(self.g_value)   + ", " + \
                          "type="   + self.node_type  	+ ", " + \
                          "color="  + self.color      + ")"
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



# --------- test -------------

node_a  = Node(x=0, y=0, f_value=1)
node_b  = Node(x=1, y=0, f_value=2)
node_c  = Node(x=2, y=0, f_value=3)

print(node_a)
print(node_b)
print(node_c)

#------------------------------
