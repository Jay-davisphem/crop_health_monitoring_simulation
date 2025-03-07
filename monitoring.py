from crop import Crop
class MonitoringSystem:
    def __init__(self, crop: Crop):
        # Initialize with a Crop instance
        self.crop = crop

    def check_health_status(self):
        # Check crop health and return an alert message if needed
        health = self.crop.get_health()
        if health < 50:
            return "⚠️ Warning: Crop health is critical!"
        else:
            return "✅ Crop health is stable."

    def get_status_report(self):
        # Return a status report with current health and alert
        return {"crop_health": self.crop.get_health(), "alert": self.check_health_status()}
