import datetime


def middle(stock, date):
    # tuple unpacking
    symbol, current, high, low = stock
    return (((high + low) / 2), date)


mid_value, date = middle(("GOOG", 613.30, 625.86, 610.50), datetime.date(2010, 1, 2))


print(mid_value, date)
print(middle(("GOOG", 613.30, 625.86, 610.50), datetime.date(2010, 1, 2))[:1])
