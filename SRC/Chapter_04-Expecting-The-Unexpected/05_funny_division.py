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


if __name__ == "__main__":
    for val in (0, "hello", 50.0, 13):
        print("Testing {}: ".format(val), end="")
        print(funny_division(val))
