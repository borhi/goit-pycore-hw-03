import re


def normalize_phone(phone_number):
    """
    Normalizes phone numbers to standard format for SMS campaigns.
    
    Args:
        phone_number (str): A string with phone number in any format.
    
    Returns:
        str: Normalized phone number containing only digits and '+' at the beginning.
             Automatically adds '+38' country code for Ukraine if missing.
    
    Examples:
        >>> normalize_phone("067\\t123 4567")
        '+380671234567'
        >>> normalize_phone("+380 44 123 4567")
        '+380441234567'
        >>> normalize_phone("380501234567")
        '+380501234567'
    """
    cleaned = re.sub(r'[^\d+]', '', phone_number)
    
    if cleaned.startswith('+'):
        return cleaned
    elif cleaned.startswith('380'):
        return '+' + cleaned
    else:
        return '+38' + cleaned


if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Normalized phone numbers for SMS campaign:", sanitized_numbers)
