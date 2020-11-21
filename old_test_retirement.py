import pytest
import datetime
import FullRetirementAge



# ------------------------------------------------
# Check that birth year validation raises ValueError
# with non-integer input
# ------------------------------------------------


def test_validate_birth_year_non_int():
    assert FullRetirementAge.validate_birth_year("a") == False


# ------------------------------------------------
# Check that birth year validation raises ValueError
# with years below 1900
# ------------------------------------------------


def test_validate_birth_year_1899():
    assert FullRetirementAge.validate_birth_year(1899) == False


# ------------------------------------------------
# Check that birth year validation raises ValueError
# with years above current year
# ------------------------------------------------


def test_validate_year_next_year():
    assert FullRetirementAge.validate_birth_year(datetime.datetime.now().year + 1) == False


# ------------------------------------------------
# Check that birth month validation raises ValueError
# with non-integer input
# ------------------------------------------------


def test_validate_birth_month_non_int():
    assert FullRetirementAge.validate_birth_month('a') == False


# ------------------------------------------------
# Check that birth month validation raises ValueError
# with months below 1
# ------------------------------------------------


def test_validate_birth_month_0():
    assert FullRetirementAge.validate_birth_month(0) == False


# ------------------------------------------------
# Check that birth month validation raises ValueError
# with months above 12
# ------------------------------------------------


def test_validate_birth_month_13():
    assert FullRetirementAge.validate_birth_month(13) == False

# ------------------------------------------------
# Check that calculate_retirement_age returns
# correct values
# ------------------------------------------------
testdata = [
    (1900, 65, 0),
    (1937, 65, 0),
    (1938, 65, 2),
    (1939, 65, 4),
    (1940, 65, 6),
    (1941, 65, 8),
    (1942, 65, 10),
    (1943, 66, 0),
    (1953, 66, 0),
    (1954, 66, 0),
    (1955, 66, 2),
    (1956, 66, 4),
    (1957, 66, 6),
    (1958, 66, 8),
    (1959, 66, 10),
    (1960, 67, 0)]


@pytest.mark.parametrize("year,a,b", testdata)
def test_calculate_retirement_age_years(year, a, b):
    a2, b2 = FullRetirementAge.calculate_retirement_age(year)
    assert a2 == a
    assert b2 == b


# ------------------------------------------------
# Check that calculate_retirement_date returns
# correct values
# ------------------------------------------------
testdata = [(1998, 12, 67, 0, 2065, 12),
            (1960, 1, 67, 0, 2027, 1),
            (1959, 1, 66, 10, 2025, 11),
            (1958, 1, 66, 8, 2024, 9),
            (1957, 1, 66, 6, 2023, 7),
            (1956, 1, 66, 4, 2022, 5),
            (1955, 1, 66, 2, 2021, 3),
            (1954, 1, 66, 0, 2020, 1),
            (1959, 3, 66, 10, 2026, 1)]


@pytest.mark.parametrize("birth_year, birth_month, age_years, age_months, expected_year, expected_month", testdata)
def test_calculate_retirement_date(birth_year, birth_month, age_years, age_months, expected_year, expected_month):
    y, m = FullRetirementAge.calculate_retirement_date(birth_year, birth_month, age_years, age_months)
    actual_age = [y, m]
    expected_age = [expected_year, expected_month]
    assert actual_age == expected_age
