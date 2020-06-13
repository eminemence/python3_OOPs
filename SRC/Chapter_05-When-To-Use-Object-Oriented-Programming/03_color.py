# Java's approach of setter and getter in Python.
class Color:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


if __name__ == "__main__":
    c = Color("#ff0000", "bright red")
    print(c.get_name())
    c.set_name("red")
    print(c.get_name())
