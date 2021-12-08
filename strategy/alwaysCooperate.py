from strategy.strategyInterface import StrategyInterface
from strategy.moves import Moves


class AlwaysCooperate(StrategyInterface):
    def play(self, my_history, opponent_history):
        return Moves.COOPERATE

    def get_name(self):
        return 'coop'

    def get_marker(self):
        return 200, 200, 200
