class Figure:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"name:{self.name},color{self.color}"