# Chapter 04 | Expecting the unexpected #

* It is not possible to return valid results for all type of inputs, be it valid or invalid.
* It is also difficult to put check for all type of inputs.
* In Object Oriented world we have **exceptions**, which can be handled for possible error conditions.

## Raising exceptions ##
* An **exception** is technically just an object.
* All **exception** are derived from the base class `BaseException`.
* All built-in exception class ends with the name `Error`.
* Few common exception seen 
    - `ZeroDivisionError` : When we divide by zero
    - `IndexError` : When we access an index outside the index range.
    - `TypeError` : When we do any operation with incompatible type.
    - `KeyError` : A dictionary not having a proper key.
    - `NameError` : When a variable is not defined.

### Raising an exception ###

```python
class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)
```
* The above code, is an example how we can raise exception to inform user about the wrong input being passed.
* `raise` keyword is used to invoke an exception when certain condition is not met.
* The above code raises these 2 exception:
    - `TypeError` : When the input it string.
    - `ValueError` : When the input is not divisible by `2`.

```python
def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned."
```
* In the above code, we will get the first print,
* The `Exception` will occur on 2nd line.
* The 3rd and the 4th line of the function will not execute.

```python
def call_exceptor():
    print("Call_exceptor starts here")
    no_return()
    print("an exception was raised")
    print("...so these lines don't run")
```
* the `call_exceptor` calls the `no_return` function.
* the `call_exceptor` prints the first line, then `no_return` prints its function first line.
* Then an exception occurs and none of the other lines are executed.
* The exception from `no_return` is propagated till `call_exceptor`

## Handling Exception ##
* We handle exception by wrapping the exception making code inside a `try...except` clause.

```python
try:
        no_return()
    except:
        print("I caought and exception")
    print("executed after the exception")
```

* We can wrap the exception making function `no_return` inside the `try...except` as soon above.
* With the above handling of the exception, the program was able to reach a logical conclusion, and not disrupt the flow with an exception.
* The above `except` will call all the exception, which is not desirable.
* We can also chose to handle certain exception and allow other exception to propagate as shown below.


```python
def funny_division(anumber):
    try:
        return 100 / anumber
    except ZeroDivisionError:
        return "Silly wabbit, you can't divide by zero."
```

* The above code catches only the `ZeroDivisionError`, and propagates all other exception.
* The generic `except` code shown in previous code will handle all the exception.
* We can also catch multiple exception using the below code.

```python
def funny_division(anumber):
    try:
        return 100 / anumber
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"
```

* The above code catches 2 exception, but prints the generic prints for both, so `ZeroDivisionError` and `TypeError` both behave in the same manner.

```python
def funny_division(anumber):
    try:
        if anumber == 13:
            raise ValueError("13 is an unlucky")
        return 100 / anumber
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13")
        raise
```

* In the above code we are handling all exception separately, like `ZeroDivisionError`, `TypeError` and `ValueError`.
* In `ValueError`, we are raising the same exception again after handling it.
* The exception classes also follow inheritance, so while catching exception always the specific exception first and then followed by more generic exception.
* If we catch the generic exception like `Exception` first then it will not match other exception.
* We can also catch the exception `as` a variable.

```python
try:
    raise ValueError("This is an argument")
except ValueError as e:
    print("The exception arguments were: ", e.args)
```

* There are two additional keywords in the exception handling concepts.
    - `else` : This is invoked when no exception has happened.
    - `finally` : This code is executed in both cases, i.e if exception happens or does not happens.
        + We put clean-up code in `finally` block expecting it to be executed in any circumstances.
* The order of the exception flow is
    - `except`
    - `else`
    - `finally`

## Exception Hierarchy ##
* Here is an hierarchy of exception in Python.
    - `BaseException`
        + `SystemExit`
            * This is raised when we call `sys.exit` in our code, it signifies natural exits.
            * Catching this exception will stop the exit process, so after cleanup we should re-raise the exception again.
            * The reason we do not want to catch this exception accidentally, that is the reason it inherits from `BaseException` 
        + `KeyboardInterrupt`
            * This is common in command line programs.
            * `Ctrl + C` is a common way to exit such application.
        + `Exception`
            * All other exception is derived from here.
* When we use a `except` clause without any exception mentioned, it catches all the exception including `BaseException`.
* Mostly in code if generic exception has to be caught, it has to be the `Exception` class.

### Own Exception ###
* We can create our own exception, by inheriting from `Exception` class.

```python
class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__("account doesn't have ${}".format(amount))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance
```

* We can raise the above exception using the `raise`

### If statement Vs Exception ###
* We can check for inputs value in a function and check or print respective error string.
* We should need `Exception` at all, but few thing works in favor of exception, which is we cannot check for all type of inputs.
* We can also use `Exception` as a effective way of handling control flow.
    - In case of an inventory system, if a item is out of stock, which is very much of a possibility we can catch an `OutOfStockError` and respond accordingly.


## Reference ##
* [Python try-else](https://stackoverflow.com/questions/855759/python-try-else)
