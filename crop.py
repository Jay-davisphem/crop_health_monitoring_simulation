import config

class Crop:
    def __init__(self):
        """Initialize crop health with the max HEALTHY value from config."""
        self.health = config.HEALTHY
        self.stress_duration = 0  # Tracks how long the crop is in bad conditions

    def update_health(self, environment):
        """Adjust crop health based on environmental conditions over time."""
        temperature = environment.get("temperature", config.INITIAL_TEMPERATURE)
        humidity = min(100, max(0, environment.get("humidity", config.INITIAL_HUMIDITY)))  # Ensuring realistic range
        pest_level = environment.get("pest_level", config.INITIAL_PEST_LEVEL)

        health_change = 0  # Accumulator for health changes

        # Temperature impact
        if temperature < config.TEMP_LOW_THRESHOLD or temperature > config.TEMP_HIGH_THRESHOLD:
            self.stress_duration += 1  # Track stress over time
            health_change -= config.TEMP_PENALTY * (1 + self.stress_duration / 10)  # Progressive damage
        elif config.OPTIMAL_TEMP_LOW <= temperature <= config.OPTIMAL_TEMP_HIGH:
            self.stress_duration = max(0, self.stress_duration - 1)  # Reduce stress if optimal
            health_change += config.TEMP_BONUS

        # Humidity impact
        if humidity < config.HUMIDITY_LOW_THRESHOLD or humidity > config.HUMIDITY_HIGH_THRESHOLD:
            health_change -= config.HUMIDITY_PENALTY
        elif config.OPTIMAL_HUMIDITY_LOW <= humidity <= config.OPTIMAL_HUMIDITY_HIGH:
            health_change += config.HUMIDITY_BONUS

        # Pest impact
        if pest_level > config.PEST_THRESHOLD:
            health_change -= config.PEST_PENALTY * (pest_level / 10)  # More pests = worse impact

        # Apply health changes gradually
        self.health = max(0, min(config.HEALTHY, self.health + health_change))

    def get_health(self):
        """Return the current health of the crop."""
        return round(self.health, 2)  # Round for cleaner output
