# Simulation parameters
SIMULATION_DURATION = 500  # Total simulation time in time units
UPDATE_INTERVAL = 1       # Time step interval

# Crop initial health
HEALTHY = 100

# Initial environmental conditions
INITIAL_TEMPERATURE = 30
INITIAL_HUMIDITY = 60
INITIAL_PEST_LEVEL = 2

# Temperature thresholds and adjustments
TEMP_LOW_THRESHOLD = 15         # Below this, crop suffers
TEMP_HIGH_THRESHOLD = 35        # Above this, crop suffers
OPTIMAL_TEMP_LOW = 20           # Lower bound of optimal temperature
OPTIMAL_TEMP_HIGH = 30          # Upper bound of optimal temperature
TEMP_PENALTY = 5                # Health penalty for stress conditions
TEMP_BONUS = 2                  # Health bonus for optimal conditions

# Humidity thresholds and adjustments
HUMIDITY_LOW_THRESHOLD = 30     # Below this, crop suffers
HUMIDITY_HIGH_THRESHOLD = 70    # Above this, crop suffers
OPTIMAL_HUMIDITY_LOW = 40       # Lower bound of optimal humidity
OPTIMAL_HUMIDITY_HIGH = 65      # Upper bound of optimal humidity
HUMIDITY_PENALTY = 3            # Health penalty for humidity stress
HUMIDITY_BONUS = 2              # Health bonus for optimal humidity

# Pest level thresholds and adjustments
PEST_THRESHOLD = 7              # Above this level, crop suffers
PEST_PENALTY = 10               # Health penalty for high pest level

# Fluctuation ranges for environmental conditions
TEMP_FLUCTUATION_MIN = -2
TEMP_FLUCTUATION_MAX = 2
HUMIDITY_FLUCTUATION_MIN = -5
HUMIDITY_FLUCTUATION_MAX = 5
PEST_LEVEL_FLUCTUATIONS = [-1, 0, 1]