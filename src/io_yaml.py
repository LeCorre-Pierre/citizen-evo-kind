import yaml
from src.map import MapData, Cell

def save_map_to_yaml(map_data: MapData, filename: str):
    with open(filename, 'w') as f:
        yaml.dump({
            'Map': {
                'Size': f"{map_data.width}x{map_data.height}",
                'Cells': [cell.__dict__ for cell in map_data.cells]
            }
        }, f)

def load_map_from_yaml(filename: str) -> MapData:
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)
        size = data['Map']['Size'].split('x')
        width, height = int(size[0]), int(size[1])
        cells = [Cell(**cell) for cell in data['Map']['Cells']]
        return MapData(width=width, height=height, cells=cells)
