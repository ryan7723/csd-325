#Ryan Barber Assignment 9.2 2/28/26

import requests

response = requests.get('https://www.google.com/')
print(response.status_code)