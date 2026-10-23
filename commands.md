# Terminal Record: Harvest Table Catering

## 1. Building the project
```
cd ~/ism3232
mkdir ism3232-midterm
cd ism3232-midterm 

py -m venv .venv
va  
pip install pytest ruff
pip freeze > requirements.txt

touch business_rules.py main.py commands.md README.md
mkdir tests 
touch tests/__init__.py tests/test_business_rules.py 

echo '.venv/' > .gitignore 
echo '__pycache__/' >> .gitignore 

git init
git branch -M main 
ga
gcmsg "midterm: part 1 - project setup"
git remote add origin https://github.com/anant-gaan/ism3232-midterm.git 
git push -u origin main 
```

## 2. The virtual environment
```
which python3
```

```
/home/anant/ism3232/ism3232-midterm/.venv/bin/python3
```

The output shows that my virtual environment is active because Python is running it from the project's .venv folder.

## 3. The project structure
```
tree2
```

```
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

__pycache__ does not appear in my GitHub repository because it is excluded by .gitignore but it exists because Python auto-generates cached files.

## 4. Every function and test
```
rg 'def '
```

```
business_rules.py
14:def calculate_food_cost(guest_price: float, guests: int) -> float:
19:def get_event_discount(guests: int, nonprofit: bool = False) -> float:
29:def calculate_event_total(
41:def needs_signoff(total: float) -> bool:
46:def needs_second_chef(guests: int, total: float) -> bool:
51:def total_booked(events: list) -> float:
62:def largest_event(events: list) -> str:
76:def format_event_line(

tests/test_business_rules.py
13:def test_calculate_food_cost_before_discount():
17:def test_discount_below_25_guests():
21:def test_discount_25_guests():
25:def test_service_fee_at_500():
29:def test_service_fee_uses_discounted_cost():
33:def test_discount_99_guests_nonprofit():
37:def test_discount_100_guests_not_nonprofit():
41:def test_discount_100_guests_nonprofit():
45:def test_event_total_with_service_fee():
49:def test_event_total_without_service_fee():
53:def test_signoff_at_2500():
57:def test_signoff_above_2500():
61:def test_second_chef_at_80_guests():
65:def test_second_chef_above_80_guests():
69:def test_second_chef_below_3000_total():
73:def test_second_chef_at_3000_total():
77:def test_total_booked_two_events():
85:def test_total_booked_empty_list():
89:def test_largest_event_two_events():
102:def test_largest_event_tied_events():
110:def test_largest_event_empty_list():
114:def test_format_event_line_no_no():
119:def test_format_event_line_yes_yes():
124:def test_format_event_line_yes_no():
129:def test_format_event_line_no_yes():
```

business_rules.py defines 8 functions, and tests/test_business_rules.py defines 25 tests.

## 5. Which files print
```
rg -l 'print'
```

```
commands.md
main.py
```

main.py prints the event report, business_rules.py is not in that list because there are only functions on that file which return values.

## 6. The commit history
```
git log --oneline
```

```
783645d (HEAD -> main, origin/main) midterm: part 4 - tests
8211524 midterm: part 3 - event report
8531c95 midterm: part 2 - functions 7-8 and 7 tests
9598f69 midterm: part 2 - functions 4-6 and 8 tests
f3dca58 midterm: part 2 - first 3 functions and 9 tests
7bcdfa1 midterm: part 1 - project setup
```

When I ran git log --oneline, it showed 6 commits.