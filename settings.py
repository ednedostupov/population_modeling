import dataclasses


@dataclasses.dataclass(frozen=True)
class ModelSettings:
    iterations_count: int
    space_size: int
    iterations_per_year: int


@dataclasses.dataclass(frozen=True)
class PlantSettings(ModelSettings):
    vegetative_start: int
    vegetative_end: int
    minimum_value: int
    maximum_value: int
    increase_coefficient: int
