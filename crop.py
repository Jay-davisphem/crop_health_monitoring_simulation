import config

class Crop:
    def __init__(self):
        # Initialize crop health using the HEALTHY value from config.
        self.health = config.HEALTHY

    def update_health(self, environment):
        # Retrieve current environmental conditions, defaulting to initial values if missing.
        temperature = environment.get("temperature", config.INITIAL_TEMPERATURE)
        humidity = environment.get("humidity", config.INITIAL_HUMIDITY)
        pest_level = environment.get("pest_level", config.INITIAL_PEST_LEVEL)

        # Adjust health based on temperature conditions.
        if temperature < config.TEMP_LOW_THRESHOLD or temperature > config.TEMP_HIGH_THRESHOLD:
            self.health -= config.TEMP_PENALTY
        elif config.OPTIMAL_TEMP_LOW <= temperature <= config.OPTIMAL_TEMP_HIGH:
            self.health += config.TEMP_BONUS

        # Adjust health based on humidity conditions.
        if humidity < config.HUMIDITY_LOW_THRESHOLD or humidity > config.HUMIDITY_HIGH_THRESHOLD:
            self.health -= config.HUMIDITY_PENALTY
        elif config.OPTIMAL_HUMIDITY_LOW <= humidity <= config.OPTIMAL_HUMIDITY_HIGH:
            self.health += config.HUMIDITY_BONUS

        # Adjust health based on pest level.
        if pest_level > config.PEST_THRESHOLD:
            self.health -= config.PEST_PENALTY

        # Ensure the crop's health remains within valid bounds [0, config.HEALTHY]
        self.health = max(0, min(self.health, config.HEALTHY))

    def get_health(self):
        # Return the current health of the crop.
        return self.health
