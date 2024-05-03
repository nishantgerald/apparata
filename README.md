# Apparata: A Python Script for Generating Realistic Data

Apparata is a Python script that can be used to generate realistic data for a variety of purposes, such as testing, prototyping, and machine learning. It is primarily a wrapper for some functions from the [faker](https://faker.readthedocs.io/en/master/) library, which provides a wide range of data generation options. However, this script has additional capabilities that Faker does not provide. Apparata can generate a wide range of data types, including:

* Integers
* Floats
* First names
* Last names
* Addresses
* Phone numbers
* Datetimes
* Emails
* Latitudes and longitudes

## How to Install Apparata
```bash
pip install apparata
```

## How to Use Apparata

To use Apparata, simply import the script into your Python program and call the desired function. For example, to generate a random number with 10 digits, you would use the following code:

```python
import apparata

number = apparata.generate_numbers(10)
```
