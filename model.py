import json
import random
import typing

import matplotlib.pyplot as plt

from cell import Cell
from plant import Plant
from settings import ModelSettings
from settings import PlantSettings
from utils import dict_to_dataclass


class Model:

    settings: ModelSettings
    space: typing.List[typing.List[Cell]]

    def __init__(self):
        with open('settings.json', 'r') as file:
            full_settings = json.load(file)
            self.settings = dict_to_dataclass(ModelSettings, full_settings)
            space_size = self.settings.space_size
            self.space = [
                [
                    self.create_cell(full_settings) for _ in range(space_size)
                ] for _ in range(space_size)
            ]

    @staticmethod
    def create_cell(settings: typing.Dict) -> Cell:
        plant_settings: PlantSettings = dict_to_dataclass(
            PlantSettings, settings,
        )
        volume = random.randint(0, plant_settings.maximum_value)
        return Cell(
            plant_object=Plant(volume=volume, settings=plant_settings)
        )

    def start(self):
        for iteration_number in range(self.settings.iterations_count):
            plot_data = []
            space_size = self.settings.space_size
            for i in range(space_size):
                plot_data.append([self.space[i][j].iter(
                    iteration_number) for j in range(space_size)])
            if iteration_number % 30 == 0:
                plt.imshow(plot_data)
                plt.show()
