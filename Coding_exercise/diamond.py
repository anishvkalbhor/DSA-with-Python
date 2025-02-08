def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here
    for i in range(n-1):
        for j in range(i, n):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        for j in range(i+1):
            print("*", end="")
        print()

    for i in range(n):
        for j in range(i+1):
            print(" ", end="")
        for j in range(i, n-1):
            print("*", end="")
        for j in range(i, n):
            print("*", end="")
        print()

generate_diamond(5);