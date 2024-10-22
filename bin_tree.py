class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.val) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search_largest(root):
    if root is None:
        return None
    
    while root.right is not None:
        root = root.right

    return root.val

def search_smallest(root):
    if root is None:
        return None
    
    while root.left is not None:
        root = root.left

    return root.val
    
# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

# Пошук максимального значення
max_result = search_largest(root)
if max_result:
    print(f"У дереві знайдено максимальне значення {max_result}")
else:
    print(f"У дереві не знайдено значення {max_result}")

# Пошук мінімального значення
min_result = search_smallest(root)
if min_result:
    print(f"У дереві знайдено мінімальне значення {min_result}")
else:
    print(f"У дереві не знайдено значення {min_result}") 

