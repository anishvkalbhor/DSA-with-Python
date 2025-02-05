def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    if n == 0:
        return []
    elif n == 1:
        return ['*']
    else:
        square = []
        square.append('*' * n)
        for i in range(1, n-1):
            square.append('*' + ' ' * (n-2) + '*')
        square.append('*' * n)
        return square

print(generate_hollow_square(5));