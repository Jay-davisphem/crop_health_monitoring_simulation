import config
import random

class Environment:
    def __init__(self):
        """
        Initialize default environmental conditions using values from config.
        """
        self.temperature = config.INITIAL_TEMPERATURE
        self.humidity = config.INITIAL_HUMIDITY
        self.pest_level = config.INITIAL_PEST_LEVEL

    def update_conditions(self):
        """
        Randomly fluctuate the environmental conditions based on configurable ranges.
        Ensures values stay within valid limits.
        """
        # Fluctuate temperature but keep it within a reasonable range (e.g., 0°C to 50°C)
        self.temperature += random.uniform(config.TEMP_FLUCTUATION_MIN, config.TEMP_FLUCTUATION_MAX)
        self.temperature = max(config.MIN_TEMPERATURE, min(self.temperature, config.MAX_TEMPERATURE))

        # Fluctuate humidity but keep it within the valid range of 0% to 100%
        self.humidity += random.uniform(config.HUMIDITY_FLUCTUATION_MIN, config.HUMIDITY_FLUCTUATION_MAX)
        self.humidity = max(0, min(self.humidity, 100))

        # Fluctuate pest level (ensuring it stays between 0 and 10)
        self.pest_level = max(
            0,
            min(
                10,
                self.pest_level + random.choice(config.PEST_LEVEL_FLUCTUATIONS)
            )
        )

    def get_conditions(self):
        """
        Return the current environmental conditions as a dictionary.
        """
        return {
            "temperature": self.temperature,
            "humidity": self.humidity,
            "pest_level": self.pest_level
        }
