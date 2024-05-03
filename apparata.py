#!/usr/bin/env python3
import random
import pandas as pd
from faker import Faker
fake = Faker()

def generate_numbers(ndigits: int) -> int:
    """
    Function that generates a random number given the number of digits

    Args:
        ndigits (int): The number of digits in the random number

    Returns:
        int: A random number with the specified number of digits
    """

    # Check if the number of digits is valid
    if ndigits <= 0:
        raise ValueError("The number of digits must be greater than 0")

    # Generate a random number with the specified number of digits
    number = random.randint(10**(ndigits-1), 10**ndigits-1)

    # Return the random number
    return number

def generate_first_name() -> str:
    """
    Function that generates a random first name

    Returns:
        str: Random first name
    """
    first_name = fake.first_name()
    return first_name

def generate_last_name() -> str:
    """
    Function that generates a random last name

    Returns:
        str: Random last name
    """
    last_name = fake.last_name()
    return last_name

def generate_address() -> str:
    """
    Function that generates a random address

    Returns:
        str: A random address
    """
    address = fake.address()
    return address

def generate_phone_number() -> str:
    """
    Function that generates a random phone number

    Returns:
        str: A random phone number
    """
    # Generate a random 10 digit phone number
    phone_number = ''.join(random.choice('0123456789') for i in range(10))

    # Add hyphens to the phone number
    phone_number = phone_number[:3] + '-' + phone_number[3:6] + '-' + phone_number[6:]
    return phone_number

def generate_datetime(start_date: str) -> str:
    """
    Function that generates a random timestamp

    Args:
        start_date (str): The start date of the timestamp from the past (eg: -30d) [Use strptime representations for date, month, year, etc.] 

    Returns:
        str: A random timestamp
    """
    datetime = fake.past_datetime(start_date=start_date)
    return datetime


def generate_email() -> str:
    """
    Function that generates a random email address

    Returns:
        str: A random email address
    """
    email = fake.ascii_free_email()
    return email

def generate_latlong(country_code: str) -> tuple[int, int, str, str, str]:
    """
    Function that generates a random latitide and longitude in the given country, which is guaranteed to exist

    Args:
        country_code (str): The country code of the location. Use country codes from https://www.nationsonline.org/oneworld/country_code_list.htm

    Returns:
        tuple[int, int, str, str, str]: A tuple containing the latitude, longitude, city, and timezone
    """
    location = fake.local_latlng(country_code=country_code)
    latitute = location[0]
    longitude = location[1]
    city = location[2]
    timezone = location[4]
    return latitute, longitude, city, timezone 

def main():
    pass

if __name__ == "__main__":
    main()