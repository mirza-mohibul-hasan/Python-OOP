class MyClass:
    def __init__(self, data):
        self.data = data

    def modify_list(self, lst):
        lst.append(4)  # This modifies the original list

    def modify_string(self, string):
        string += " World!"  # This creates a new string object

# Creating an instance of MyClass
obj = MyClass([1, 2, 3])
print("Original List:", obj.data)  # Output: Original List: [1, 2, 3]

# Calling modify_list method
obj.modify_list(obj.data)
print("After modify_list:", obj.data)  # Output: After modify_list: [1, 2, 3, 4]

str="Hello"
# Calling modify_string method
obj.modify_string(str)
print("After modify_string:", str) # Output: "Hello"
