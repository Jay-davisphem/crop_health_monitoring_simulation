class MonitoringSystem:
    def __init__(self, crop):
        """
        Initialize the monitoring system with a Crop object.
        :param crop: Instance of Crop.
        """
        self.crop = crop

    def check_health_status(self):
        """
        Check crop health and return a status message.
        TODO: Return a warning if health is below a critical threshold, otherwise indicate stability.
        """
        pass

    def get_status_report(self):
        """
        Get a report of current crop health and alert status.
        TODO: Return a dictionary with 'crop_health' and 'alert' status.
        """
        pass
