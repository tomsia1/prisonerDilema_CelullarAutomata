from abc import ABC, abstractmethod
import matplotlib.patches as patches


class VisualizerInterface(ABC):
    @abstractmethod
    def __init__(self, graph):
        labels = {}
        for u in graph:
            name = u.strategy.get_name()
            marker = u.strategy.get_marker()
            labels[name] = tuple(x / 255 for x in marker)

        self.patches = [patches.Patch(color=colour, label=label) for label, colour in labels.items()]

    @abstractmethod
    def draw(self, save_path, show):
        pass
