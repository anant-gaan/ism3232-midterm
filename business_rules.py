# Named Constants
MIN_DISCOUNT_GUESTS = 25
LARGE_EVENT_GUESTS = 100
NO_DISCOUNT = 0.0
STANDARD_DISCOUNT = 0.05
NONPROFIT_DISCOUNT = 0.12
SERVICE_FEE = 75.0
SERVICE_FEE_LIMIT = 500.0
SIGNOFF_LIMIT = 2500.0
SECOND_CHEF_GUEST_LIMIT = 80
SECOND_CHEF_TOTAL_LIMIT = 3000.0


def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Returns the food cost without any discounts (rule 1)."""
    return guest_price * guests


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Returns the discount rate as a decimal, so 5% is 0.05 (rule 2 and 3)."""
    if guests < MIN_DISCOUNT_GUESTS:
        return NO_DISCOUNT
    elif guests >= LARGE_EVENT_GUESTS and nonprofit:
        return NONPROFIT_DISCOUNT
    else:
        return STANDARD_DISCOUNT


def calculate_event_total(
    guest_price: float, guests: int, nonprofit: bool = False
) -> float:
    """Returns the event total for one event: the discounted cost plus the service fee when it applies (rule 4)."""
    food_cost = calculate_food_cost(guest_price, guests)
    discount = get_event_discount(guests, nonprofit)
    discounted_cost = food_cost * (1 - discount)
    if discounted_cost <= SERVICE_FEE_LIMIT:
        discounted_cost += SERVICE_FEE
    return discounted_cost


def needs_signoff(total: float) -> bool:
    """Returns True when the event total needs a manager's sign-off (rule 5), otherwise False."""
    return total > SIGNOFF_LIMIT


def needs_second_chef(guests: int, total: float) -> bool:
    """Returns True when event needs a second chef (rule 6), otherwise False."""
    return guests > SECOND_CHEF_GUEST_LIMIT or total >= SECOND_CHEF_TOTAL_LIMIT


def total_booked(events: list) -> float:
    """Returns the sum of the event totals for every event in the list."""
    total = 0.0
    for event in events:
        event_total = calculate_event_total(
            event["guest_price"], event["guests"], event["nonprofit"]
        )
        total += event_total
    return total


def largest_event(events: list) -> str:
    """Returns the client of the event with the largest event total. If two are tied for largest, it returns the first one in the list. An empty list returns an empty string."""
    largest_client = ""
    largest_total = 0.0
    for event in events:
        event_total = calculate_event_total(
            event["guest_price"], event["guests"], event["nonprofit"]
        )
        if largest_client == "" or event_total > largest_total:
            largest_total = event_total
            largest_client = event["client"]
    return largest_client


def format_event_line(
    client: str, total: float, signoff: bool, second_chef: bool
) -> str:
    """Returns one line of the report. Each True/False value is shown as yes or no, and the amount always has two decimal places."""
    signoff_text = "no"
    if signoff:
        signoff_text = "yes"
    chef_text = "no"
    if second_chef:
        chef_text = "yes"
    return (
        f"{client}: ${total:.2f} | sign-off: {signoff_text} | second chef: {chef_text}"
    )
