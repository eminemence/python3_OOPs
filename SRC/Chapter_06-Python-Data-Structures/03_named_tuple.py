from collections import namedtuple

Stock = namedtuple("Stock", "symbol current high low")
stock = Stock("GOOG", 613.30, 625.86, 610.50)

print(stock)
