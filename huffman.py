from Objects.Node import Node
from collections import Counter
from queue import PriorityQueue

def get_encoded_data(to_comprime_text, tree_nodes):
    
    binary_sequence = ""
    
    for char in to_comprime_text:
        actual_node = tree_nodes[char]
                
        while "True":
            if actual_node.get_binary_node_value() == None:
                break
                
            binary_sequence += str(actual_node.get_binary_node_value())
            
            actual_node = actual_node.get_back_node()
            
    return binary_sequence

def get_decoded_data(binary_sequence, tree_nodes):
    root_node = None
    decoded_string = ""
    
    for node in tree_nodes:
        if tree_nodes[node].get_binary_node_value() == None:
            root_node = tree_nodes[node]
        
    actual_node = root_node
        
    for bit in binary_sequence:
        bit = int(bit)
        
        if (binary_sequence[bit] == 1 and actual_node.get_right_node() != None):
            actual_node = actual_node.get_right_node()
        elif (binary_sequence[bit] == 0 and actual_node.get_left_node() != None):
            actual_node = actual_node.get_left_node()
        else:
            decoded_string += actual_node.get_node_representation()
            actual_node = root_node
            
    return decoded_string
    

def create_tree(to_comprime_text):
    separated_chars = Counter(to_comprime_text)
    
    nodes = {}
        
    for char in separated_chars:
        nodes[char] = Node(separated_chars[char], char)
    
    q = PriorityQueue()
    
    for node in nodes:
        q.put((nodes[node].get_node_value(), node))
    
    while q.qsize() > 1:
        left = q.get()
        right = q.get()
        
        nodes[left[1]].set_binary_node_value(0)
        nodes[right[1]].set_binary_node_value(1)
        
        node_representation = nodes[left[1]].get_node_representation() + nodes[right[1]].get_node_representation()
        node_value = nodes[left[1]].get_node_value() + nodes[right[1]].get_node_value()
        
        nodes[node_representation] = Node(node_value, node_representation)
        
        nodes[node_representation].set_left_node(nodes[left[1]])
        nodes[node_representation].set_right_node(nodes[right[1]])
        nodes[left[1]].set_back_node(nodes[node_representation])
        nodes[right[1]].set_back_node(nodes[node_representation])
        
        q.put((nodes[node_representation].get_node_value(), node_representation))
    
    return nodes

if __name__ == "__main__":
    
    to_comprime_text = "AAAAAABBBBBCCCCDDDEEF"
    
    tree_nodes = create_tree(to_comprime_text)
    
    compressed_string = get_encoded_data(to_comprime_text, tree_nodes)
    
    print(compressed_string)
    
    uncompressed_string = get_decoded_data(compressed_string, tree_nodes)
    
    print(uncompressed_string)