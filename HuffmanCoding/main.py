from typing import Optional

class HuffmanTree:
    def __init__(self, value: Optional[str] = None, frequency: int = 0):
        self.value: Optional[str] = value
        self.frequency: int = frequency
        self.left_child: Optional[HuffmanTree] = None
        self.right_child: Optional[HuffmanTree] = None

    def is_leaf(self) -> bool:
        return self.value is not None
    
    
