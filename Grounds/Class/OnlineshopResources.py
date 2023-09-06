# Oskar Svedlund
# TE4
# 2023-09-04
# Online shop made up of classes

class Customer():
    def __init__(self, customer_id, name, password) -> None:
        self.customer_id = customer_id
        self.name = name
        self.password = password
        
    def __str__(self) -> str:
        return f"customer_id: {self.customer_id}, name: {self.name}"

class Ware():
    def __init__(self, ware_id, name, price, description) -> None:
        self.ware_id = ware_id
        self.name = name
        self.price = price
        self.description = description
        
    def __str__(self) -> str:
        return f"ware_id: {self.ware_id}, name: {self.name}, price: {self.price}, description: {self.description}"
        

class Order():
    def __init__(self, customerID, wareID, cost, delivery) -> None:
        self.customerID = customerID
        self.wareID = wareID
        self.cost = cost
        self.delivery = delivery
        
    def __str__(self) -> str:
        return f"customerID: {self.customerID}, wareID: {self.wareID}, cost: {self.cost}, delivery: {self.delivery}"


def purchase(customerID, wareID, cost, delivery):
    order = Order(customerID, wareID, cost, delivery)
    return order
    