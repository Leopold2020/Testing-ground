# Oskar Svedlund
# TE4
# 2023-09-04
# Online shop made up of classes

import OnlineshopResources as res



def main():
    order_list = []
    customer_list = []
    ware_list = []
    
    
    customer = res.Customer(1, "Oskar")
    ware = res.Ware(1, "Banana", 10, "One banana")
    # order = input("What do you want to buy?: ")
    customer_list.append(customer)
    ware_list.append(ware)
    # order_list.append(res.purchase(customer.customer_id, ware.ware_id, ware.price, "Homedelivery"))
    
    print(customer)
    print(ware)
    # for item in order_list:
    #     print(item)

    make_order(customer_list, ware_list)
    
    
def make_account():
    name = input("Name?: ")
    id = input("ID?: ")
    return res.Customer(id, name)

def make_ware():
    name = input("Name?: ")
    id = input("ID?: ")
    price = input("Price?: ")
    description = input("Description?: ")
    return res.Ware(id, name, price, description)

def make_order(accounts, wares):
    identification = int(input("ID?: "))
    for account in accounts:
        if account.customer_id == identification:
            customer = account

    purchase = int(input("What do you want to buy?: "))
    for item in wares:
        if item.ware_id == purchase:
            ware = item
    
    print(f"{customer}, {ware}")
if "__main__" == __name__:
    main()