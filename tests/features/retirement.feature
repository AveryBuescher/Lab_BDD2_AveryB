Feature: Full Retirement Age Calculator
  Determine your retirement date(year/month) and age
  based on your birth year and month

  Scenario Outline: Catching invalid year entry
    Given Program has started, and is prompting user to enter birth year
    When User enters year "<input>"
    Then Year validation returns "<valid>"

    Examples:
      |input|valid|
      |1899 |False|
      |2021 |False|
      |a    |False|
      |2000 |True |

  Scenario Outline: Catching invalid month entry
    Given Program has started, and is prompting user to enter birth year
    When User enters month "<input>"
    Then Month validation returns "<valid>"

    Examples:
      |input|valid|
      |0    |False|
      |13   |False|
      |a    |False|
      |5    |True |

  Scenario Outline: Getting retirement age with valid inputs
    Given Program has started, and is prompting user to enter birth year
    When User enters valid "<birth_year>"
    Then Program returns correct "<age_years>" and "<age_months>"

    Examples:
      |birth_year|age_years|age_months|
      |1900      |65      |0        |
      |1937      |65      |0        |
      |1938      |65      |2        |
      |1939      |65      |4        |
      |1940      |65      |6        |
      |1941      |65      |8        |
      |1942      |65      |10       |
      |1943      |66      |0        |
      |1954      |66      |0        |
      |1955      |66      |2        |
      |1956      |66      |4        |
      |1957      |66      |6        |
      |1958      |66      |8        |
      |1959      |66      |10       |
      |1960      |67      |0        |
      |2020      |67      |0        |

  Scenario Outline: Getting retirement date, user enters valid inputs
    Given Program has started, and is prompting user to enter birth year
    When User enters valid "<birth_year>" and "<birth_month>" And Program returns correct "<age_years>" and "<age_months>"
    Then Program outputs correct "<date_year>" and "<date_month>"

    Examples:
      |birth_year|birth_month|age_years|age_months|date_year|date_month|
      |1998      |12         |67       |0         |2065     |12        |
      |1960      |1          |67       |0         |2027     |1         |
      |1959      |1          |66       |10        |2025     |11        |
      |1959      |3          |66       |10        |2026     |1         |
