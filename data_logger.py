import os
import csv

class DataLogger:
    def __init__(self, filename="simulation_data.csv"):
        """
        Initialize the data logger.
        TODO: Create a CSV file with headers if it doesn't exist or is empty.
        :param filename: Name of the CSV file.
        """
        self.filename = filename
        pass

    def log_data(self, environment, crop):
        """
        Log environmental conditions and crop health to CSV.
        TODO: Append a new row with temperature, humidity, pest_level, and crop health.
        :param environment: Dictionary of environmental conditions.
        :param crop: Instance of Crop.
        """
        pass
