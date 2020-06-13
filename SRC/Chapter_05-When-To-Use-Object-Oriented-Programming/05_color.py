class Color(object):
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        print("set_name")
        if not name:
            raise Exception("Invalid Names")
        self._name = name

    def _get_name(self):
        print("getname")
        return self._name

    name = property(_get_name, _set_name)


if __name__ == "__main__":
    c = Color("#ff0000", "bright_red")
    print(c.name)
    c.name = "red"
