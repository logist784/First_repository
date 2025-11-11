year_to_check = int(input())


def is_year_leap(year):
    return year % 4 == 0


result = is_year_leap(year_to_check)

print(f"год {year_to_check}: {result}")
