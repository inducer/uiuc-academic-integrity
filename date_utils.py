import datetime


def date_by_adding_business_days(from_date, add_days):
    business_days_to_add = add_days
    current_date = from_date
    while business_days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5: # sunday = 6
            continue
        business_days_to_add -= 1
    return current_date


def datetime_by_adding_business_days(from_dt, add_days):
    return datetime.datetime.combine(
        date_by_adding_business_days(from_dt.date(), add_days),
        from_dt.time())
