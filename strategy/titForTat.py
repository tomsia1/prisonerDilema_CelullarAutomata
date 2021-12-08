from strategy.strategyInterface import StrategyInterface
from strategy.moves import Moves


class TitForTat(StrategyInterface):
    def play(self, my_history, opponent_history):
        return ([Moves.COOPERATE] + opponent_history)[-1]

    def get_name(self):
        return 'tit-for-tat'

    def get_marker(self):
        return 0, 255, 0