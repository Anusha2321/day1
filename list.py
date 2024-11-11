# Python Program: List Operations and Functions

# Initialize example lists
list1 = [1, 2, 3, 4, 5]
list2 = ["apple", "banana", "cherry"]

print("Original list1:", list1)
print("Original list2:", list2)

# 1. **Adding Elements**:
# Append a single element
list1.append(6)
print("After appending 6:", list1)

# Extend list1 with another list
list1.extend([7, 8, 9])
print("After extending with [7, 8, 9]:", list1)

# Insert an element at a specific index
list1.insert(1, "inserted")
print("After inserting 'inserted' at index 1:", list1)

# 2. **Removing Elements**:
# Remove a specific element
list1.remove("inserted")
print("After removing 'inserted':", list1)

# Pop an element by index
popped_element = list1.pop(2)
print("After popping element at index 2:", list1)
print("Popped element:", popped_element)

# Clear the entire list
temp_list = list2.copy()  # Copy for reset demonstration
temp_list.clear()
print("After clearing list2:", temp_list)

# 3. **Finding Elements**:
# Find the index of an element
index_of_banana = list2.index("banana")
print("Index of 'banana' in list2:", index_of_banana)

# Count occurrences of an element
count_of_apple = list2.count("apple")
print("Count of 'apple' in list2:", count_of_apple)

# 4. **Sorting and Reversing**:
numbers = [4, 2, 8, 1, 7]
print("Unsorted numbers:", numbers)

# Sort the list in ascending order
numbers.sort()
print("Sorted numbers:", numbers)

# Sort the list in descending order
numbers.sort(reverse=True)
print("Numbers sorted in descending order:", numbers)

# Reverse the list
list2.reverse()
print("Reversed list2:", list2)

# 5. **List Comprehension**:
# Square each number in list1
squares = [x ** 2 for x in list1 if isinstance(x, int)]
print("Squares of numbers in list1:", squares)

# Filter and double even numbers in list1
doubled_evens = [x * 2 for x in list1 if isinstance(x, int) and x % 2 == 0]
print("Doubled even numbers in list1:", doubled_evens)

# 6. **Copying Lists**:
# Copy list1 to a new list
list_copy = list1.copy()
print("Copied list:", list_copy)

# 7. **List Length and Membership**:
# Length of list1
print("Length of list1:", len(list1))

# Check if an element is in the list
print("Is 3 in list1?", 3 in list1)
print("Is 10 in list1?", 10 in list1)

# 8. **Nested Lists**:
nested_list = [["a", "b"], [1, 2, 3], ["apple", "banana"]]
print("Nested list:", nested_list)

# Access an element in a nested list
print("Element at [1][2] in nested_list:", nested_list[1][2])

# Flatten nested list using a list comprehension
flattened = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened)
