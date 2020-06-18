stocks = {"GOOG": (613.30, 625.86, 610.50), "MSFT": (30.25, 30.70, 30.19)}
print(stocks["GOOG"])
print(stocks.get("RIM"))
print(stocks.get("RIM", "NOT FOUND"))

# Since key `GOOG` it will return the value
print(stocks.setdefault("GOOG", "INVALID"))
print(stocks.setdefault("RIM", (67.38, 68.48, 67.28)))


# keys(), values(), items()
for k, v in stocks.items():
    print("{} last value id {}".format(k, v))

stocks["GOOG"] = (597.63, 610.00, 596.28)
print(stocks["GOOG"])

random_keys = {}
random_keys["astring"] = "somestring"
random_keys[5] = "aninteger"
random_keys[25.2] = "floats work too"
random_keys[("abc", 123)] = "so do tuples"


class AnObject:
    def __init__(self, avalue):
        self.avalue = avalue


my_object = AnObject(14)
random_keys[my_object] = "we can even store objets"
my_object.avalue = 12

try:
    random_keys[1, 2, 3] = "we can't store lists though"
except:
    print("unable to store lists\n")
