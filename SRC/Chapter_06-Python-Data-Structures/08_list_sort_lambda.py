if __name__ == "__main__":
    x = [(1, "c"), (2, "a"), (3, "b")]
    print(x)
    x.sort()
    print(x)
    x.sort(key=lambda i: i[1])
    print(x)

    l = ["hello", "HelP", "Helo"]
    print(l)
    l.sort(key=str.lower)
    print(l)
