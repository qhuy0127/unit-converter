#!/usr/bin/env python3
"""
Unit Converter - A simple command-line tool to convert between different units of measurement.
Supports temperature (Celsius/Fahrenheit), distance (Kilometers/Miles), and weight (Kilograms/Pounds).
"""

import argparse
import sys

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def kilometers_to_miles(kilometers):
    """Convert Kilometers to Miles."""
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    """Convert Miles to Kilometers."""
    return miles * 1.60934

def kilograms_to_pounds(kilograms):
    """Convert Kilograms to Pounds."""
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    """Convert Pounds to Kilograms."""
    return pounds * 0.453592

def main():
    parser = argparse.ArgumentParser(
        description='Convert between different units of measurement.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        'value',
        type=float,
        help='The value to convert'
    )
    
    parser.add_argument(
        'conversion',
        choices=['c2f', 'f2c', 'km2mi', 'mi2km', 'kg2lb', 'lb2kg'],
        help='''Conversion type:
c2f   - Celsius to Fahrenheit
f2c   - Fahrenheit to Celsius
km2mi - Kilometers to Miles
mi2km - Miles to Kilometers
kg2lb - Kilograms to Pounds
lb2kg - Pounds to Kilograms'''
    )

    try:
        args = parser.parse_args()
        
        # Dictionary mapping conversion types to their respective functions and unit labels
        conversions = {
            'c2f': (celsius_to_fahrenheit, '°C', '°F'),
            'f2c': (fahrenheit_to_celsius, '°F', '°C'),
            'km2mi': (kilometers_to_miles, 'km', 'mi'),
            'mi2km': (miles_to_kilometers, 'mi', 'km'),
            'kg2lb': (kilograms_to_pounds, 'kg', 'lb'),
            'lb2kg': (pounds_to_kilograms, 'lb', 'kg')
        }
        
        # Get the conversion function and units
        convert_func, from_unit, to_unit = conversions[args.conversion]
        
        # Perform the conversion
        result = convert_func(args.value)
        
        # Display the result
        print(f"\nConversion Result:")
        print(f"{args.value} {from_unit} = {result:.2f} {to_unit}")
        
    except argparse.ArgumentError as e:
        print(f"Error: {str(e)}")
        parser.print_help()
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Please enter a valid number")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()