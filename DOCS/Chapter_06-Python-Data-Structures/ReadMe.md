# Chapter 06 | Python Data Structure #

## Empty Object ##

```python
obj = object()
print(obj)
# Following line raises AttributeError, so cannot set any attribute on object class
# obj.x = 9
```

* In the above code, we can create an empty object by just calling the `object()` constructor / initiator .
* Creating object in the above manner stop's from adding new attribute to the class, it raise `AttributeError`.
* The reason for not allowing to create the attributes is memory, as everything inherits from  `objects`, even keeping minor memory allocated will be big.
* Python disables arbitrary properties on object and other built-ins.

```python
class MyObject:
    pass

m = MyObject()
m.x = "hello"
print(m.x)
```

* We should create our own class and assign attributes if we want to do that, in place of creating empty `object`.
* Built-in data structures are available in Python to support data storage, and we should not use objects for this purpose.
* _Tip : Save memory & limit arbitrary properties on class you define by using __slots__. More info : https://book.pythontips.com/en/latest/__slots__magic.html_

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
            * ```python
              stock = "FB", 100, 20, 500
              volume = stock[3]
              print(volume)
              ```
* The side effect of the tuple is that, there is no name to understand the values while passing around.
* Tuples should be used when the group of values make sense.

### Named Tuple ###

* As discussed in tuples above, the biggest disadvantage of tuple is that individual element cannot be named.
* We can used Named Tuple to group data with no extra behavior.
* `Stock = namedtuple("Stock", ["symbol","current","high","low"])`
    - `namedtuple` constructor takes two arguments.
        + The identifier the tuple can have
        + String separated space attributes
    - The resulting `namedtuple` can be packed and unpacked just like tuple, along with benefits of individually accepting value, like `stock.high`.
* `namedtuple` are perfect for data only representation.
* Since `namedtuple` is a tuple, we cannot modify the individual values of the tuple.

### Dataclasses ###
* For creating objects where data can be changed, used `dataclass`.
  **TODO : Add more dataclass details and samples**
 
## Dictionaries ##
* Dictionaries map object directly to other objects.
* Dictionaries are best used for fast lookup, i.e. searching for value.
* The object stored is called **value**, and its reference or index is called **key**.

```python
stocks = {"GOOG": (613.30, 625.86, 610.50), "MSFT": (30.25, 30.70, 30.19)}
```

* The above line, defines a dictionary called `stocks`, with the 2 values of `GOOG` and `MSFT`.
* We can access the values using `stocks['GOOG']`.
* Accessing a key not present in the dictionary raises `KeyError`.
* The best way to access a key in dictionary is by the use of `get`, which does not throws error for key not present

```python
print(stocks.get("RIM"))
print(stocks.get("RIM", "NOT FOUND"))
```

* As shown in the above code, by using `get`, if the key is not present like in the first line, it will return NONE, and not a key error.
* `get` also takes a optional parameters which is returned in case the key is not found, like `NOT FOUND` in 2nd line.


```python
print(stocks.setdefault("GOOG", "INVALID"))
print(stocks.setdefault("RIM", (67.38, 68.48, 67.28)))
```

* `setdefault` : returns the 2nd parameter if the key is not present, and also sets the key value pair, like in the 2nd line, 
    - If the key is present it acts like a `get`, i.e. returns the value of the key.
* It becomes difficult for setting all the key with default values using `setdefault`.
    - We can use `defaultdict()` to initialize a dictionary values, it takes an argument, which initializes accordingly.
    - We also pass our own object to `defaultdict`

```python
for k, v in stocks.items():
    print("{} last value id {}".format(k, v))
```

* `keys()`, `values()`, `items()`: other important methods in dictionary.
    - `keys()` : returns an iterator object of all keys in the dictionary to iterate.
    - `values()` : returns an iterator object of all values in the dictionary to iterate.
    - `items()` : as shown above, returns a tuple with a iterator of (key, value) pair.
* Dictionaries are not ordered, i.e. it does not return values in the order they were inserted.
* `stocks["GOOG"] = (597.63, 610.00, 596.28)`
    - We can use the index notation to save an retrieve values.
* We can store all different type of objects as key in dictionaries, like integer, floats, another objects, string, even tuple
    - We cannot store `list` or `dict` as a key,
        + these are not hash ables as these can change on runtime or are mutable.
* We can use anything as a value, there is no restrictions.
* Dictionaries can be used in 2 ways
    - As an indexing system
    - Each key represent an attribute of object and its value.


## List ##
* List are the least object oriented Python data structure.
* List is used when mostly order is important.
* List can be used to create queues, stacks, linked lists etc.
* List should not be used to create attribute of the same object.
* List sorting is an interesting topics, where it can do a number of things.
    - To Sort a class of object in a list, we can implement the `__lt__` method in the class, to tell the sorting order.
    - As shown below, `__lt__`, changes the sort order based on the value of `sort_num`

```python
class WierdSortee(object):
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
        return "{}:{}".format(self.string, self.number)
```

* We can also pass a `key=` to the sorting function, identifying which is the key for sorting.
    - `x = [(1, "c"), (2, "a"), (3, "b")]`
    - `x.sort(key=lambda i: i[1])`
        + For the above list of tuple, we defined a `key=` to a `lamda` function, which passed the 2nd element of the tuple as a key.
    - `l.sort(key=str.lower)`
        + We can also pass built-in `str.lower` as a key, thus sorting by ignoring the case.


## Sets ##
* Sets are used when the uniqueness of the objects are important.
* Sets store only one copy of the objects.
* Empty sets is created with `sets()` constructor.
* Sets are also not ordered like Dictionaries.
* Sets are useful for these operations
    - Finding if a element is in the sets.
    - Looping over item in sets.
* Sets are not useful, to provide order to its elements, like sorting etc.
* The most important methods on Sets are
    - `union() ` : It combines 2 sets, which have all the elements from both sets.
    - `intersection() ` : it finds the common element in two sets.
    - `symmetric_difference()` : it finds the element which are in one set of the other but not in both.
    - `issubset()` : if a set is a subset of another set.
    - `issuperset()` : if a set is a superset of another set.
    - `difference()` : elements present in the calling set but not in the parameter sets.


## Extending Built-in ##
* There are two ways we can use the above storage data structure in our code.
    - Use Inheritance to extend the functionality.
        + We should use Inheritance when we want to modify the way the Data Structure interacts.
    - Use composition to store certain data.
        + We can use composition, when we have to use it just as a storage.
* To all the non object oriented syntax of python, there is an underlying Object Oriented syntax.
    - The Non Object oriented syntax is taken just so that the writing code is more logical.

```python
c = a + b
c = a.add(b) # Non Object oriented way
```

* The above syntax is possible by overriding a lot of hidden methods.
    - `__add__()` : should be overridden for `+`
    - `__contains()` : should be overridden for `in` operator.
    - `__setitem__()` : should be overridden for `=` operator.
    - `__getitem_()` : should be overridden for getting value from operator.
  


