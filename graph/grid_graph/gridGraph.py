from graph.graphInterface import GraphInterface
from graph.node import Node
from graph.grid_graph.neighbourhoods import neighbourhood_to_deltas
import numpy as np


class GridGraph(GraphInterface):
    def build(self, config):
        neighbourhood = config['neighbourhood']
        strategy_grid = config['strategy_grid']

        graph = np.empty(strategy_grid.shape, dtype=np.object)

        for i in range(graph.shape[0]):
            for j in range(graph.shape[1]):
                graph[i, j] = Node(strategy_grid[i, j])

        deltas = neighbourhood_to_deltas[neighbourhood]
        for i in range(graph.shape[0]):
            for j in range(graph.shape[1]):
                for di, dj in deltas:
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < graph.shape[0] and 0 <= nj < graph.shape[1]:
                        graph[i, j].neighbours.add(graph[ni, nj])

        flat = graph.flatten()
        for i, node in enumerate(flat):
            node.set_idx(i)

        return flat
