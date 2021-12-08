from visualization.visualizerInterface import VisualizerInterface

import networkx as nx

import matplotlib.pyplot as plt


class NetworkxVisualizer(VisualizerInterface):
    def __init__(self, graph):
        super().__init__(graph)

        self.graph = nx.Graph()
        self.color_graph = graph

        for u in graph:
            self.graph.add_node(u.idx)

        added_self_loops = set()
        for u in graph:
            for v in u.neighbours:
                if u.idx < v.idx:
                    self.graph.add_edge(u.idx, v.idx)
                elif u.idx == v.idx and u.idx not in added_self_loops:
                    added_self_loops.add(u.idx)
                    self.graph.add_edge(u.idx, v.idx)

        self.pos = nx.spring_layout(self.graph, seed=0)

        self.node_size = [15] * len(graph)

    def draw(self, save_path=None, show=True):
        color_map = []
        for u in self.color_graph:
            r, g, b = u.strategy.get_marker()
            color_map.append((r / 255, g / 255, b / 255))

        plt.legend(handles=self.patches, bbox_to_anchor=(0.9, 1.1), loc=2)

        nx.draw(self.graph, self.pos, node_color=color_map, node_size=self.node_size)

        if show:
            plt.show()

        if save_path:
            plt.savefig(save_path)

        plt.clf()


