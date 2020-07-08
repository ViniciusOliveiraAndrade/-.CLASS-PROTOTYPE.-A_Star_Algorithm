import json
from AStar import AStar

start_city = "Lugoj"

with open("cities.json", "r") as read_file:
    cities = json.load(read_file)

a = AStar(cities, start_city)
a.printPath(a.getPath())
