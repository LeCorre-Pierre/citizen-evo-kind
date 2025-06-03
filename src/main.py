from map import MapData, Cell
from individual import Individual

# This file will contain the main simulation loop and logic for moving individuals, updating map, etc.

def main():
    # Example: create a 5x5 map with empty cells
    width, height = 5, 5
    cells = [Cell(x=x, y=y, type="Green") for x in range(width) for y in range(height)]
    map_data = MapData(width=width, height=height, cells=cells)
    # Example: create an individual
    ind = Individual(
        name="Anna",
        surname="Smith",
        gender="Female",
        age=25,
        max_age=80,
        job="Farmer",
        position={"x": 2.3, "y": 4.7},
        destination={"x": 4, "y": 4},
        skills={"Manual": 75, "Medicine": 20, "Intellectual": 40, "Cooking": 55, "Social": 30}
    )
    print(map_data)
    print(ind)

if __name__ == "__main__":
    main()
