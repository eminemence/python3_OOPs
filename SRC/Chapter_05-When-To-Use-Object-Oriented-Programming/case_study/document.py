class Document(object):
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ""

    def insert(self, character):
        if not hasattr(character, "character"):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor.position]

    def save(self):
        f = open(self.filename, "w")
        f.write("".join(self.characters))
        f.close()

    @property
    def string(self):
        return "".join((str(c) for c in self.characters))


class Cursor(object):
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        while self.document.characters[self.position - 1].character != "\n":
            self.position -= 1
            if self.position == 0:
                break

    def end(self):
        while (
            self.position < len(self.document.characters)
            and self.document.characters[self.position].character != "\n"
        ):
            self.position += 1


class Character(object):
    def __init__(self, character, bold=False, italic=False, underline=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        bold = "*" if self.bold else ""
        italic = "/" if self.italic else ""
        underline = "_" if self.underline else ""
        return bold + italic + underline + self.character


if __name__ == "__main__":
    doc = Document()
    doc.filename = "test_doc"
    doc.insert("h")
    doc.insert("e")
    doc.insert(Character("l", bold=True))
    doc.insert(Character("l", bold=True))
    doc.insert("o")
    doc.insert("\n")
    doc.insert(Character("w", italic=True))
    doc.insert(Character("o", italic=True))
    doc.insert(Character("r", underline=True))
    doc.insert("l")
    doc.insert("d")
    print(doc.string)
