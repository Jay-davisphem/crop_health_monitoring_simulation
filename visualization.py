import pandas as pd
import matplotlib.pyplot as plt

class DataVisualization:
    def plot_data(self, data_file):
        # Read simulation data and plot crop health over time
        df = pd.read_csv(data_file)
        plt.plot(df.index, df["crop_health"], label="Crop Health")
        plt.xlabel("Time")
        plt.ylabel("Crop Health")
        plt.title("Crop Health Over Time")
        plt.legend()
        plt.show()
