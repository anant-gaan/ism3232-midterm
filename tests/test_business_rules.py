from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    format_event_line,
    get_event_discount,
    largest_event,
    needs_second_chef,
    needs_signoff,
    total_booked,
)


def test_calculate_food_cost_before_discount():
    assert round(calculate_food_cost(18.00, 20), 2) == 360.00


def test_discount_below_25_guests():
    assert get_event_discount(24) == 0.0


def test_discount_25_guests():
    assert get_event_discount(25) == 0.05


def test_discount_fee_at_500():
    assert round(calculate_event_total(25.00, 20), 2) == 575.00


def test_discount_99_guests_nonprofit():
    assert get_event_discount(99, nonprofit=True) == 0.05


def test_discount_100_guests_not_nonprofit():
    assert get_event_discount(100, nonprofit=False) == 0.05


def test_discount_100_guests_nonprofit():
    assert get_event_discount(100, nonprofit=True) == 0.12


def test_event_total_with_service_fee():
    assert round(calculate_event_total(18.00, 20), 2) == 435.00


def test_even_total_without_service_fee():
    assert round(calculate_event_total(500.01, 1), 2) == 500.01


def test_signoff_at_2500():
    assert needs_signoff(2500.00) is False


def test_signoff_above_2500():
    assert needs_signoff(2500.01) is True


def test_second_chef_at_80_guests():
    assert needs_second_chef(80, 1000.00) is False


def test_second_chef_above_80_guests():
    assert needs_second_chef(81, 1000.00) is True


def test_second_chef_below_3000_total():
    assert needs_second_chef(20, 2999.99) is False


def test_second_chef_at_3000_total():
    assert needs_second_chef(20, 3000.00) is True


def test_total_booked_two_events():
    events = [
        {"client": "Acme Corp", "guest_price": 20.00, "guests": 20, "nonprofit": False},
        {"client": "Beta Inc", "guest_price": 25.00, "guests": 30, "nonprofit": True},
    ]
    assert round(total_booked(events), 2) == 1187.50


def test_total_booked_empty_list():
    assert total_booked([]) == 0.0


def test_largest_event_two_events():
    events = [
        {
            "client": "Arc Studios",
            "guest_price": 20.00,
            "guests": 20,
            "nonprofit": False,
        },
        {"client": "Loro Group", "guest_price": 20.00, "guests": 40, "nonprofit": True},
    ]
    assert largest_event(events) == "Loro Group"


def test_largest_event_tied_events():
    events = [
        {"client": "Ford Club", "guest_price": 30.00, "guests": 20, "nonprofit": False},
        {"client": "Honda Inc", "guest_price": 60.00, "guests": 10, "nonprofit": True},
    ]
    assert largest_event(events) == "Ford Club"


def test_largest_event_empty_list():
    assert largest_event([]) == ""


def test_format_event_line_no_no():
    result = format_event_line("Yummy Goods", 435.00, False, False)
    assert result == "Yummy Goods: $435.00 | sign-off: no | second chef: no"


def test_format_event_line_yes_yes():
    result = format_event_line("Tasty Treats", 3420.50, True, True)
    assert result == "Tasty Treats: $3420.50 | sign-off: yes | second chef: yes"


def test_format_event_line_yes_no():
    result = format_event_line("Delicious Dishes", 1500.75, True, False)
    assert result == "Delicious Dishes: $1500.75 | sign-off: yes | second chef: no"


def test_format_event_line_no_yes():
    result = format_event_line("Savory Snacks", 800.25, False, True)
    assert result == "Savory Snacks: $800.25 | sign-off: no | second chef: yes"
