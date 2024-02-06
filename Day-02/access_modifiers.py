class MyClass:
    def __init__(self):
        self.public_variable = "This is a public variable"
        self._private_variable = "This is a private variable"
    
    def public_method(self):
        print("This is a public method")

    def _private_method(self):
        print("This is a private method")
    
    def __mangled_method(self):
        print("This method is mangled")

if __name__ == "__main__":

    obj = MyClass()
    print(obj.public_variable)  # Accessing public variable
    obj.public_method()         # Calling public method
    # obj.__mangled_method()
    obj._MyClass__mangled_method()


    print(obj._private_variable)  # Accessing private variable (conventionally discouraged)
    obj._private_method()         # Calling private method (conventionally discouraged)


