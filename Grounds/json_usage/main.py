import json

testdata = {"test2" : "test3"}

class User():

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return self.name

    def save_data(self):

        data = {"name":f"{self.name}", "age":f"{self.age}"}

        with open('Grounds/json_usage/data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def request_info(self):
        self.name = input("Name?: ")
        self.age = input("Age?: ")


def loding_data():
    with open('Grounds/json_usage/data.json') as json_file:
        read_data = json.load(json_file)
        return read_data["name"], read_data["age"]
    

def main():
    print(loding_data())
    name_data, age_data = loding_data()
    user = User(name_data, age_data)

    print(user)

    user.request_info()
    user.save_data()

if __name__ == "__main__":
    main()