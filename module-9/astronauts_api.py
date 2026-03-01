#Ryan Barber Assignment 9.2 2/28/26

import requests

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
data = response.json()

print(response.json())

print("=== RAW OUTPUT ===")
print(data)

print("\n=== FORMATTED OUTPUT ===")
print("People currently in space:", data["number"])
print("\nAstronauts:\n")

for person in data["people"]:
    print(person["name"], "-", person["craft"])

