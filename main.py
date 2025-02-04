# By: mathewn24
# Date: May 4, 2023


import time

# ----------------- Record the start time of the program -----------------
start = time.time()

# ----------------- Start of code -----------------

class Node:
    def __init__(self, k):
        self.key = k
        self.leftptr = None
        self.rightptr = None

def createBSTfromArray(ds):

    if not ds:
        return None
    # According to tutorial 10 in week 11: # The median A[n+1/2]
    # Get the median element of the array, and get the floor value.
    middle = len(ds) // 2
    # Set the root of the BST as the middle element of the sorted array.
    root = Node(ds[middle])
    # Create the left subtree by recursively calling the function on the values less than the middle.
    root.leftptr = createBSTfromArray(ds[:middle])
    # Create the right subtree by recursively calling the function on the values greater than the middle.
    root.rightptr = createBSTfromArray(ds[middle+1:])
    return root

# Extract the integers stored in the ds data file storing all the numbers.
with open("ds-half.txt", "r") as ds_file:
    ds_data = [int(line) for line in ds_file]

# We need to sort our data array in ascending order.
ds_data.sort()
root = createBSTfromArray(ds_data)

def getPredecessor(root, query):
    # Algorithm adapted from 
    # Lecture note 16 - Binary Search Trees (Static Version):
    # Step 1: Set p ← −∞ (p will contain the final answer at the end)
    predecessor = None
    
    # Step 2: Set u ← the root of T
    u = root

    while u is not None:
        # Step 4: If key of u = q, then set p to q, and return p
        if u.key == query:
            predecessor = query
            return predecessor
        # Step 5: If key of u > q, then set u to the left child (now u = nil if there is
        # no left child), and repeat (while loop).
        elif u.key > query:
            u = u.leftptr

        # Step 6: Otherwise, set p to the key of u, set u to the right child, and repeat (while loop).
        else:
            predecessor = u.key
            u = u.rightptr
    # Step 3: If u = nil, then return p       
    return predecessor

with open("qs-half.txt", "r") as qs_file:
    qs = [int(query.strip("qry ")) for query in qs_file]

#print("Length of queries are:", len(qs))

# Output the results to output.txt file.
with open("output.txt", "w") as output_file:
    for query in qs:
        pred = getPredecessor(root, query)
        if pred:
            output_file.write("{}\n".format(pred))
        else:
            output_file.write("no\n")

# ----------------- End of code -----------------

# ----------------- Record the end time of the program -----------------
end = time.time()
total_time = end-start

print(f"The execution time of the above program is : {total_time:.4f} seconds")

# Credit as some of the code was inspired by the resources in the following websites:
# 1. https://www.geeksforgeeks.org/sorted-array-to-balanced-bst/
# 2. https://stackoverflow.com/questions/36067787/successor-and-predecessor-binary-search-tree-python
