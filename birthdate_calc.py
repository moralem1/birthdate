from datetime import date, timedelta
from calendar import monthrange

MAX_AGE_YEARS = 122


def subtract_years(d: date, years: int) -> date:
    target_year = d.year - years
    try:
        return d.replace(year=target_year)
    except ValueError:
        # Handles Feb 29 -> Feb 28 on non-leap years
        return d.replace(year=target_year, month=2, day=28)


def subtract_months(d: date, months: int) -> date:
    total_months = d.year * 12 + (d.month - 1) - months
    target_year = total_months // 12
    target_month = total_months % 12 + 1
    last_day = monthrange(target_year, target_month)[1]
    target_day = min(d.day, last_day)
    return date(target_year, target_month, target_day)


def read_int_in_range(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if min_value <= value <= max_value:
                return value
            print(f"Enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Please enter a valid whole number.")


def main() -> None:
    while True:
        death_date_str = input("Enter death date (YYYY-MM-DD): ").strip()
        try:
            death_date = date.fromisoformat(death_date_str)
            break
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD and a real calendar date.")

    while True:
        years = read_int_in_range(
            "Enter years lived (0-122): ",
            0,
            MAX_AGE_YEARS,
        )
        months = read_int_in_range(
            "Enter additional months lived (0-11): ",
            0,
            11,
        )
        days = read_int_in_range(
            "Enter additional days lived (0-30): ",
            0,
            30,
        )

        birth_date = death_date - timedelta(days=days)
        birth_date = subtract_months(birth_date, months)
        birth_date = subtract_years(birth_date, years)
        oldest_allowed_birth = subtract_years(death_date, MAX_AGE_YEARS)

        if birth_date < oldest_allowed_birth:
            print("Age exceeds 122 years total. Please re-enter years/months/days.")
            continue

        print("Estimated birth date:", birth_date.isoformat())
        break


if __name__ == "__main__":
    main()