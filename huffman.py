from Objects.Node import Node
from collections import Counter

if __name__ == "__main__":
    
    to_comprime_text = "That text will be compressed!"
    
    separated_chars = Counter(to_comprime_text)
        
    for char in separated_chars:
        node = Node(separated_chars[char], char)
    
    
    
    
        