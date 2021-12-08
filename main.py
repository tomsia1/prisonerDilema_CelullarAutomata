from engine.simulationEngine import SimulationEngine


def main(config):

    engine = SimulationEngine(config.graph, config.visualizer, config.rewards)
    engine.run(config.num_round_per_play, config.num_epochs, config.visualizer_interval, config.save_path)


if __name__ == '__main__':

    # from configurations.configuration_set.config1 import config1 as config
    from configurations.configuration_set.config_lasftm_asia_1 import config_lasftm_asia_1 as config

    main(config)


