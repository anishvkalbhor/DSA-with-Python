# def generate_triangle(n):
#     """
#     Function to return a right-angled triangle of '*' of side n as a list of strings.
    
#     Parameters:
#     n (int): The height and base of the triangle.
    
#     Returns:
#     list: A list of strings where each string represents a row of the triangle.
#     """
#     # Your code here
    
#     for i in range(n):
#         print('*' * (i+1))

# generate_triangle(5);

def generate_right_angled_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    for i in range(n):
        for j in range(i, n):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()

generate_right_angled_triangle(5);