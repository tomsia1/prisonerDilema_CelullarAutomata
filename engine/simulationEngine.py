import os
import shutil
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class SimulationEngine:
    def __init__(self, graph, visualizer, rewards):
        self.graph = graph
        self.visualizer = visualizer

        self.rewards = rewards
        
        # name : color
        self.strategy_dict = {}
        for u in self.graph:
            r, g, b = u.strategy.get_marker()
            self.strategy_dict[u.strategy.get_name()] = (r / 255, g / 255, b / 255)

        self.patches = [patches.Patch(color=colour, label=label) for label, colour in self.strategy_dict.items()]

    def play(self, u, v, num_rounds, hist_len):
        u_history = []
        v_history = []

        for _ in range(num_rounds):
            u_action = u.strategy.play(u_history, v_history)
            v_action = v.strategy.play(v_history, u_history)

            u.score += self.rewards[u_action.value][v_action.value]
            v.score += self.rewards[v_action.value][u_action.value]

            u_history.append(u_action)
            u_history = u_history[-hist_len:]

            v_history.append(v_action)
            v_history = v_history[-hist_len:]

    def _update_strategy_count(self, count_dict):
        counter = Counter()
        for u in self.graph:
            counter[u.strategy.get_name()] += 1
        
        for name, count in counter.items():
            count_dict[name].append(count)

    def _plot_strategy_count(self, save_path, strategy_count_per_epoch):
        for name, count in strategy_count_per_epoch.items():
            color = self.strategy_dict[name]

            plt.plot(count, color=color)
        
        lgd = plt.legend(handles=self.patches, bbox_to_anchor=(1.0, 1.1), loc=2)
        plt.savefig(save_path, bbox_extra_artists=(lgd,), bbox_inches='tight')

    def run(self, num_rounds, epochs, visualizer_interval, save_path):

        shutil.rmtree(save_path, ignore_errors=True)
        
        pictures_save_path = save_path / 'pictures'
        plots_save_path = save_path / 'plots'

        os.makedirs(pictures_save_path)
        os.makedirs(plots_save_path)

        strategy_count_per_epoch = {name: [] for name in self.strategy_dict}
        self._update_strategy_count(strategy_count_per_epoch)
        
        self.visualizer.draw(pictures_save_path / "_start.png", False)

        for i in range(epochs):
            print("EPOCH: {}".format(i))

            for u in self.graph:
                u.zero_score()

            for u in self.graph:
                for v in u.neighbours:
                    if u.idx <= v.idx:
                        self.play(u, v, num_rounds, 2)

            to_update = set()
            for u in self.graph:
                if u.check_update():
                    to_update.add(u)

            for u in to_update:
                u.update()

            self._update_strategy_count(strategy_count_per_epoch)

            if i % visualizer_interval == 0:
                name = "epoch_{}.png".format(i)
                self.visualizer.draw(pictures_save_path / name, False)

        self._plot_strategy_count(plots_save_path / 'strategy_count.png', strategy_count_per_epoch)
