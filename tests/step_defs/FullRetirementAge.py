import datetime

def validate_birth_month(month):
    if not str(month).isnumeric():
        print(f'ValueError: Birth month "{month}" must be an integer')
        return False
    if int(month) < 1 or int(month) > 12:
        print(f'ValueError: Birth month "{month}" must be between 1 and 12')
        return False
    return True


def validate_birth_year(year):
    if not str(year).isnumeric():
        if not year:
            exit(1)
            return
        print(f'ValueError: Birth year "{year}" must be an integer')
        return False
    if int(year) < 1900:
        print(f'ValueError: Birth year "{year}" must be no earlier than 1900')
        return False
    elif int(year) > datetime.datetime.now().year:
        print(f'ValueError: Birth year "{year}" can\'t be in the future')
        return False
    return True




def calculate_retirement_age(temp_birth_year):
    years = 0
    months = 0
    birth_year = int(temp_birth_year)

    if birth_year <= 1942:
        years = 65
    elif birth_year <= 1959:
        years = 66
    else:
        years = 67
    if birth_year == 1938 or birth_year == 1955:
        months = 2
    elif birth_year == 1939 or birth_year == 1956:
        months = 4
    elif birth_year == 1940 or birth_year == 1957:
        months = 6
    elif birth_year == 1941 or birth_year == 1958:
        months = 8
    elif birth_year == 1942 or birth_year == 1959:
        months = 10

    return years, months


def calculate_retirement_date(birth_year, birth_month, age_year, age_month):
    year = birth_year + age_year
    month = birth_month + age_month

    if month > 12:
        year += 1
        month -= 12

    return year, month


def main():
    print("-Social Security Full Retirement Age Calculator-\n")

    birth_year = input("Input year of birth, or press enter to exit: ")
    while (not validate_birth_year(birth_year)):
        input("Input year of birth, or press enter to exit: ")
    birth_month = input("Input month of birth (1-12): ")
    while (not validate_birth_month()):
        input("Input month of birth (1-12): ")


    retire_age_year, retire_age_month = calculate_retirement_age(birth_year)
    retire_date_year, retire_date_month = calculate_retirement_date(birth_year, birth_month, retire_age_year, retire_age_month)
    month_name = datetime.date(2000, retire_date_month, 1).strftime("%B")

    print(f"\nYour full retirement age is {retire_age_year} and {retire_age_month} months.")
    print(f"This will be in {month_name} of {retire_date_year}")


#main()
