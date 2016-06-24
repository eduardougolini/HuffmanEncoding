
class Node:
    
    def __init__(self, node_value, node_representation):
        self.node_value = node_value
        self.node_representation = node_representation
        self.back_node = None
        self.left_node = None
        self.right_node = None
        self.binary_value = None
        
    def set_binary_node_value(self, binary_value):
        self.binary_value = binary_value;
        
    def get_binary_node_value(self):
        return self.binary_value
        
    def get_node_value(self):
        return self.node_value
    
    def get_node_representation(self):
        return self.node_representation
    
    def set_back_node(self, back_node):
        self.back_node = back_node
        
    def get_back_node(self):
        return self.back_node
    
    def set_left_node(self, left_node):
        self.left_node = left_node
        
    def get_left_node(self):
        return self.left_node
    
    def set_right_node(self, right_node):
        self.right_node = right_node
        
    def get_right_node(self):
        return self.right_node