from visualization.visualizerInterface import VisualizerInterface
import numpy as np
import matplotlib.pyplot as plt


class GridVisualizer(VisualizerInterface):
    def __init__(self, graph):
        super().__init__(graph)

        size = int(np.sqrt(len(graph)))
        self.poses = []
        for u in graph:
            self.poses.append((u.idx // size, u.idx % size))

        labels = {}
        for u in graph:
            name = u.strategy.get_name()
            marker = u.strategy.get_marker()
            labels[name] = tuple(x / 255 for x in marker)

        self.graph = graph
        self.grid = np.empty((size, size, 3), np.uint8)
        self.xticks = [0.5 + i for i in range(size)]
        self.yticks = [0.5 + i for i in range(size)]

    def draw(self, save_path=None, show=True):
        for u, pos in zip(self.graph, self.poses):
            self.grid[pos] = u.strategy.get_marker()

        # fig, ax = plt.subplots(1)
        fig = plt.figure()
        ax = plt.gca()
        ax.grid()
        ax.set_xticks(self.xticks)
        ax.set_yticks(self.yticks)
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.imshow(self.grid)
        ax.legend(handles=self.patches, bbox_to_anchor=(1.05, 1), loc=2)

        if show:
            plt.show()

        if save_path:
            fig.savefig(save_path, dpi=fig.dpi)

        plt.close(fig)
