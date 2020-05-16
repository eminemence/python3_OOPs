def funny_division(anumber):
    try:
        return 100 / anumber
    except ZeroDivisionError:
        return "Silly wabbit, you can't divide by zero."


if __name__ == "__main__":
    # The below line produces a ZeroDivisionError, which is caught
    # print(funny_division(0))
    print(funny_division(50.0))
    # the below raises a TypeErro
    print(funny_division("hello"))
