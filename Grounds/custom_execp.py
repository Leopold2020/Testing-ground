

class AgeTooLow(Exception):
    """
        exception raises when someones age is too low
    Args:
        message (str): explenation for the problem
    """

    def __init__(self, age) -> None:
        self.current_age = age
        self.message = f"you are younger than 18, you are {self.current_age} years old"
        super().__init__(self.message)


# age = int(input("Write your age: "))
# if not age > 18: raise AgeTooLow(age)

if __name__ == "__main__":
    try:
        age = int(input("Write your age: "))
        if not age > 18: raise AgeTooLow(age)
        elif age == 18: raise ValueError
        elif age == 100: raise KeyboardInterrupt

    except AgeTooLow() as e:
        print("Too young.")
        print(e)
    except KeyboardInterrupt:
        print("please dont go")
    except ValueError:
        print("Eightteen.")
    
    else: 
        print("You old.")