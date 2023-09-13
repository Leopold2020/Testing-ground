# Oskar Svedlund
# TE4
# 2023-09-13
# Stocks emulation

import resources as res

from time import sleep
import random as rand

def main():
    stock = load_stock()
    
    while True:
        choice = input("What do you want to do?\n>>")
        
        match choice:
            case "1":
                # stock = load_stock()
                print(stock)
                
            case "2":
                
                time = 0
                
                while time < 24:
                    
                    sleep(5)
                    number = rand.uniform(0.98, 1.02)
                    print(number)
                    number = float(str(number)[:5])
                    print(number)
                    stock.update_value(number)
                    print(stock)
                    time += 1
                
                
            case "3":
                break

def load_stock():
    name, nick, values, current_value = res.load_data()
    return res.Stock(name, nick, values, current_value)

if __name__ == "__main__":
    main()