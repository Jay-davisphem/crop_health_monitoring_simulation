import config
class Crop:
    def __init__(self):
        """
        Initialize the crop with a default health value.
        TODO: Set the initial crop health.
        """
        self.health = config.HEALTHY  # Example default

    def update_health(self, environment):
        """
        Update crop health based on environmental conditions.
        TODO: Adjust crop health based on conditions such as temperature, humidity, and pest level.
        :param environment: Dictionary containing environmental conditions.
        """
        pass

    def get_health(self):
        """
        Return the current crop health.
        TODO: Return the crop's health value.
        """
        pass
