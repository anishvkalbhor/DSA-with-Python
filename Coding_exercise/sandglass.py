def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    # ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']
    # Your code here
    for i in range(n):
        for j in range(i+1):
            print(" ", end="")
        for j in range(i, n-1):
            print("*", end="")
        for j in range (i, n):
            print("*", end="")
        print()
    for i in range(n):
        for j in range(i, n):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")
        for j in range(i):
            print("*", end="")
        print()

generate_sandglass(3);