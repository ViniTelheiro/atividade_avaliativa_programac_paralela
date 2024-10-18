import numpy as np

def is_prime(n:int)->bool:
    """This function returns if a input number is a prime number.
    A a number n is a prime number if It's only divisible for 1 and himself.

    Args:
        n (int): The input integer number.

    Raises:
        ValueError: The type of n must be integer

    Returns:
        bool: True if the input number is a prime number else False
    """
    if "int" not in str(type(n)):
        raise ValueError("The type of n must be integer.")
    
    if n < 2:
        return False # 1 isn't a prime number
    
    n_list = np.arange(start=2, stop=n) # pick every number between 1 and n and put into a np array
    div_list = n % n_list # create a new list with the rest of the division between n and n_list
    
    return 0 not in div_list # If n is a Prime number, the list won't have zeros inside.

