# Chapter 03 | When Objects are Alike #

We will discuss one of the important OOP concepts, **inheritance** in this text. Inheritance allows us to create a *is-a* relationship between class, where the abstracted common details are present in super class and specific details are present in sub class.

## Basic Inheritance ##

* All Python classes are intrinsically inherited from the same Python class called `object`.
* Due to this common ancestry all Python Class can be treated in the same manner.
* `object` class provides the basic `__` methods.
* A **superclass** or **parent class** is the class from which we inherit.
* A **subclass** or **derived class** is the class which inherits from base class.
* Inheritance is used to make the derived class use all the functionality provided by base class, and add few more of its own functionality.
* Below is a sample inherited class from `object` and adding a new attribute called `all_contacts`


```python
class Contact(object):
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
```

* `all_contacts` list in the above sample is a **Class Variable**, that means this variable is shared across all instance variable.
* We append to this list using the Class name.

```python
class Supplier(contact.Contact):
    def order(self, order):
        print(
            "If this were a real system we would send"
            "{} order to {}".format(order, self.name)
        )
```

* The above code takes all code from `Contact` class described above and adds a `order` method.
* `Supplier` inherits all the code from `Contact` and adds an additional method of `order`.
    - This `order` is not available on the `Contact` class.

### Extending built-in ###

```python
class ContactList(list):
    def search(self, name):
        """Return all contacts that contain the search value in their name"""
        matching_contact = []
        for contact in self:
            if name in contact.name:
                matching_contact.append(contact)
        return matching_contact
```

* Like `object` we can also extend other built-in objects like
    - `list`
    - `set`
    - `dict`
    - `file`
    - `str`


### Overriding and Super ###

* We can add new behavior but also can change behavior to existing class. 
* Changing behavior is called **override**, it is altering or replacing a method of the superclass with a new method.
* We can extend the functionality in place of completely modifying the implementation by calling `super()` which invoke parent class methods.
* `super()` can be called inside any method.
* `super()` can be called at any point of the method and not at the beginning of the method.

```python
class Friend(contact.Contact):
    def __init__(self, name, email, phone):
        # Corrected by calling super init.
        super().__init__(name, email)
        self.phone = phone
```
## Multiple Inheritance ##
* Multiple inheritance is very delicate subject in inheritance. It means a class inheriting from 2 or more classes.
* Most of the time we do not need multiple inheritance, we should think multiple times before committing to a solution using multiple inheritance.
* One common use of multiple inheritance in Python is the use of **Mixin**.
    - A **Mixin** is used in when we want to provide lot of optional functionality to a single class.
    - Or we want to use a single functionality in multiple classes.

```python
class EmailableContact(contact.Contact, mailsender.MailSender):
    pass
```

* The above is an example of multiple inheritance.
* One important thing to remember in multiple inheritance is that the class hierarchy is taken from right to left in the parameter list above.
* The order does not matter most of the time, when the both base classes have different methods, but becomes and issues if the share method, the order changes based on inheritance.
* The methods are resolved left to right.
* As a best practice always keep the base class at the end of the parameter list.
* In place of using explicit class name to call base class methods, it is useful to call `super()` instead. It help by not invoking the base class method twice.

### Argument Passing ###

* When we have to pass different set of arguments to both parent class, then it becomes difficult.
* We can use the existing way of using explicit Class name, to call `__init__`, but same cannot be used with `super` as we will not know which base class will be called.
* We have to used Key Word argument as a parameter and also providing an empty value to the key word argument.
* The Key word explicitly mentioned in the function consumes those argument and passes the remaining to hierarchy as `**kwargs`
* This causes issue is multiple class in the hierarchy want to use the same arguments, then we have to keep the `**kwargs` update with all values, and each class uses only relevant values.  



## Reference ##
* [What is a mixin, and why are they useful?](https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful)
* [Mixins and Python](https://www.ianlewis.org/en/mixins-and-python)
* [Supercharge Your Classes With Python super()](https://realpython.com/python-super/)
* [ Python’s super() considered super! ](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)


