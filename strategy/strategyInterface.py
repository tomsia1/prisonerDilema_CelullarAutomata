from abc import ABC, abstractmethod


class StrategyInterface(ABC):

    @abstractmethod
    def play(self, my_history, opponent_history):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_marker(self):
        pass
