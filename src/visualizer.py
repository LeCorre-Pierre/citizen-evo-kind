import tkinter as tk
from map import MapData, Cell

CELL_SIZE = 40
CELL_COLORS = {
    "Green": "#7ec850",
    "Dirt": "#bfa76f",
    "Town": "#b0b0b0"
}

class MapVisualizer(tk.Tk):
    def __init__(self, map_data: MapData):
        super().__init__()
        self.title("Map Visualizer")
        self.map_data = map_data
        self.width_var = tk.IntVar(value=map_data.width)
        self.height_var = tk.IntVar(value=map_data.height)
        self.menu_frame = tk.Frame(self)
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)
        tk.Label(self.menu_frame, text="Width:").pack(side=tk.LEFT)
        tk.Entry(self.menu_frame, textvariable=self.width_var, width=4).pack(side=tk.LEFT)
        tk.Label(self.menu_frame, text="Height:").pack(side=tk.LEFT)
        tk.Entry(self.menu_frame, textvariable=self.height_var, width=4).pack(side=tk.LEFT)
        tk.Button(self.menu_frame, text="Resize", command=self.resize_map).pack(side=tk.LEFT)
        tk.Label(self.menu_frame, text=" | Cell Type:").pack(side=tk.LEFT)
        self.cell_type_var = tk.StringVar(value="Green")
        tk.OptionMenu(self.menu_frame, self.cell_type_var, "Green", "Dirt", "Town").pack(side=tk.LEFT)
        tk.Button(self.menu_frame, text="Set Cell", command=self.set_cell_type).pack(side=tk.LEFT)
        tk.Button(self.menu_frame, text="Add Mine", command=self.add_mine).pack(side=tk.LEFT)
        tk.Button(self.menu_frame, text="Save Map", command=self.save_map).pack(side=tk.LEFT)
        tk.Button(self.menu_frame, text="Load Map", command=self.load_map).pack(side=tk.LEFT)
        self.selected_cell = None
        self.selected_rect = None
        self.canvas = tk.Canvas(self, width=map_data.width*CELL_SIZE, height=map_data.height*CELL_SIZE)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.draw_map()

    def resize_map(self):
        width = self.width_var.get()
        height = self.height_var.get()
        # Recreate cells as Green by default
        cells = [Cell(x=x, y=y, type="Green") for x in range(width) for y in range(height)]
        self.map_data.width = width
        self.map_data.height = height
        self.map_data.cells = cells
        self.canvas.config(width=width*CELL_SIZE, height=height*CELL_SIZE)
        self.canvas.delete("all")
        self.draw_map()

    def on_canvas_click(self, event):
        x = event.x // CELL_SIZE
        y = event.y // CELL_SIZE
        for cell in self.map_data.cells:
            if cell.x == x and cell.y == y:
                self.selected_cell = cell
                break
        self.canvas.delete("all")
        self.draw_map()

    def draw_map(self):
        for cell in self.map_data.cells:
            x0 = cell.x * CELL_SIZE
            y0 = cell.y * CELL_SIZE
            x1 = x0 + CELL_SIZE
            y1 = y0 + CELL_SIZE
            color = CELL_COLORS.get(cell.type, "white")
            width = 3 if self.selected_cell == cell else 1
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black", width=width)
            if getattr(cell, 'mine', False):
                self.canvas.create_oval(x0+10, y0+10, x1-10, y1-10, fill="gray")
            if getattr(cell, 'growth', None) is not None:
                self.canvas.create_text((x0+x1)//2, (y0+y1)//2, text=str(cell.growth), fill="darkgreen")

    def set_cell_type(self):
        if self.selected_cell:
            self.selected_cell.type = self.cell_type_var.get()
            self.selected_cell.mine = False  # Remove mine if type changes
            self.canvas.delete("all")
            self.draw_map()

    def add_mine(self):
        if self.selected_cell and self.selected_cell.type == "Green":
            self.selected_cell.mine = True
            self.canvas.delete("all")
            self.draw_map()

    def save_map(self):
        import tkinter.filedialog as fd
        from io_yaml import save_map_to_yaml
        file = fd.asksaveasfilename(defaultextension=".yaml", filetypes=[("YAML files", "*.yaml")])
        if file:
            save_map_to_yaml(self.map_data, file)

    def load_map(self):
        import tkinter.filedialog as fd
        from io_yaml import load_map_from_yaml
        file = fd.askopenfilename(filetypes=[("YAML files", "*.yaml")])
        if file:
            map_data = load_map_from_yaml(file)
            self.map_data.width = map_data.width
            self.map_data.height = map_data.height
            self.map_data.cells = map_data.cells
            self.width_var.set(map_data.width)
            self.height_var.set(map_data.height)
            self.canvas.config(width=map_data.width*CELL_SIZE, height=map_data.height*CELL_SIZE)
            self.selected_cell = None
            self.canvas.delete("all")
            self.draw_map()

if __name__ == "__main__":
    # Example usage
    width, height = 5, 5
    cells = [Cell(x=x, y=y, type="Green") for x in range(width) for y in range(height)]
    # Add a mine and a dirt cell for demo
    cells[7].type = "Dirt"
    cells[12].type = "Town"
    cells[3].mine = True
    cells[3].growth = 80
    map_data = MapData(width=width, height=height, cells=cells)
    app = MapVisualizer(map_data)
    app.mainloop()
