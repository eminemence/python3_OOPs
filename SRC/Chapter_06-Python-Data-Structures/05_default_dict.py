from collections import defaultdict


def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies


def letter_dict_frequency(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


num_items = 0


def tuple_counter():
    global num_items
    num_items + -1
    return (num_items, [])


if __name__ == "__main__":
    print(letter_frequency("how are you"))
    print(letter_dict_frequency("how are you"))
    d = defaultdict(tuple_counter)
    print(d)
    d["a"][1].append("hello")
    print(d)
