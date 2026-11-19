# Assignment 10 – Product Inventory Management System

A Python inventory application that calculates total product prices, applies discounts, checks stock availability, validates inputs, handles errors, and records operations in `application.log`.

## Features

- `calculate_total_price(price, quantity)` calculates price × quantity.
- `apply_discount(total, discount_percent)` returns the final amount after discount.
- `check_stock(available_stock, requested_quantity)` returns `True` or `False`.
- Rejects negative prices, invalid percentages, non-integer quantities, and invalid types.
- Logs successful calculations, stock checks, insufficient-stock warnings, and input errors.
- Includes 16 pytest cases and Ruff lint/format support.

## macOS setup

Open Terminal and navigate to this folder:

```bash
cd ~/Desktop/product-inventory-management
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

If Python 3.12 is not installed, install it with `brew install python@3.12`, or use a compatible Python 3 version.

## Run application

```bash
python inventory.py
```

Follow the prompts for price, requested quantity, available stock, and discount percentage. The program generates `application.log` automatically.

## Run tests

```bash
python -m pytest -v
```

## Ruff lint and formatting

```bash
ruff check .
ruff check . --fix
ruff format .
ruff check .
ruff format --check .
```

## Evidence and submission

Capture terminal screenshots showing successful pytest execution and Ruff lint/format checks. Place them in `screenshots/` before committing. Upload the project files, including the generated `application.log`, but do not upload `.venv/`.

Create a GitHub repository named `product-inventory-management` and push the project to it. Submit the repository link and requested screenshots to the classroom platform.
