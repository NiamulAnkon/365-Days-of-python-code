class BinaryserchTreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryserchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryserchTreeNode(data)
    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.right.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
    def pre_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        
        elements.append(self.data)

        return elements
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0

    
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.right.delete(max_val)


        return self

def build_tree (elements):
    print("Building tree with these elements:",elements)
    root = BinaryserchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal())
