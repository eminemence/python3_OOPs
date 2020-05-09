# Relative imports
from ..database import Database


class Paypal(object):
    def __init__(self):
        print("Inside Paypal __init__")
        db = Database()
