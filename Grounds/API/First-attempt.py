# Oskar Svedlund
# TEINF-20
# 2023-03-15
# Testing API

import requests

name = input("name?\n>> ")
name2 = input("name2?\n>> ")

response = requests.get(f"https://api.agify.io?name[]={name}&name[]={name2}&country_id=SE")

anwser = response.json()

print(anwser)