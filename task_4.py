from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """
    Determines which colleagues need to be congratulated on their birthdays
    in the next 7 days, including today.
    
    Args:
        users (list): List of dictionaries with keys 'name' (str) and 'birthday' (str in format 'YYYY.MM.DD').
    
    Returns:
        list: List of dictionaries with keys 'name' and 'congratulation_date' (str in format 'YYYY.MM.DD').
              If birthday falls on weekend, congratulation date is moved to next Monday.
    
    Examples:
        >>> users = [{"name": "John Doe", "birthday": "1985.01.23"}]
        >>> result = get_upcoming_birthdays(users)
        >>> 'name' in result[0] and 'congratulation_date' in result[0]
        True
    """
    today = datetime.today().date()
    upcoming = []
    
    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except (ValueError, KeyError) as e:
            print(f"Warning: Skipping user '{user.get('name', 'Unknown')}' due to invalid date format: {e}")
            print()
            continue

        try:
            birthday_this_year = birthday.replace(year=today.year)
        except (ValueError, KeyError) as e:
            print(f"Warning: Skipping user '{user.get('name', 'Unknown')}' due to invalid date: {e}")
            print()
            continue
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        days_until_birthday = (birthday_this_year - today).days
        
        if 0 <= days_until_birthday < 7:
            congratulation_date = birthday_this_year
            
            weekday = congratulation_date.weekday()

            if weekday > 4:
                congratulation_date += timedelta(days=7-weekday)
            
            upcoming.append({
                "name": user.get("name", "Unknown"),
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming


if __name__ == "__main__":
    from datetime import datetime
    
    today = datetime.today().date()
    print(f"Today is: {today.strftime('%Y.%m.%d (%A)')}\n")
    
    users = [
        {"name": "Alice", "birthday": "1990.02.08"},
        {"name": "Bob", "birthday": "1985.02.09"},
        {"name": "Charlie", "birthday": "1992.02.13"},
        {"name": "Diana", "birthday": "1988.02.15"},
        {"name": "Eve", "birthday": "1995.02.16"},
        {"name": "Frank", "birthday": "1980.02.01"},
        {"name": "George (leap year)", "birthday": "2020.02.29"},
        {"name": "Helen (invalid format)", "birthday": "1990-02-08"},
        {"name": "Ivan (invalid date)", "birthday": "1987.11.31"},
    ]
    
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("List of congratulations for this week:", upcoming_birthdays)
    print()
    
    if upcoming_birthdays:
        print("Detailed view:")
        for item in upcoming_birthdays:
            congrat_date = datetime.strptime(item['congratulation_date'], '%Y.%m.%d')
            weekday = congrat_date.strftime('%A')
            print(f"  {item['name']}: {item['congratulation_date']} ({weekday})")
