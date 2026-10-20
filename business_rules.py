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
    """Returns the event total for for one event: the discounted cost plus the service fee when it applies (rule 4)."""
    food_cost = calculate_food_cost(guest_price, guests)
    discount = get_event_discount(guests, nonprofit)
    discounted_cost = food_cost * (1 - discount)
    if discounted_cost <= SERVICE_FEE_LIMIT:
        discounted_cost += SERVICE_FEE
    return discounted_cost
