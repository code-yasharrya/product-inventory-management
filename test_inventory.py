"""Unit tests for the product inventory management functions."""

import pytest

from inventory import apply_discount, calculate_total_price, check_stock


def test_total_price_valid():
    assert calculate_total_price(125.5, 2) == 251.0


def test_total_price_zero_quantity():
    assert calculate_total_price(100, 0) == 0


def test_total_price_negative_price():
    with pytest.raises(ValueError):
        calculate_total_price(-10, 2)


def test_total_price_fractional_quantity():
    with pytest.raises(TypeError):
        calculate_total_price(10, 1.5)


def test_discount_valid():
    assert apply_discount(500, 20) == 400


def test_discount_zero():
    assert apply_discount(500, 0) == 500


def test_discount_hundred():
    assert apply_discount(500, 100) == 0


def test_discount_above_hundred():
    with pytest.raises(ValueError):
        apply_discount(500, 101)


def test_discount_negative():
    with pytest.raises(ValueError):
        apply_discount(500, -1)


def test_stock_available():
    assert check_stock(10, 5) is True


def test_stock_exact_boundary():
    assert check_stock(10, 10) is True


def test_stock_unavailable():
    assert check_stock(3, 5) is False


def test_stock_negative_quantity():
    with pytest.raises(ValueError):
        check_stock(10, -1)


def test_stock_invalid_type():
    with pytest.raises(TypeError):
        check_stock(10, "2")


def test_stock_zero():
    assert check_stock(0, 0) is True


def test_price_boolean_rejected():
    with pytest.raises(TypeError):
        calculate_total_price(True, 2)
