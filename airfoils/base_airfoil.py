class BaseAirfoil:
    def __init__(self, name):
        self.name = name
        self.nose_radius = None
        self.max_thickness = None
        self.camber = None
        self.thickness_position = None

    def describe(self):
        return f"{self.name} (Camber: {self.camber}, Thickness: {self.max_thickness})"
