# Chapter 06 | Python Data Structure #

## Empty Object ##

```python
obj = object()
print(obj)
obj.x = 9
```

* In the above code, we can create an empty object by just calling the `object()` constructor / initiator .
* Creating object in the above manner stop's from adding new attribute to the class, it raise `AttributeError`.
* The reason for not allowing to create the attributes is memory, as everything inherits from  `objects`, even keeping minor memory allocated will be big.

```python
class MyObject:
    pass

m = MyObject()
m.x = "hello"
print(m.x)
```

* We should create our own class and assign attributes if we want to do that, in place of creating empty `object`.
* Built-in data structures are available in Python to support data storage, and we should not use objects for this purpose.


## Tuples and Named Tuples. ##

* Tuples are immutable, ordered storage of related data.
* Due to immutability of tuples, these can be used as keys in dictionary.
* The primary purpose of a tuple is to aggregate different pieces of data together into one container.
* Tuples are created by using comma `,` to separate values, but a parentheses is used while passing it to a function.
    - The reason for parentheses is that, it will be difficult to identify if only 1 argument was pass or multiple.

```python
import datetime


def middle(stock, date):
    # tuple unpacking
    symbol, current, high, low = stock
    return (((high + low) / 2), date)


mid_value, date = middle(("GOOG", 613.30, 625.86, 610.50), datetime.date(2010, 1, 2))

print(mid_value, date)
```

* In the above code, this is the tuple,
    - `("GOOG", 613.30, 625.86, 610.50)`
* The above example also supports tuple unpacking and packing.
    - `symbol, current, high, low = stock` 
        + The above is an example of tuple unpacking.
        + The 4 values of `stock` are expanded into `symbol, current, high, low`, in order.
        + The number of variables has to be 4, same as the no of values inside the tuple.
        + We can pack the variable and move it around, like passing into function etc, and when individual values are required we can unpack them.
        + We can use the index to access the individual elements of tuple.
        + We can also use slice to get a group of values, which is a tuple and not a list.
* The side effect of the tuple is that, there is no name to understand the values while passing around.
* Tuples should be used when the group of values make sense.

### Named Tuple ###

* As discussed in tuples above, the biggest disadvantage of tuple is that individual element cannot be named.
* We can used Named Tuple to group data with no extra behavior.
* `Stock = namedtuple("Stock", "symbol current high low")`
    - `namedtuple` constructor takes two arguments.
        + The identifier the tuple can have
        + String separated space attributes
    - The resulting `namedtuple` can be packed and unpacked just like tuple, along with benefits of individually accepting value, like `stock.high`.
* `namedtuple` are perfect for data only representation.
* Since `namedtuple` is a tuple, we cannot modify the individual values of the tuple. 



