"""Calculate progressive electricity bills and compare consecutive months."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


# Sample tariff; edit these values to match the applicable electricity provider.
SLABS = (
    (Decimal("100"), Decimal("1.50")),
    (Decimal("200"), Decimal("2.50")),
    (Decimal("300"), Decimal("4.00")),
    (None, Decimal("6.00")),
)
FIXED_CHARGE = Decimal("50.00")
SURCHARGE_RATE = Decimal("0.05")
REBATE_RATE = Decimal("0.02")
REBATE_USAGE_LIMIT = Decimal("100")
UNUSUAL_INCREASE_RATE = Decimal("0.20")
MONEY = Decimal("0.01")


def calculate_bill(units: Decimal) -> tuple[Decimal, Decimal, Decimal, Decimal, Decimal]:
    """Return energy charge, fixed charge, surcharge, rebate, and total."""
    if not units.is_finite() or units < 0:
        raise ValueError("Units must be a finite non-negative number.")

    remaining_units = units
    previous_limit = Decimal("0")
    energy_charge = Decimal("0")

    for limit, rate in SLABS:
        slab_capacity = (
            remaining_units
            if limit is None
            else min(remaining_units, limit - previous_limit)
        )
        energy_charge += slab_capacity * rate
        remaining_units -= slab_capacity

        if remaining_units <= 0:
            break
        if limit is not None:
            previous_limit = limit

    surcharge = (energy_charge + FIXED_CHARGE) * SURCHARGE_RATE
    rebate = (
        energy_charge * REBATE_RATE
        if units <= REBATE_USAGE_LIMIT
        else Decimal("0")
    )
    total = energy_charge + FIXED_CHARGE + surcharge - rebate

    return tuple(
        amount.quantize(MONEY, rounding=ROUND_HALF_UP)
        for amount in (energy_charge, FIXED_CHARGE, surcharge, rebate, total)
    )


def read_decimal(prompt: str) -> Decimal:
    """Prompt until the user enters a finite, non-negative decimal."""
    while True:
        try:
            value = Decimal(input(prompt).strip())
            if value.is_finite() and value >= 0:
                return value
        except InvalidOperation:
            pass
        print("Enter a valid non-negative number.")


def main() -> None:
    print("Progressive Electricity Billing")
    print("Sample tariff rates are configured at the top of task2.py.")
    while True:
        try:
            month_count = int(input("Number of months to enter: ").strip())
            if month_count > 0:
                break
        except ValueError:
            pass
        print("Enter a positive whole number.")

    bills: list[tuple[str, Decimal, Decimal]] = []
    for month_number in range(1, month_count + 1):
        month = input(f"\nMonth {month_number} name: ").strip()
        while not month:
            print("Month name cannot be empty.")
            month = input(f"Month {month_number} name: ").strip()

        units = read_decimal(f"Units consumed in {month}: ")
        energy, fixed, surcharge, rebate, total = calculate_bill(units)
        bills.append((month, units, total))
        print(
            f"{month}: energy {energy:.2f}, fixed {fixed:.2f}, "
            f"surcharge {surcharge:.2f}, rebate {rebate:.2f}, "
            f"total {total:.2f}"
        )

    if len(bills) < 2:
        print("\nEnter at least two months to compare bills.")
        return

    print("\nMonth-to-month comparison")
    for previous, current in zip(bills, bills[1:]):
        previous_month, _, previous_total = previous
        current_month, _, current_total = current
        change = current_total - previous_total

        if previous_total == 0:
            increase_rate = Decimal("Infinity") if change > 0 else Decimal("0")
        else:
            increase_rate = change / previous_total

        if change > 0:
            percent_change = (
                "unbounded" if previous_total == 0 else f"{increase_rate:.1%}"
            )
            status = (
                "UNUSUAL INCREASE"
                if increase_rate > UNUSUAL_INCREASE_RATE
                else "increase"
            )
            print(
                f"{previous_month} to {current_month}: +{change:.2f} "
                f"({percent_change}) - {status}"
            )
        elif change < 0:
            print(f"{previous_month} to {current_month}: {change:.2f} (decrease)")
        else:
            print(f"{previous_month} to {current_month}: no change")


if __name__ == "__main__":
    main()
