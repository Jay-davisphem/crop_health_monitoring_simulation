
### Module Breakdown

- **environment.py** – Simulates environmental factors like temperature, humidity, and soil moisture.
- **crop.py** – Models crop behavior, health, and response to environmental conditions.
- **monitoring.py** – Tracks the crop’s health and triggers alerts if any conditions become critical.
- **actions.py** – Implements possible actions that affect the crop’s growth and environmental parameters.
- **data_logger.py** – Stores simulation data in a CSV format for later analysis.
- **ml_model.py** – Trains and applies a machine learning model to predict crop health trends.
- **visualization.py** – Generates graphs and charts to visualize simulation results.
- **simulation.py** – Runs the core simulation loop, updating values over time.
- **main.py** – The script to start and control the entire simulation.
- **config.py** – Holds configuration values such as the number of time steps, threshold values, etc.
- **utils.py** – A set of utility functions used across multiple modules.
- **logger.py** – Centralized logging and debugging system.
- **tests.py** – Unit tests for verifying the correctness of individual components.

---

## Installation

### Prerequisites
- **Python 3.6+** must be installed.

### 1. Clone the Repository
```bash
git clone https://github.com/jay-davisphem/crop_health_monitoring_simulation.git
cd crop_health_monitoring_simulation


python3 -m venv env # if not no virtual environment

# Activate the virtual environment
source env/bin/activate # macOS/linux
env\Scripts\activate.bat  (for CMD)
.\env\Scripts\Activate.ps1  (for PowerShell)

# Install dependencies
pip install -r requirements.txt

# Usage

# Running simulation
python main.py

# Visualizing Data
python -c "from visualization import DataVisualization; DataVisualization().plot_data('synthetic_crop_data_10000_uniform.csv')"

# Deactivating the Virtual Environment
deactivate


# Possible issues on windows, if encountered
Set-ExecutionPolicy RemoteSigned


```


# Crop Simulation Project: Architecture Overview

The Crop Simulation Project is designed to simulate monitoring of crop health under dynamic environmental conditions. This project models the interplay between external factors (like temperature, humidity, and pest levels) and crop health over time. The system is built using a modular architecture where each file encapsulates a specific responsibility. Below is a detailed explanation of how each component works and how they integrate to create the full simulation.

## Overall Workflow

1. **Initialization:**  
   - The simulation is launched via the `main.py` file, which sets up a SimPy environment.
   - An instance of the `Simulation` class (from `simulation.py`) is created, which in turn instantiates all the core components needed for the simulation.

2. **Environmental Conditions:**  
   - The `environment.py` module defines the `Environment` class. This class initializes the simulation with default environmental parameters such as temperature, humidity, and pest level.
   - The `update_conditions` method in this module simulates natural fluctuations by randomly altering these parameters, mimicking real-world variations.

3. **Crop Health Management:**  
   - The `crop.py` module contains the `Crop` class, responsible for managing the crop's health.
   - The crop's health is influenced by the environmental conditions provided by the `Environment` class. Extreme conditions (e.g., high/low temperatures, low humidity, or high pest levels) cause a decrement in health.
   - The method `update_health` uses these conditions to adjust the crop's health accordingly.

4. **Monitoring and Alerts:**  
   - The `monitoring.py` module implements the `MonitoringSystem` class. It continuously monitors the crop's health.
   - When the crop’s health falls below a certain threshold, the system generates a warning alert; otherwise, it reports that the crop health is stable.
   - This real-time feedback is essential for determining if any corrective actions are needed.

5. **Intervention Actions:**  
   - The `actions.py` module defines the `Actions` class, which provides functions to interact with the simulation.
   - Actions include watering the crops (to increase humidity), applying pesticides (to reduce pest levels), and using fertilizer (to boost crop health).
   - These actions serve as interventions that can mitigate adverse conditions and help maintain or improve the crop's health.

6. **Data Logging:**  
   - The `data_logger.py` module is responsible for persisting the state of the simulation.
   - The `DataLogger` class logs key data points (such as environmental conditions and crop health) to a CSV file at every simulation step.
   - This logged data serves as a historical record and is later used for analysis and model training.

7. **Machine Learning Predictions:**  
   - The `ml_model.py` module introduces the `CropHealthPredictor` class.
   - Using the data logged in the CSV file, this module trains a `RandomForestRegressor` model to predict future crop health based on current environmental conditions.
   - This predictive capability helps forecast trends and can be used to proactively adjust interventions.

8. **Data Visualization:**  
   - The `visualization.py` module contains the `DataVisualization` class.
   - It reads the CSV data and produces visual representations (like plots of crop health over time) using matplotlib.
   - Visualization aids in understanding simulation trends and the impact of various factors over time.

9. **Central Simulation Loop:**  
   - The `simulation.py` module acts as the central orchestrator.
   - The `Simulation` class in this file ties together all the above components. It maintains a continuous loop (using SimPy) where:
     - The environment is updated.
     - The crop’s health is recalculated.
     - Data is logged.
     - The monitoring system checks the crop’s status.
     - The machine learning model makes predictions when applicable.
   - This loop simulates the passage of time and ensures all parts of the system are synchronized.

10. **Configuration Management:**  
    - The `config.py` module centralizes key simulation parameters such as the simulation duration, update intervals, and initial environmental settings.
    - By keeping configuration values in one place, it becomes easy to adjust simulation settings without modifying multiple files.

11. **Utility Functions:**  
    - The `utils.py` module provides helper functions that are used across different modules.
    - Functions here handle common tasks like formatting data and validating inputs, ensuring consistency and reducing code duplication.

12. **Logging and Error Handling:**  
    - The `logger.py` module sets up centralized logging and error-handling.
    - It configures the logging system to capture and report errors or significant events, making it easier to debug and maintain the system.

## How the Files Work Together

- **Entry Point (`main.py`):**  
  This is where the simulation starts. The file creates a SimPy environment, instantiates the `Simulation` class, and begins the simulation loop.

- **Simulation Integration (`simulation.py`):**  
  The Simulation class is the heart of the project. It brings together the environment, crop, monitoring, actions, logging, and ML prediction modules. Each cycle of the simulation loop:
  - Calls the environment to update its conditions.
  - Updates the crop's health based on these new conditions.
  - Logs the current state to the CSV file.
  - Uses the monitoring system to check crop health and trigger alerts if necessary.
  - Optionally uses the ML model to predict future crop health.
  
- **Data Handling:**  
  Both the `data_logger.py` and `visualization.py` modules work on the simulation data. DataLogger ensures that every state is saved, while DataVisualization helps in analyzing this data visually after or during the simulation.

- **Decision Making:**  
  The monitoring and actions modules enable decision-making within the simulation. Monitoring provides real-time feedback on the crop's status, and the actions module defines how to intervene (for example, watering or pesticide application) to mitigate adverse conditions.

- **Predictive Analysis:**  
  The ML component (ml_model.py) leverages historical data to forecast crop health. This predictive insight can eventually help in automating some intervention decisions or understanding long-term trends.

- **Supporting Infrastructure:**  
  The `config.py`, `utils.py`, and `logger.py` modules provide foundational support by offering configuration management, utility functions, and robust logging/error handling. They ensure that the system is flexible, maintainable, and easy to debug.

## Summary

The Crop Simulation Project is an integrated system where:
- **Environmental factors** are dynamically simulated.
- **Crop health** is continuously updated based on these factors.
- **Real-time monitoring** provides feedback on the system’s state.
- **Interventions** are available to influence the simulation.
- **Data logging and visualization** facilitate analysis.
- **Machine learning** adds predictive capabilities.

This modular design allows for easy maintenance and scalability, making it possible to add new features or modify existing ones without impacting the entire system. Each file has a clearly defined role, ensuring that team members can work independently on different parts while understanding how they fit into the overall project.

Happy coding, and feel free to ask in the whatsapp group if you need any more details!
