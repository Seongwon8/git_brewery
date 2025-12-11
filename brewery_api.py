import requests, pyfiglet
from tabulate import tabulate

print(pyfiglet.figlet_format("breweries API"))

url = "https://api.openbrewerydb.org/v1/breweries"

response = requests.get(url)
res = response.json()

headers = res[0].keys()
table_data = [[brewery.get(header, "") for header in headers] for brewery in res]

print(tabulate(table_data, headers=headers, tablefmt="grid"))
