from pytest_bdd import scenarios, given, when, then

import FullRetirementAge

CONVERTERS = {
    'input': str,
    'valid': str,
    'birth_year': int,
    'birth_month': int,
    'age_years': int,
    'age_months': int,
    'date_year': int,
    'date_month': int,
}

scenarios('../features/retirement.feature', example_converters=CONVERTERS)

@given('Program has started, and is prompting user to enter birth year')
def initial():
    pass

@when('User enters year "<input>"')
def enter_invalid_year(input):
    FullRetirementAge.validate_birth_year(input)

@then('Year validation returns "<valid>"')
def get_year_validation(valid, input):
    assert str(FullRetirementAge.validate_birth_year(input)) == valid

@when('User enters month "<input>"')
def enter_invalid_month(input):
    FullRetirementAge.validate_birth_month(input)

@then('Month validation returns "<valid>"')
def get_year_validation(valid, input):
    assert str(FullRetirementAge.validate_birth_month(input)) == valid

@when('User enters valid "<birth_year>"')
def enter_invalid_month(birth_year):
    FullRetirementAge.calculate_retirement_age(birth_year)

@then('Program returns correct "<age_years>" and "<age_months>"')
def get_year_validation(birth_year, age_years, age_months):
    y, m = FullRetirementAge.calculate_retirement_age(birth_year)
    assert y == int(age_years)
    assert m == int(age_months)

@when('User enters valid "<birth_year>" and "<birth_month>" And Program returns correct "<age_years>" and "<age_months>"')
def enter_invalid_month(birth_year, birth_month, age_years, age_months):
    FullRetirementAge.calculate_retirement_date(birth_year, birth_month, age_years, age_months)

@then('Program outputs correct "<date_year>" and "<date_month>"')
def get_year_validation(birth_year, birth_month, age_years, age_months, date_year, date_month):
    y, m = FullRetirementAge.calculate_retirement_date(birth_year, birth_month, age_years, age_months)
    assert y == int(date_year)
    assert m == int(date_month)
