def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    traingle = []
    if n == 0:
        return []
    elif n == 1:
        return ['*']
    else:
        traingle.append('*' * n)
        for i in range(1, n-1):
            traingle.append('*' + ' ' * (n-2) + '*')
        traingle.append('*' * n)
        return traingle
    
print(generate_hollow_right_angled_triangle(5));