# ISM3232 Midterm: Harvest Table Catering

**Name:** Anant Gaan 
- **Version:** Version Beta 
- **Date:** 10/23/2026

## What This Program Does
The program I've written creates an event report for Harvest Table Catering. It calculates the total cost of each event based on the number of guests and price per guest. My program also applies discounts and service fees when relevant according to the business rules and checks whether an event needs a sign-off or a second chef. The report conveys information such as total booked, average event total, and largest event total.

## Business Rules
1. Food cost is to be calculated as the number of guests times the price per guest
2. Events with fewer than 25 guests receive no discount. Events with guests between 25-99 receive a discount of 5%. Events with 100 guests or more receive a discount of 12%.
3. The 12% discount, however, is only applicable for registered nonprofits. Any other event of 100 guests or more receives the standard discount of 5%.
4. A service fee of $75 is added when the discounted amount is $500 or less.
5. If an event has a total of over $2500 it needs a manager's sign-off
6. An event needs a second chef when it has more than 80 guests or when the total is $3000 or more. 

## How to Run
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test
```
ruff format .
ruff check .
pytest -v
```

I wrote 25 tests.

## Files in This Repository
1. business_rules.py -> contains 8 functions representing the 6 business rules
2. main.py -> contains the entire client list and also prints out the event report 
3. commands.md -> contains the terminal record
4. README.md -> contains the 7 section README
5. requirements.txt -> contains the packages needed to run the project
6. .gitignore -> contains .venv/ and __pycache__/
7. tests/__init__.py -> is an empty file 
8. tests/test_business_rules.py -> contains the 25 pytests for the business rules

## AI Use Statement
I did not use AI