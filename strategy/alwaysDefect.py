from strategy.strategyInterface import StrategyInterface
from strategy.moves import Moves


class AlwaysDefect(StrategyInterface):
    def play(self, my_history, opponent_history):
        return Moves.DEFECT

    def get_name(self):
        return 'defect'

    def get_marker(self):
        return 0, 0, 0
