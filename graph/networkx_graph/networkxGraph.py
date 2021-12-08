from graph.graphInterface import GraphInterface
from graph.node import Node


class NetworkxGraph(GraphInterface):
    @staticmethod
    def _make_node(i, strategy):
        node = Node(strategy)
        node.set_idx(i)
        return node

    @staticmethod
    def _get_distant_neighbours(u, radius):
        if radius == 0:
            return {u}

        result = set()
        for v in u.neighbours:
            result.update(NetworkxGraph._get_distant_neighbours(v, radius-1))

        return result

    def build(self, config):
        vertices_strategies = config['strategies']
        edge_list = config['edge_list']
        neighbour_radius = config['neighbour_radius']

        graph = [NetworkxGraph._make_node(i, strategy) for i, strategy in enumerate(vertices_strategies)]

        for u, v in edge_list:
            graph[u].neighbours.add(graph[v])
            graph[v].neighbours.add(graph[u])

        if neighbour_radius > 1:
            for u in graph:
                distant = NetworkxGraph._get_distant_neighbours(u, neighbour_radius)
                u.neighbours.update(distant)

        return graph
