class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rect = Rectangle(10, 5)
for attribute in rect:
    print(attribute)

# Output:
# {'length': 10}
# {'width': 5}
