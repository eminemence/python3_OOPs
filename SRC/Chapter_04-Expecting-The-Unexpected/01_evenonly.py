class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)


if __name__ == "__main__":
    e = EvenOnly()
    # This below line raises a TypeErrpr
    # e.append("Hello")
    # This below line raise a ValueError
    # e.append(3)
    e.append(2)
    print(e)
