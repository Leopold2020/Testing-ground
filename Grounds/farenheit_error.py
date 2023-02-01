class FahrenheitError(Exception):
    min_f = 32
    max_f = 212

    def __init__(self, f, *args: object) -> None:
        super().__init__(args)
        self.f = f

    def __str__(self) -> str:
        if self.f > 212:
            return "too hot for the macine"
        elif self.f < 32:
            return "too cold for the macine"

def fahrenheit_to_celsius(f: float):
    if f < FahrenheitError.min_f or f > FahrenheitError.max_f:
        raise FahrenheitError(f)
    return (f - 32)* (5 / 9)

if __name__ == "__main__":
    try:
        degree = int(input("Write a number in fahrenheit you want to convert to celsius: "))
        new_degree = fahrenheit_to_celsius(degree)
        
    except ValueError:
        print("use only numbers, not words")

    except FahrenheitError as e:
        print(e)

    else: 
        print(f"{degree} Fahrenheit is {new_degree:.2f} celsius")