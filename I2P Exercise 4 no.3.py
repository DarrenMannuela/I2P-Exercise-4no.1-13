import calendar


def date(year, month):
    tc = calendar.TextCalendar(firstweekday=0)
    print(tc.formatmonth(year, month, w=0, l=0))
    return tc


date(2200,4)