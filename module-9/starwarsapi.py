#Ryan Barber Assignment 9.2 2/28/26

import requests

url = "https://swapi.py4e.com/api/films/"

response = requests.get(url)
data = response.json()

print("=== RAW OUTPUT ===")
print(data)

print("=== STAR WARS FILMS ===")

for film in data["results"]:
    print(f"Title: {film['title']}")
    print(f"Episode: {film['episode_id']}")
    print(f"Director: {film['director']}")
    print(f"Release Date: {film['release_date']}")
    print("-" * 40)