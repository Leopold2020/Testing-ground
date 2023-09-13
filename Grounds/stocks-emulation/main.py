# Oskar Svedlund
# TE4
# 2023-09-13
# Stocks emulation

import resources as res


def main():
    stock = []
    
    while True:
        choice = input("What do you want to do?\n>>")
        
        match choice:
            case "1":
                stock = load_stock()
                print(stock)
                
            case "2":
                break

def load_stock():
    stock = res.Stock(res.load_data())
    return stock

if "__name__" == "__main__":
    main()