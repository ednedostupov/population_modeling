from plant import Plant


class Cell:

    plant_object: Plant

    def __init__(self, plant_object: Plant):
        self.plant_object = plant_object

    def iter(self, iteration_number: int) -> int:
        plant_volume = self.plant_object.iter(iteration_number)
        return plant_volume
