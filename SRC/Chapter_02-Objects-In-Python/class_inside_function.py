def format_string(string, formatter=None):
    """Format a string using the formatter object, which
    is ecpected to have a format() method that accepts a string"""

    class DefaultFormatter(object):
        """Format a String in title case"""

        def format(self, string):
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)


if __name__ == "__main__":
    hello_string = "hello world, how are you today?"
    print(" input: " + hello_string)
    print(" output: " + format_string(hello_string))
