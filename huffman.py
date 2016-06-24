from Objects.Node import Node
from collections import Counter
from queue import PriorityQueue

if __name__ == "__main__":
    
    to_comprime_text = "That text will be compressed!"
    
    separated_chars = Counter(to_comprime_text)
    
    nodes = {}
        
    for char in separated_chars:
        nodes[char] = Node(separated_chars[char], char)
    
    q = PriorityQueue()
    
    for node in nodes:
        q.put((nodes[node].get_node_value(), node))
    
    print(q.queue)
    while q.qsize() > 1:
        left = q.get()
        right = q.get()
        
        node_representation = nodes[left[1]].get_node_representation() + nodes[right[1]].get_node_representation()
        node_value = nodes[left[1]].get_node_value() + nodes[right[1]].get_node_value()
        
        nodes[node_representation] = Node(node_value, node_representation)
        
        nodes[node_representation].set_left_node(nodes[left[1]])
        nodes[node_representation].set_right_node(nodes[right[1]])
        
        q.put((nodes[node_representation].get_node_value(), node_representation))
    
    
    
    
        