def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned."


def call_exceptor():
    print("Call_exceptor starts here")
    no_return()
    print("an exception was raised")
    print("...so these lines don't run")


if __name__ == "__main__":
    # no_return()
    # call_exceptor()
    try:
        no_return()
    except:
        print("I caought and exception")
    print("executed after the exception")
