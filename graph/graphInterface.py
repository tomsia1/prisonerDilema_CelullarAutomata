from abc import ABC, abstractmethod


class GraphInterface(ABC):

    def __init__(self):
        self.nodes = []

    def get_node(self, idx):
        return self.nodes[idx]

    def get_all_nodes(self):
        return self.nodes

    @abstractmethod
    def build(self, config):
        pass
