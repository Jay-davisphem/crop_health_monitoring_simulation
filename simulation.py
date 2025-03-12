import pandas as pd
from environment import Environment
from crop import Crop
from monitoring import MonitoringSystem
from actions import Actions
from data_logger import DataLogger
from ml_model import CropHealthPredictor
from utils import format_conditions
from logger import setup_logger, log_error

class Simulation:
    def __init__(self, env):
        self.env = env
        # Set up the centralized logger
        self.log = setup_logger()
        
        # Instantiate simulation components
        self.environment = Environment()
        self.crop = Crop()
        self.monitoring = MonitoringSystem(self.crop)
        self.actions = Actions(self.environment, self.crop)
        self.logger = DataLogger()  # CSV logger for simulation data
        self.ml_model = CropHealthPredictor()

    def run(self):
        while True:
            try:
                # Update environmental conditions and crop health
                self.environment.update_conditions()
                current_conditions = self.environment.get_conditions()
                self.crop.update_health(current_conditions)

                # Apply actions based on current conditions
                # For example, water the crops if humidity is too low
                if current_conditions["humidity"] < 40:
                    water_message = self.actions.water_crops()
                    self.log.info(water_message)
                    # Update conditions after action (if needed)
                    current_conditions = self.environment.get_conditions()

                # Apply pesticide if pest level is high
                if current_conditions["pest_level"] > 5:
                    pesticide_message = self.actions.apply_pesticide()
                    self.log.info(pesticide_message)
                    current_conditions = self.environment.get_conditions()

                # Apply fertilizer if crop health is below a threshold
                if self.crop.get_health() < 80:
                    fertilizer_message = self.actions.apply_fertilizer()
                    self.log.info(fertilizer_message)
                    current_conditions = self.environment.get_conditions()

                # Log simulation data to CSV
                self.logger.log_data(current_conditions, self.crop)

                # Log formatted environmental conditions using the utility function
                self.log.info(format_conditions(current_conditions))

                # Log the monitoring status report
                status_report = self.monitoring.get_status_report()
                self.log.info(str(status_report))

                # Use the ML model to predict crop health if it's trained, and log the prediction
                if self.ml_model.is_trained:
                    # features = pd.DataFrame([current_conditions])
                    predicted_health = self.ml_model.predict(current_conditions)
                    self.log.info(f"🔮 Predicted Crop Health: {predicted_health}")

                # Advance the simulation by one time unit
                yield self.env.timeout(1)
            except Exception as e:
                # Log any exceptions using the logger
                log_error(e)
