# Absolute Import
import ecommerce.products
import ecommerce.payments.paypal
from ecommerce.database import Database
from ecommerce import db

product = ecommerce.products.Products()
paypal = ecommerce.payments.paypal.Paypal()

print(db)
