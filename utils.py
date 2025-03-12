def format_conditions(conditions):
    """
    Format environmental conditions for display.
    """
    return f"Temperature: {conditions['temperature']:.2f} °C, " \
           f"Humidity: {conditions['humidity']:.2f} %, " \
           f"Pest Level: {conditions['pest_level']}"

def validate_data(data):
    """
    Validate data input (placeholder for potential data validation logic).
    """
    return True
