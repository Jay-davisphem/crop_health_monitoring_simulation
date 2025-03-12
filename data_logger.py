import os
import csv

class DataLogger:
    def __init__(self, filename="synthetic_crop_data_10000_uniform.csv"):
        self.filename = filename
        # Create the CSV file with headers if it doesn't exist or is empty
        if not os.path.exists(self.filename) or os.stat(self.filename).st_size == 0:
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["temperature", "humidity", "pest_level", "crop_health"])

    def log_data(self, environment, crop):
        # Log a row of data: environment conditions and crop health
        data = [
            environment["temperature"],
            environment["humidity"],
            environment["pest_level"],
            crop.get_health()
        ]
        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(data)
