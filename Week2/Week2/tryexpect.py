def divide_and_access(a, b):
    try:
        result = a // b
        print("Result:", result)
        
        try:
            lst = [1, 2, 3]
            print("Accessing index 1:", lst[0])  # This will raise IndexError
        except IndexError:
            print("Handled inner IndexError: Invalid index access.")
    
    except ZeroDivisionError:
        print("Handled outer ZeroDivisionError: Cannot divide by zero.")

    finally:
        print("Outer finally block always runs.")

# Testing both types of exceptions
divide_and_access(6, 2)
print("---")
divide_and_access(6, 0)