def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    # Your code here
    number = 1
    for i in range(0, n):
        for j in range(0, i+1):
            print(number, end=" ")
            number += 1
        print()

generate_floyds_triangle(5);
