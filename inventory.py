"""Product inventory calculations and stock availability checks."""

import logging
from pathlib import Path

LOG_FILE = Path(__file__).with_name("application.log")
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def _validate_number(value: int | float, name: str) -> None:
    """Require a finite, nonnegative numeric value (excluding booleans)."""
    import math

    if isinstance(value, bool) or not isinstance(value, (int, float)):
        logger.error("Invalid %s type: %r", name, value)
        raise TypeError(f"{name} must be a number")
    if not math.isfinite(value) or value < 0:
        logger.error("Invalid %s value: %r", name, value)
        raise ValueError(f"{name} must be finite and nonnegative")


def _validate_quantity(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        logger.error("Invalid %s type: %r", name, value)
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        logger.error("Negative %s: %r", name, value)
        raise ValueError(f"{name} cannot be negative")


def calculate_total_price(price: int | float, quantity: int) -> float:
    """Return the total price for a nonnegative unit price and quantity."""
    _validate_number(price, "price")
    _validate_quantity(quantity, "quantity")
    total = round(price * quantity, 2)
    logger.info(
        "Total price calculated: price=%s quantity=%s total=%s", price, quantity, total
    )
    return total


def apply_discount(total: int | float, discount_percent: int | float) -> float:
    """Return the final amount after a discount from 0 to 100 percent."""
    _validate_number(total, "total")
    _validate_number(discount_percent, "discount_percent")
    if discount_percent > 100:
        logger.error("Discount exceeds 100%%: %s", discount_percent)
        raise ValueError("discount_percent cannot exceed 100")
    discounted = round(total * (1 - discount_percent / 100), 2)
    logger.info(
        "Discount applied: total=%s percent=%s final=%s",
        total,
        discount_percent,
        discounted,
    )
    return discounted


def check_stock(available_stock: int, requested_quantity: int) -> bool:
    """Return True if the requested quantity is available, otherwise False."""
    _validate_quantity(available_stock, "available_stock")
    _validate_quantity(requested_quantity, "requested_quantity")
    available = requested_quantity <= available_stock
    if available:
        logger.info(
            "Stock check passed: available=%s requested=%s",
            available_stock,
            requested_quantity,
        )
    else:
        logger.warning(
            "Insufficient stock: available=%s requested=%s",
            available_stock,
            requested_quantity,
        )
    return available


def main() -> None:
    """Run a small interactive product inventory demonstration."""
    print("Product Inventory Management System")
    try:
        price = float(input("Unit price: "))
        quantity = int(input("Requested quantity: "))
        stock = int(input("Available stock: "))
        discount = float(input("Discount percentage: "))
        if not check_stock(stock, quantity):
            print("Insufficient stock for this order.")
            return
        total = calculate_total_price(price, quantity)
        final_amount = apply_discount(total, discount)
        print(f"Total price: ₹{total:.2f}")
        print(f"Final price after discount: ₹{final_amount:.2f}")
        print("Stock available: Yes")
    except (TypeError, ValueError) as exc:
        logger.error("Operation failed: %s", exc)
        print(f"Invalid input: {exc}")


if __name__ == "__main__":
    main()
