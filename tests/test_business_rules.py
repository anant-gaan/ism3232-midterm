from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    get_event_discount,
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
