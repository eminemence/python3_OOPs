class SceretString(object):
    """A not at all secure way to store a secret string."""

    def __init__(self, plain_text, pass_phrase):
        self.__plain_string = plain_text
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        """Only Show the string if the pass_phrase is correct """
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ""


if __name__ == "__main__":
    secret_string = SceretString("ACME: Top Secret", "antwerp")
    print(secret_string.decrypt("antwerp"))
    # Give AttributeError: 'SceretString' object has no attribute '__plain_string'
    # print(secret_string.__plain_string)
    print(secret_string._SceretString__plain_string)
