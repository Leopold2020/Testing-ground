# Oskar Svedlund
# TE4
# 2023-09-04
# Online shop made up of classes

import OnlineshopResources as res


customer = res.Customer(1, "Oskar", "1234")
ware = res.Ware(1, "Banana", 10, "it's bananas")

def main():
    user = ""
    order_list = []
    customer_list = []
    ware_list = []
    # order = input("What do you want to buy?: ")
    customer_list.append(customer)
    ware_list.append(ware)
    # order_list.append(res.purchase(customer.customer_id, ware.ware_id, ware.price, "Homedelivery"))
    
    loginChoice = input("Do you want to login or make an account?\n1. Login\n2. Make account\n>>")
    
    if loginChoice == "1":
        login = input("Password\n>>")
    
        for account in customer_list:
            if account.password == login:
                user = account
                print(f"Welcome {user.name}")
    
    if loginChoice == "2":
        user = make_account()
        customer_list.append(user)
        print(f"Welcome {user.name}")
    

    while True:
        menuChoice = input("What do you want to do?\n1. Make order\n2. Show orders\n3. Show wares\n4. Make ware\n5. Exit\n>>")
        
        match menuChoice:
            case "1":
                order_list.append(make_order(user, ware_list))
                
            case "2":
                for orders in order_list:
                    print(orders)
            
            case "3":
                for items in ware_list:
                    print(items)
                    
            case "4":  
                ware_list.append(make_ware())
                
            case "5":
                break

    
def make_account():
    name = input("Name?: ")
    id = input("ID?: ")
    password = input("Password?: ")
    return res.Customer(id, name, password)

def make_ware():
    name = input("Name?: ")
    id = input("ID?: ")
    price = input("Price?: ")
    description = input("Description?: ")
    return res.Ware(id, name, price, description)

def make_order(account, wares):
    purchase = int(input("What do you want to buy?: "))
    for item in wares:
        if item.ware_id == purchase:
            ware = item
    print(f"{account}, {ware}")
    
    return f"{account.customer_id}, {ware.ware_id}, {ware.price}, Homedelivery"
    
    
if "__main__" == __name__:
    main()