# actions.py

class Actions:
    def __init__(self, environment, crop):
        # Initialize with Environment and Crop instances
        self.environment = environment
        self.crop = crop
    
    def water_crops(self):
        # Increase humidity by watering the crops
        self.environment.humidity += 10
        return "💧 Watered crops, increasing humidity."
    
    def apply_pesticide(self):
        # Decrease pest level by applying pesticide
        self.environment.pest_level = max(0, self.environment.pest_level - 3)
        return "🛡️ Pesticide applied, reducing pest level."
    
    def apply_fertilizer(self):
        # Boost crop health by applying fertilizer
        self.crop.health = min(100, self.crop.health + 5)
        return "🌱 Fertilizer applied, boosting crop health."
