from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import calendar
import csv

tz = ZoneInfo("Europe/Kyiv")
today = datetime.now(tz).date()


def month_start(d):
    return d.replace(day=1)


def month_end(d):
    return d.replace(day=calendar.monthrange(d.year, d.month)[1])


def add_months(d, months):
    month = d.month - 1 + months
    year = d.year + month // 12
    month = month % 12 + 1
    day = min(d.day, calendar.monthrange(year, month)[1])
    return d.replace(year=year, month=month, day=day)


current = today
previous = add_months(today, -1)
preprevious = add_months(today, -2)

last_sunday = today - timedelta(days=(today.weekday() + 1) % 7)

rows = [
    [1, "Date.today", today],

    [2, "Date.CurrentMonthStart", month_start(current)],
    [3, "Date.CurrentMonthEnd", month_end(current)],
    [4, "Date.8CalendarDayCurrentMonth", current.replace(day=8)],
    [5, "Date.9CalendarDayCurrentMonth", current.replace(day=9)],
    [6, "Date.16CalendarDayCurrentMonth", current.replace(day=16)],
    [7, "Date.17CalendarDayCurrentMonth", current.replace(day=17)],
    [8, "Date.24CalendarDayCurrentMonth", current.replace(day=24)],
    [9, "Date.25CalendarDayCurrentMonth", current.replace(day=25)],

    [10, "Date.PreviousMonthStart", month_start(previous)],
    [11, "Date.PreviousMonthEnd", month_end(previous)],
    [12, "Date.8CalendarDayPreviousMonth", previous.replace(day=8)],
    [13, "Date.9CalendarDayPreviousMonth", previous.replace(day=9)],
    [14, "Date.16CalendarDayPreviousMonth", previous.replace(day=16)],
    [15, "Date.17CalendarDayPreviousMonth", previous.replace(day=17)],
    [16, "Date.24CalendarDayPreviousMonth", previous.replace(day=24)],
    [17, "Date.25CalendarDayPreviousMonth", previous.replace(day=25)],

    [18, "Date.PrePreviousMonthStart", month_start(preprevious)],
    [19, "Date.PrePreviousMonthEnd", month_end(preprevious)],
    [20, "Date.8CalendarDayPrePreviousMonth", preprevious.replace(day=8)],
    [21, "Date.9CalendarDayPrePreviousMonth", preprevious.replace(day=9)],
    [22, "Date.16CalendarDayPrePreviousMonth", preprevious.replace(day=16)],
    [23, "Date.17CalendarDayPrePreviousMonth", preprevious.replace(day=17)],
    [24, "Date.24CalendarDayPrePreviousMonth", preprevious.replace(day=24)],
    [25, "Date.25CalendarDayPrePreviousMonth", preprevious.replace(day=25)],

    [26, "Date.LastSundayFromToday", last_sunday],

    [27, "", ""],
    [28, "", ""]
]

with open("dates.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["RowNumber", "Primary Column", "DateToUse"])

    writer.writerows(rows)

print("dates.csv updated")
