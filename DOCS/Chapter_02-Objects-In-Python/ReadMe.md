# Chapter 02 | Objects in Python #

## Hello World Python Classes ##

````python
class MyFirstClass:
    pass

# initiate the class
a = MyFirstClass()
b = MyFirstClass()
````

* The above is a most basic class in python.
* `class` : keyword defines the start of class.
* Class names follows a conventions in Python.
    - Class name should comprise of number, letters or underscore.
    - Class name should use CamelCase naming convention.
    - The first letter of a class name should be capital, as when creating object we can differentiate between a function call or Object initialization.
* Object Creation:-
    - We can create the objects of a new class as shown in the code above.
    - The only difference in creating object and calling function is that, creating function has the first character as capitalized.
* `python -i hello.py` : runs the code, and then enters into python shell loading the class.

### Attributes ###
* Attribute in Python classes can be set even outside class definition.
* Attribute added in 1 object does not automatically adds it into the other object.

````python
class Point:
    pass


p1 = Point()
p2 = Point()

# Adding x,y attribute to Point P1
p1.x = 5
p1.y = 4

# Adding x,y attribute to Point P1
p2.x = 3
p2.y = 6

print(p1.x, " ", p1.y)
print(p2.x, " ", p2.y)

````
* As shown above example, when we add `p1.x` and `p1.y`, adds `x` and `y` attribute to th `Point` Class.
* This `x` and `y` is not accessible in the other object called `p2`, we have to individually add these attribute to that object.
* We use the syntax `<object>.<attribute> = <value>` to assign values to an attribute of an object.

### Methods ###
* There is no point in writing Object if we cannot show the interaction between them. The interaction between them is possible using methods.

```python
class Point:
    # Move method
    def move(self, x, y):
        self.x = x
        self.y = y

    # self is a manditory name.
    def reset(self):
        self.move(0, 0)

    # Calculate distance
    def calculate_distance(self, other):
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))

p1 = Point()
p1.reset()
point2.move(5, 0)
```

* A **method** is just a function inside class. 
* Every method have a mandatory method called `self` as an arguments. This name `self` is by convention.
* The `self` is just a reference to the object used to invoke the method.
* The `self` is not passed while calling the method, as shown by `p1.reset()`, it is implicitly passed by the interpretor.
* `Point.reset(p1)` is another alternate way of calling the method.
* Python interpreter gives an error `TypeError` if we do not use `self` as an arguments.
* We can pass multiple argument to a function shown below, 
    - `def move(self, x, y)`
* Calling the above `move` function is very similar `point2.move(5, 0)`, `self` is not passed explicitly

### Object Initialization ###


## References ##
1. [Python Modules and Packages - An Introduction ](https://realpython.com/python-modules-packages/)
2. [Corey Schafer | Python OOP Tutorials - Working with Classes ](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
3. [SentDex | Intermediate Python Programming ](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_)
