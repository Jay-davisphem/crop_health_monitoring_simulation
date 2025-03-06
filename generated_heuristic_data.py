# generate_dataset_10000_uniform.py
import csv
import random

def clamp(val, minimum=0, maximum=100):
    return max(minimum, min(val, maximum))

with open("synthetic_crop_data_10000_uniform.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # Write header row
    writer.writerow(["temperature", "humidity", "pest_level", "crop_health"])
    
    for _ in range(10000):
        # Generate uniformly random values within specified ranges
        temperature = random.uniform(10, 40)      # Temperature between 10°C and 40°C
        humidity = random.uniform(20, 100)          # Humidity between 20% and 100%
        pest_level = random.randint(0, 10)          # Pest level as an integer from 0 to 10
        noise = random.uniform(-2, 2)               # Noise between -2 and +2
        
        # Apply penalties:
        temp_penalty = 5 if temperature > 35 else 0
        pest_penalty = pest_level * 2
        
        # Compute crop health based on our heuristic
        crop_health = 100 - temp_penalty - pest_penalty + noise
        crop_health = clamp(crop_health)
        
        writer.writerow([
            round(temperature, 2),
            round(humidity, 2),
            pest_level,
            round(crop_health, 2)
        ])

print("CSV file 'synthetic_crop_data_10000_uniform.csv' generated with 10000 rows.")

