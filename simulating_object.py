import abc


class SimulatingObject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def iter(self, iter_value: int):
        pass
