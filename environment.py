import config
import random

class Environment:
    def __init__(self):
        """
        Initialize default environmental conditions.
        TODO: Set initial temperature, humidity, and pest_level.
        """
        self.temperature = config.INITIAL_TEMPERATURE  # Example default
        self.humidity = config.INITIAL_HUMIDITY     # Example default
        self.pest_level = config.INITIAL_PEST_LEVEL    # Example default

    def update_conditions(self):
        """
        Update environmental conditions with random fluctuations.
        TODO: Implement logic to adjust temperature, humidity, and pest_level.
        """
        pass

    def get_conditions(self):
        """
        Return current environmental conditions as a dictionary.
        TODO: Return a dict with keys: 'temperature', 'humidity', 'pest_level'.
        """
        pass
