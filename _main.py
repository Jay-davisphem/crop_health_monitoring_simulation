import random
import simpy
import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import os

# =========================
# environment.py
# =========================
class Environment:
    def __init__(self):
        self.temperature = 30
        self.humidity = 60
        self.pest_level = 2

    def update_conditions(self):
        self.temperature += random.uniform(-2, 2)
        self.humidity += random.uniform(-5, 5)
        self.pest_level = max(0, min(10, self.pest_level + random.choice([-1, 0, 1])))

    def get_conditions(self):
        return {
            "temperature": self.temperature,
            "humidity": self.humidity,
            "pest_level": self.pest_level
        }

# =========================
# crop.py
# =========================
class Crop:
    def __init__(self):
        self.health = 100
    
    def update_health(self, environment):
        if environment["temperature"] > 35 or environment["temperature"] < 15:
            self.health -= 5
        if environment["humidity"] < 30:
            self.health -= 3
        if environment["pest_level"] > 7:
            self.health -= 10
        self.health = max(0, self.health)
    
    def get_health(self):
        return self.health

# =========================
# monitoring.py
# =========================
class MonitoringSystem:
    def __init__(self, crop):
        self.crop = crop

    def check_health_status(self):
        health = self.crop.get_health()
        return "⚠️ Warning: Crop health is critical!" if health < 50 else "✅ Crop health is stable."
    
    def get_status_report(self):
        return {"crop_health": self.crop.get_health(), "alert": self.check_health_status()}

# =========================
# actions.py
# =========================
class Actions:
    def __init__(self, environment, crop):
        self.environment = environment
        self.crop = crop
    
    def water_crops(self):
        self.environment.humidity += 10
        return "💧 Watered crops, increasing humidity."
    
    def apply_pesticide(self):
        self.environment.pest_level = max(0, self.environment.pest_level - 3)
        return "🛡️ Pesticide applied, reducing pest level."
    
    def apply_fertilizer(self):
        self.crop.health = min(100, self.crop.health + 5)
        return "🌱 Fertilizer applied, boosting crop health."

# =========================
# data_logger.py
# =========================
class DataLogger:
    def __init__(self, filename="simulation_data.csv"):
        self.filename = filename
        if not os.path.exists(self.filename) or os.stat(self.filename).st_size == 0:
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["temperature", "humidity", "pest_level", "crop_health"])

    def log_data(self, environment, crop):
        data = [environment["temperature"], environment["humidity"], environment["pest_level"], crop.get_health()]
        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(data)

# =========================
# ml_model.py
# =========================
class CropHealthPredictor:
    def __init__(self, data_file="simulation_data.csv"):
        self.model = RandomForestRegressor()
        self.data_file = data_file
        self.is_trained = False
        if os.path.exists(self.data_file) and os.stat(self.data_file).st_size > 0:
            self.train()

    def train(self):
        df = pd.read_csv(self.data_file)
        if df.empty:
            print("⚠️ Warning: No data available for training. Please run the simulation longer to generate data.")
            return
        X, y = df.iloc[:, :-1], df.iloc[:, -1]
        self.model.fit(X, y)
        self.is_trained = True
    
    def predict(self, conditions):
        if not self.is_trained:
            print("⚠️ Warning: Model is not trained yet. Prediction may not be accurate.")
            return 100
        return self.model.predict([conditions])[0]

# =========================
# visualization.py
# =========================
class DataVisualization:
    def plot_data(self, data_file):
        df = pd.read_csv(data_file)
        plt.plot(df.index, df["crop_health"], label="Crop Health")
        plt.xlabel("Time")
        plt.ylabel("Health")
        plt.legend()
        plt.show()

# =========================
# simulation.py
# =========================
class Simulation:
    def __init__(self, env):
        self.env = env
        self.environment = Environment()
        self.crop = Crop()
        self.monitoring = MonitoringSystem(self.crop)
        self.actions = Actions(self.environment, self.crop)
        self.logger = DataLogger()
        self.ml_model = CropHealthPredictor()

    def run(self):
        while True:
            self.environment.update_conditions()
            self.crop.update_health(self.environment.get_conditions())
            self.logger.log_data(self.environment.get_conditions(), self.crop)
            print(self.monitoring.get_status_report())
            if os.stat("simulation_data.csv").st_size > 0 and self.ml_model.is_trained:
                predicted_health = self.ml_model.predict(list(self.environment.get_conditions().values()))
                print(f"🔮 Predicted Crop Health: {predicted_health}")
            yield self.env.timeout(1)

# =========================
# main.py
# =========================
if __name__ == "__main__":
    env = simpy.Environment()
    simulation = Simulation(env)
    env.process(simulation.run())
    env.run(until=50)

