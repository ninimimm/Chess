class Cage:
    def __init__(self, color, coordinate, figure = None):
        self.coordinate = coordinate
        self.figure = figure
        self.color = color

    def __str__(self):
        return f"{self.color[0]},f:{str(self.figure)}"