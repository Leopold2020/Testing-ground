import requests
from dotenv import load_dotenv
import os

load_dotenv()
DEP_KEY = os.getenv("DEP_KEY")
PLACE_KEY = os.getenv("PLACE_KEY")

# place_search = "Nacka strand"
# place_url = f"https://api.se/api2/typehead.JSON?key={PLACE_KEY}&searchstring={place_search}"
# response = requests.get(place_url)
# print(response)
# anwser = response.json()
# print(anwser)

time = "14"
slussen = "9192"
nacka_strand = "4031"
realtime = f""

response = requests.get(realtime)
print(response)
anwser = response.json()
# print(anwser)

for line in anwser["ResponseData"]["Buses"]:
    print(line["Linenumber"], line["Destination"], line["DisolayTime"])