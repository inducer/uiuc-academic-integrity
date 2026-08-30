import datetime


def date_by_adding_business_days(
            from_date: datetime.date, add_days: int) -> datetime.date:
    business_days_to_add = add_days
    current_date = from_date
    while business_days_to_add > 0:
        current_date += datetime.timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5:  # sunday = 6
            continue
        business_days_to_add -= 1
    return current_date


def datetime_by_adding_business_days(
            from_dt: datetime.datetime, add_days: int
        ) -> datetime.datetime:
    return datetime.datetime.combine(
        date_by_adding_business_days(from_dt.date(), add_days),
        from_dt.time())


def advance_deadline(
            old_deadline: float, fresh_days: int = 2, existing_days: int = 1,
        ) -> float:

    if old_deadline is None:
        min_bump = fresh_days
        deadline = None
    else:
        min_bump = existing_days
        deadline = datetime.datetime.fromtimestamp(old_deadline)

    min_deadline = datetime_by_adding_business_days(
        datetime.datetime.combine(
            datetime.date.today(),
            datetime.time(17, 0)),
        min_bump)

    if deadline is None or deadline < min_deadline:
        deadline = min_deadline

    return deadline.timestamp()
