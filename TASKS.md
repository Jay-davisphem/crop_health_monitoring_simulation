# Crop Health Monitoring Simulation Project

This project simulates crop health under varying environmental conditions. The code is modularized into 12 independent components, each responsible for a specific part of the simulation. Below is an overview of each module with a description of its purpose and tasks to accomplish.

## 1. environment.py
**Purpose:** Simulate environmental conditions affecting the crop.  
**Responsibilities:**
- Initialize default parameters (temperature, humidity, pest level).
- Update these conditions with random fluctuations.
- Provide a method to retrieve the current conditions.

**TODO:**  
- Implement logic in `update_conditions` to adjust temperature, humidity, and pest level.
- Return the updated conditions in `get_conditions`.

---

## 2. crop.py
**Purpose:** Model the crop and manage its health status.  
**Responsibilities:**
- Initialize the crop with a default health value.
- Update the crop's health based on environmental factors (e.g., extreme temperature, low humidity, high pest levels).
- Provide a method to retrieve the current health.

**TODO:**  
- Implement health adjustment logic in `update_health`.
- Ensure `get_health` returns the correct crop health.

---

## 3. monitoring.py
**Purpose:** Monitor the crop’s health and generate alerts if necessary.  
**Responsibilities:**
- Check if the crop's health is within a safe range.
- Return a status message (e.g., warning if health is critical, stable if not).
- Provide a complete status report including health and any alerts.

**TODO:**  
- Implement the health checking logic in `check_health_status`.
- Ensure `get_status_report` returns a dictionary with current health and alert message.

---

## 4. actions.py
**Purpose:** Define actions to modify the simulation state.  
**Responsibilities:**
- Implement actions such as watering the crops, applying pesticide, and applying fertilizer.
- Each action should affect either the environmental conditions or the crop's health.
- Return a descriptive message for each action taken.

**TODO:**  
- Code the logic for `water_crops`, `apply_pesticide`, and `apply_fertilizer`.

---

## 5. data_logger.py
**Purpose:** Log simulation data persistently in a CSV file.  
**Responsibilities:**
- Create or initialize a CSV file with proper headers.
- Append new rows of data capturing environmental conditions and crop health.

**TODO:**  
- Implement file creation in the constructor.
- Write the data logging logic in `log_data`.

---

## 6. ml_model.py
**Purpose:** Predict crop health using a machine learning model.  
**Responsibilities:**
- Set up a `RandomForestRegressor` or `others` model.
- Train the model on historical simulation data logged in the CSV file.
- Provide predictions based on current environmental conditions.

**TODO:**  
- Develop the `train` method to load data and fit the model.
- Implement the `predict` method to return crop health predictions.

---

## 7. visualization.py  
**Purpose:** Visualize simulation data from the CSV log.  

### Tasks:  
- Read and process the CSV data.  
- Plot the impact of temperature, humidity, and pest level on crop health.  
- Use Seaborn/Matplotlib for effective visualization.  


## 8. simulation.py
**Purpose:** Integrate all components into a cohesive simulation loop.  
**Responsibilities:**
- Create instances of Environment, Crop, MonitoringSystem, Actions, DataLogger, and CropHealthPredictor.
- Manage the simulation loop using SimPy.
- Update environmental conditions, adjust crop health, log data, and predict crop health periodically.

**TODO:**  
- Write the simulation loop in the `run` method to call each component appropriately.

---

## 9. main.py
**Purpose:** Serve as the entry point to run the simulation.  
**Responsibilities:**
- Initialize the SimPy environment.
- Instantiate the Simulation class.
- Run the simulation for a specified duration (e.g., 50 time units).

**DONE:**  
- Ensure proper instantiation and execution of the simulation process.

---

## 10. config.py
**Purpose:** Centralize simulation configuration parameters.  
**Responsibilities:**
- Define constants like simulation duration, update interval, and initial environmental conditions.

**DONE:**  
- Set and document the configuration constants for easy modification.

---

## 11. utils.py
**Purpose:** Provide helper functions for common tasks across the project.  
**Responsibilities:**
- Implement utility functions for data formatting, validation, and other common calculations.

**DONE:**  
- Develop reusable functions to streamline code in other modules (e.g., `format_conditions` and `validate_data`).

---

## 12. logger.py
**Purpose:** Centralize logging and error handling for the project.  
**Responsibilities:**
- Set up a logging configuration using Python’s `logging` module.
- Provide helper functions for logging errors and other messages.

**DONE:**  
- Implement `setup_logger` for configuring the logger.
- Code the `log_error` function to capture and report errors.

---
## 13. Dataset Sourcing
**Responsibilities**
Find dataset that will include, temperature, humidity, pest_control and crop_health.
Presently, I included a heuristic (generated based on some patterns) based dataset.

NOTE: the field names(the ones you find) might be a bit different from the project's.

---
## 14. Slide Presentation Task

**Objective:**  
  Create a slide presentation (using Microsoft PowerPoint or Google Slides) that showcases the Crop Health Monitoring Simulation.

- **Content to Include:**  
  - **Title Slide:** Project title, tagline, presenter name(s), and date.  
  - **Overview:**  
    - Describe the simulation’s purpose (monitoring crop health based on environmental conditions).  
    - **Note:** Explain that initially, the simulation was run without ML, and later ML was integrated to predict crop health—demonstrating how ML complements and enhances the DES (Discrete Event Simulation) system as taught in class.
  - **Architecture:**  
    - Use a diagram or bullet points to outline key modules (environment, crop, monitoring, actions, data logging, ML prediction, visualization, simulation, configuration, utilities, and logging).
  - **Key Features:**  
    - Detail how the simulation updates conditions, manages crop health, triggers actions, logs data, and integrates ML for predictions.
    - Use Discrete Event Simulation terms.
  - **Results:**  
    - Present example outputs (screenshots, graphs, alerts).
  - **Future Enhancements:**  
    - List potential improvements.
  - **Conclusion & Q&A:**  
    - Summarize the project
---
