from app.models.order import *
import datetime

order1 = Order("Barry", datetime.date(2021, 1, 5), 2)
order2 = Order("Jerry", datetime.date(2021, 1, 6), 54)
order3 = Order("Sherry", datetime.date(2021, 1, 6), 3)
orders = [order1, order2, order3]