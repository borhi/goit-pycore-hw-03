import random


def get_numbers_ticket(min, max, quantity):
    """
    Generates a set of unique random numbers for lottery tickets.
    
    Args:
        min (int): Minimum possible number in the set (not less than 1).
        max (int): Maximum possible number in the set (not more than 1000).
        quantity (int): Number of numbers to select (value between min and max).
    
    Returns:
        list: A sorted list of unique random numbers. Returns empty list if parameters
              don't meet the constraints.
    
    Examples:
        >>> numbers = get_numbers_ticket(1, 49, 6)
        >>> len(numbers) == 6
        True
        >>> numbers == sorted(numbers)
        True
    """
    if (min < 1 or max > 1000) or (min >= max) or (quantity < 1 or quantity > (max - min + 1)):
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)


if __name__ == "__main__":
    print("Testing get_numbers_ticket() function:\n")
    
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Your lottery numbers:", lottery_numbers)
    
    lottery_numbers = get_numbers_ticket(1, 36, 5)
    print("Your lottery numbers:", lottery_numbers)
    
    print("\nEdge cases:")
    print("Invalid min (0):", get_numbers_ticket(0, 49, 6))
    print("Invalid max (1001):", get_numbers_ticket(1, 1001, 6))
    print("Invalid quantity (too large):", get_numbers_ticket(1, 10, 20))
    print("Invalid quantity (0):", get_numbers_ticket(1, 49, 0))
    print("Min >= max:", get_numbers_ticket(50, 49, 6))
