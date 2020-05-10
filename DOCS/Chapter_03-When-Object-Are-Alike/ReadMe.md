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

