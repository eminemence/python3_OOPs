class Color(object):
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self.name = name


if __name__ == "__main__":
    c = Color("#ff0000", "bright_red")
    print(c.name)
    c.name = "red"
