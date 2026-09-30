import random
import re
import time


def generate_unique_email():
    """
    Creates a new email address every time using the current time.
    This way the 'Register User' test never fails with
    'Email Address already exist!' when we run it again.
    """
    unique_number = int(time.time())
    return f"testuser{unique_number}@example.com"


def generate_random_name():
    """Creates a simple random name like 'User4821'."""
    unique_number = random.randint(1000, 9999)
    return f"User{unique_number}"


def extract_price_number(price_text: str) -> int:
    """
    Turns a price text into a plain number so we can do maths with it.
    Example: 'Rs. 500'  ->  500
    """
    digits = re.findall(r"\d+", price_text)
    return int("".join(digits))
