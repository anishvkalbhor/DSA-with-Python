def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    for i in range(n):
        for j in range(i):
            print(' ', end="")
        for j in range(2*(n-i)-1):
            print("*", end="")
        print()

generate_pyramid(5);