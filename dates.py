from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import calendar
import csv

# Kyiv timezone
tz = ZoneInfo("Europe/Kyiv")

# Current date/time in Kyiv
now = datetime.now(tz)
today = now.date()


def format_date(value):
    if isinstance(value, datetime):
        return ""

    if value == "":
        return ""

    return value.strftime("%Y-%m-%d")


def month_start(date_value):
    return date_value.replace(day=1)


def month_end(date_value):
    return date_value.replace(
        day=calendar.monthrange(
            date_value.year,
            date_value.month
        )[1]
    )


def add_months(date_value, months):
    month = date_value.month - 1 + months
    year = date_value.year + month // 12
    month = month % 12 + 1

    day = min(
        date_value.day,
        calendar.monthrange(year, month)[1]
    )

    return date_value.replace(
        year=year,
        month=month,
        day=day
    )


def last_sunday(date_value):
    days_since_sunday = (date_value.weekday() + 1) % 7
    return date_value - timedelta(days=days_since_sunday)


# Month references
current_month = today
previous_month = add_months(today, -1)
pre_previous_month = add_months(today, -2)

# Future month references
next_month = add_months(today, 1)
month_after_next = add_months(today, 2)


rows = [

    [1, "Date.today", today, ""],

    # Current Month
    [2, "Date.CurrentMonthStart", month_start(current_month), ""],
    [3, "Date.CurrentMonthEnd", month_end(current_month), ""],
    [4, "Date.8CalendarDayCurrentMonth", current_month.replace(day=8), ""],
    [5, "Date.9CalendarDayCurrentMonth", current_month.replace(day=9), ""],
    [6, "Date.16CalendarDayCurrentMonth", current_month.replace(day=16), ""],
    [7, "Date.17CalendarDayCurrentMonth", current_month.replace(day=17), ""],
    [8, "Date.24CalendarDayCurrentMonth", current_month.replace(day=24), ""],
    [9, "Date.25CalendarDayCurrentMonth", current_month.replace(day=25), ""],

    # Previous Month
    [10, "Date.PreviousMonthStart", month_start(previous_month), ""],
    [11, "Date.PreviousMonthEnd", month_end(previous_month), ""],
    [12, "Date.8CalendarDayPreviousMonth", previous_month.replace(day=8), ""],
    [13, "Date.9CalendarDayPreviousMonth", previous_month.replace(day=9), ""],
    [14, "Date.16CalendarDayPreviousMonth", previous_month.replace(day=16), ""],
    [15, "Date.17CalendarDayPreviousMonth", previous_month.replace(day=17), ""],
    [16, "Date.24CalendarDayPreviousMonth", previous_month.replace(day=24), ""],
    [17, "Date.25CalendarDayPreviousMonth", previous_month.replace(day=25), ""],

    # Pre-Previous Month
    [18, "Date.PrePreviousMonthStart", month_start(pre_previous_month), ""],
    [19, "Date.PrePreviousMonthEnd", month_end(pre_previous_month), ""],
    [20, "Date.8CalendarDayPrePreviousMonth", pre_previous_month.replace(day=8), ""],
    [21, "Date.9CalendarDayPrePreviousMonth", pre_previous_month.replace(day=9), ""],
    [22, "Date.16CalendarDayPrePreviousMonth", pre_previous_month.replace(day=16), ""],
    [23, "Date.17CalendarDayPrePreviousMonth", pre_previous_month.replace(day=17), ""],
    [24, "Date.24CalendarDayPrePreviousMonth", pre_previous_month.replace(day=24), ""],
    [25, "Date.25CalendarDayPrePreviousMonth", pre_previous_month.replace(day=25), ""],

    # Other dates
    [26, "Date.LastSundayFromToday", last_sunday(today), ""],

    # Future Months
    [27, "Date.NextMonthStart", month_start(next_month), ""],
    [28, "Date.NextMonthEnd", month_end(next_month), ""],
    [29, "Date.MonthAfterNextStart", month_start(month_after_next), ""],
    [30, "Date.MonthAfterNextEnd", month_end(month_after_next), ""],

    # Last Updated
    [31, "Date.LastUpdated", "", now.strftime("%Y-%m-%d %H:%M:%S")]
]


with open(
    "dates.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow(
        [
            "RowNumber",
            "Primary Column",
            "DateToUse",
            "UpdatedAt"
        ]
    )

    for row in rows:
        writer.writerow(row)


print("dates.csv successfully updated")
print(f"Today: {today}")
print(f"Next month: {month_start(next_month)} - {month_end(next_month)}")
print(f"Month after next: {month_start(month_after_next)} - {month_end(month_after_next)}")
print(f"Last Sunday: {last_sunday(today)}")
print(f"Updated at: {now}")
