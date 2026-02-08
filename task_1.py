from datetime import datetime


def get_days_from_today(date):
    """
    Calculates the number of days between a given date and the current date.
    
    Args:
        date (str): A string representing a date in the format 'YYYY-MM-DD' (e.g., '2020-10-09').
    
    Returns:
        int: The number of days from the given date to the current date.
             If the given date is later than the current date, the result will be negative.
    
    Raises:
        ValueError: If the date format is incorrect.
    
    Examples:
        >>> get_days_from_today("2021-10-09")
        -157
        >>> get_days_from_today("2021-01-01")
        124
    """
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.today().date()
        difference = current_date - given_date
        return difference.days
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected format 'YYYY-MM-DD', got: '{date}'") from e


if __name__ == "__main__":
    print("Testing get_days_from_today() function:\n")
    
    test_date_1 = "2021-01-01"
    try:
        result_1 = get_days_from_today(test_date_1)
        print(f"Date: {test_date_1}")
        print(f"Days from given date to today: {result_1}\n")
    except ValueError as e:
        print(f"Error: {e}\n")
    
    test_date_2 = "2026-12-31"
    try:
        result_2 = get_days_from_today(test_date_2)
        print(f"Date: {test_date_2}")
        print(f"Days from given date to today: {result_2}\n")
    except ValueError as e:
        print(f"Error: {e}\n")
    
    current_date_str = datetime.today().strftime('%Y-%m-%d')
    try:
        result_3 = get_days_from_today(current_date_str)
        print(f"Date: {current_date_str} (today)")
        print(f"Days from given date to today: {result_3}\n")
    except ValueError as e:
        print(f"Error: {e}\n")
    
    test_date_4 = "2021/10/09"
    try:
        result_4 = get_days_from_today(test_date_4)
        print(f"Date: {test_date_4}")
        print(f"Days from given date to today: {result_4}\n")
    except ValueError as e:
        print(f"Error: {e}\n")
