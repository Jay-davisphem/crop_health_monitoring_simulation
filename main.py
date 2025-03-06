import simpy
from simulation import Simulation
import config

if __name__ == "__main__":
    # Create the SimPy environment
    env = simpy.Environment()
    # Instantiate the Simulation
    simulation = Simulation(env)
    # Start the simulation process
    env.process(simulation.run())
    # Run the simulation for a specified duration (e.g., 50 time units)
    env.run(until=config.SIMULATION_DURATION)
