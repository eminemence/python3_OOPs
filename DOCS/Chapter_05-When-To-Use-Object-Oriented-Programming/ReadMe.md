# Chapter 05 | When To Use Object Oriented Programming #

## Identifying Object ##

* Identifying objects in a problem statement is the most crucial part of the learning experience.
* We generally identify object in the problem and then model their data and behaviors.
    - Identifying is not about only figuring the nous in the problem statement.
    - As an object has both data and behavior. If we need only Data we can use the built in list, set etc.
    - If only behavior is concerned, we can use only function.
* The Object oriented code generally is relatively self documenting.
* Interaction between objects is also important.
    - inheritance is important.
    - composition can be modeled using only data structure.


## property ##
* In Python, there is no restriction on accessing the data member, unlike Java.
* Though we can indicate a private member of a class by adding `_` in the name like `_name`.
    - This does not prevent it from accessing the member, just that it is a convention.
* Python uses a `property()` keyword which can provide getter and setter on a member.

```python
class Color(object):
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Names")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)


if __name__ == "__main__":
    c = Color("#ff0000", "bright_red")
    print(c.name)
    c.name = "red"
```
* In the above code, `_name` is a member variable meant to be hidden by convention.
* We create 2 more getter and setter method, which are also hidden by convention, `_set_name` and `_get_name`.
* `name = property(_get_name, _set_name)`
    - The is the magic line, it creates a member variable with the name `name`, which can be accessed normally in python. as shown above.
    - `_get_name()` is called when we are doing `print(c.name)`
    - `_set_name()` is called when we are doing `c.name = "red"`
* The `property` keywords is used to make methods look like class attribute.
* The `property` function can be considered as a proxies any request to set or access the attributes value.
* The `property` takes in total of 4 parameters, but generally only 2 are provided, which acts as a getter and setter.
    - 1st parameter: The getter function
    - 2nd parameter: The setter function
    - 3rd parameter: The delete function
    - 4th parameter: The doc string of the function, generally only supposed in the getter function, which is the copied.

```python
class Silly(object):
    def _get_silly(self):
        print("You are getting silly")
        return self._silly

    def _set_silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    def _del_silly(self):
        print("Whoah, you killed silly")
        del self._silly

    silly = property(_get_silly, _set_silly, _del_silly, """This is a silly property""")


if __name__ == "__main__":
    s = Silly()
    s.silly = "funny"
    print(s.silly)
    del s.silly
```

* In the above code, we are using all the 4 parameters.
