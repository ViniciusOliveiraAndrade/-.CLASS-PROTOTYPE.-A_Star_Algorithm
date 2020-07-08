import json
from AStar import AStar

with open("cities.json", "r") as read_file:
    cities = json.load(read_file)

a = AStar(cities, "Arad")
a.printPath(a.getPath())
