class Node:
    def __init__(self, strategy):
        self.idx = -1

        self.strategy = strategy
        self.next_strategy = None
        self.score = 0

        self.neighbours = set()

    def check_update(self):
        update = False
        max_score = self.score
        for neighbour in self.neighbours:
            if neighbour.score >= max_score and neighbour.strategy.get_name() == self.strategy.get_name():
                max_score = neighbour.score
                self.next_strategy = None
                update = False
            elif neighbour.score > max_score:
                max_score = neighbour.score
                self.next_strategy = neighbour.strategy
                update = True

        return update

    def update(self):
        self.strategy = self.next_strategy
        self.next_strategy = None

    def set_idx(self, idx):
        self.idx = idx

    def zero_score(self):
        self.score = 0