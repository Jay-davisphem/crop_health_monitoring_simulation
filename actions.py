class Actions:
    def __init__(self, environment, crop):
        """
        Initialize actions with the environment and crop objects.
        :param environment: Instance of Environment.
        :param crop: Instance of Crop.
        """
        self.environment = environment
        self.crop = crop

    def water_crops(self):
        """
        Water the crops to increase humidity.
        TODO: Implement logic to increase the humidity and return a descriptive message.
        """
        pass

    def apply_pesticide(self):
        """
        Apply pesticide to reduce pest levels.
        TODO: Implement logic to decrease pest level and return a descriptive message.
        """
        pass

    def apply_fertilizer(self):
        """
        Apply fertilizer to boost crop health.
        TODO: Increase crop health and return a descriptive message.
        """
        pass
