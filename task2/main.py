import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
   
    pattern = r'\b\d+\.\d+\b'

    # Use re.finditer to find all matches of the pattern in the text
    # and yield each match as a float. 
    for match in re.finditer(pattern, text):
        # Convert the matched string to a float and yield it
        yield float(match.group(0))

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    
    total_sum = 0.0
    # # Call the generator function to get the numbers from the text
    # and iterate through the generator to calculate the total sum. 
    numbers_generator = func(text)
    for number in numbers_generator:
        total_sum += number
    return total_sum

# Example usage  
text = """Main income for the month is
    1000.01 as reported in the financial statement., 
    and additional income 27.45  
    and 324.00 dollars."""
total_income = sum_profit(text, generator_numbers)

print(f"Total income: {total_income}")
