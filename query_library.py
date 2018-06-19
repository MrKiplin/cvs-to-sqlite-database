# Function will return today's date.
def get_today_date():
    tday_date = datetime.date.today()
    return tday_date


# Function will return first day of the previous month date.
def get_last_day_previous_month_date():
    prev_month_last_day = date.today().replace(day=1) - timedelta(days=1)
    return prev_month_last_day


# Function will return last day of the previous month date.
def get_first_day_previous_month_date():
    prev_month_first_day = get_last_day_previous_month_date().replace(day=1)
    return prev_month_first_day


# List of SQL query's
test_query = """
SELECT *
FROM table_name
WHERE fruit_type = 'apple'
"""