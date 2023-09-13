# Oskar Svedlund
# TE4
# 2023-09-13
# Stocks emulation

import json

class Stock():
    def __init__(self, name: str, nickname: str, values: list, current_value: int):
        self.name = name
        self.nickname = nickname
        self.values = values
        self.current_value = current_value
        
    def __str__(self):
        return f"{self.name} ({self.nickname}) - {self.current_value} kr"
    
    def append_value(self, value):
        self.values.append(value)
        
    def update_value(self, value):
        self.current_value = value
        
    def save(self):
        data = {"name":f"{self.name}", "nickname":f"{self.nickname}", "values":f"{self.values}", "current_value":0}

        with open('Grounds/stock-emulation/data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
def load_data():
    with open('Grounds/stock-emulation/data.json') as json_file:
        read_data = json.load(json_file)
        return read_data["name"], read_data["nickname"], read_data["values"], read_data["current_value"]