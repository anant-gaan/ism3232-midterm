from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    get_event_discount,
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
