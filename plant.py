from simulating_object import SimulatingObject
from settings import PlantSettings


class Plant(SimulatingObject):

    volume: int
    settings: PlantSettings

    def __init__(self, volume, settings):
        self.volume = volume
        self.settings = settings

    def is_vegetative_period(self, iter_value):
        iter_in_year = iter_value % self.settings.iterations_per_year
        if iter_in_year < self.settings.vegetative_start:
            return False
        if iter_in_year > self.settings.vegetative_end:
            return False

        return True

    def iter(self, iteration_number):
        if (
                self.is_vegetative_period(iteration_number) and
                self.volume >= self.settings.minimum_value
        ):
            self.volume = min(
                self.volume + self.settings.increase_coefficient,
                self.settings.maximum_value,
            )

        return self.volume
