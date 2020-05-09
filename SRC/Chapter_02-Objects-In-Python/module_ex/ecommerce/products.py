from .database import Database


class Products(object):
    def __init__(self):
        print("Inside Product __init__ ")
        db = Database()
