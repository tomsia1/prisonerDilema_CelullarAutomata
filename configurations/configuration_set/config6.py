from configurations.configuration import Configuration

import numpy as np
from pathlib import Path

from graph.grid_graph.neighbourhoods import Neighbourhood
from strategy.alwaysCooperate import AlwaysCooperate
from strategy.alwaysDefect import AlwaysDefect
from strategy.titForTat import TitForTat
from strategy.pavlov import Pavlov
from graph.grid_graph.gridGraph import GridGraph
from visualization.gridVisualizer import GridVisualizer
from rewards import PRISONER_REWARDS

np.random.seed(0)

neighbourhood = Neighbourhood.MANHATTAN2

mapping = [AlwaysCooperate(), AlwaysDefect(), TitForTat(), Pavlov()]

r = np.random.randint(0, 4, (100, 100))
strategy_grid = np.empty(r.shape, object)
for i, row in enumerate(r):
    for j, elm in enumerate(row):
        strategy_grid[i, j] = AlwaysCooperate()

for x in range(-2, 3):
    for y in range(-2, 3):
        strategy_grid[50+x, 50+y] = AlwaysDefect()
# strategy_grid[50, 50] = AlwaysDefect()

graph_config = {
    'neighbourhood': neighbourhood,
    'strategy_grid': strategy_grid
}

graph = GridGraph().build(graph_config)
visualizer = GridVisualizer(graph)

config6 = Configuration(
    graph=graph,
    visualizer=visualizer,
    visualizer_interval=1,
    num_round_per_play=2,
    num_epochs=50,
    rewards=PRISONER_REWARDS,
    save_path=Path("results/res6")
)
