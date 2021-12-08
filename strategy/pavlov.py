from strategy.strategyInterface import StrategyInterface
from strategy.moves import Moves


class Pavlov(StrategyInterface):
    def play(self, my_history, opponent_history):
        if len(my_history) == 0 or (my_history[-1] == opponent_history[-1]):
            return Moves.COOPERATE
        return Moves.DEFECT

    def get_name(self):
        return 'pavlov'

    def get_marker(self):
        return 0, 0, 255