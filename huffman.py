from time import sleep
from Objects.Node import Node
from collections import Counter
from queue import PriorityQueue

def get_encoded_data(to_comprime_text, tree_nodes):
    
    binary_sequence = ""
    
    for char in to_comprime_text:
        actual_node = tree_nodes[char]
        
        binary_letter = ""
        while "True":
            if actual_node.get_back_node() == None:
                binary_sequence += binary_letter
                break
                
            binary_letter = str(actual_node.get_binary_node_value()) + binary_letter
            
            actual_node = actual_node.get_back_node()
            
    return binary_sequence

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
    
    to_comprime_text = "compressed"
    
    tree_nodes = create_tree(to_comprime_text)
    
    compressed_string = get_encoded_data(to_comprime_text, tree_nodes)
    
    print("Palavra a ser comprimida: " + to_comprime_text)
    print("Palavra comprimida: " + compressed_string)
    
    print("")
    
    for char in to_comprime_text:
        compressed_char = get_encoded_data(char, tree_nodes)
        print("Letra " + char + " comprimida: " + compressed_char)
    
    sleep(10)
