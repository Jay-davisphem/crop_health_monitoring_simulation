import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualization:
    def plot_data(self, data_file):
        # Read CSV file
        df = pd.read_csv(data_file)

        # Set Seaborn style for better aesthetics
        sns.set_style("whitegrid")

        # Scatter plot: Crop Health vs Temperature
        plt.figure(figsize=(6, 4))
        sns.scatterplot(x=df["temperature"], y=df["crop_health"], color='red')
        plt.xlabel("Temperature (°C)")
        plt.ylabel("Crop Health")
        plt.title("Effect of Temperature on Crop Health")
        plt.savefig("crop_health_vs_temperature.png")
        plt.close()

        # Scatter plot: Crop Health vs Humidity
        plt.figure(figsize=(6, 4))
        sns.scatterplot(x=df["humidity"], y=df["crop_health"], color='blue')
        plt.xlabel("Humidity (%)")
        plt.ylabel("Crop Health")
        plt.title("Effect of Humidity on Crop Health")
        plt.savefig("crop_health_vs_humidity.png")
        plt.close()

        # Scatter plot: Crop Health vs Pest Level
        plt.figure(figsize=(6, 4))
        sns.scatterplot(x=df["pest_level"], y=df["crop_health"], color='green')
        plt.xlabel("Pest Level")
        plt.ylabel("Crop Health")
        plt.title("Effect of Pest Level on Crop Health")
        plt.savefig("crop_health_vs_pest_level.png")
        plt.close()

        print("Plots saved: crop_health_vs_temperature.png, crop_health_vs_humidity.png, crop_health_vs_pest_level.png")

    def plot_pairplot(self, data_file):
        df = pd.read_csv(data_file)
        sns.pairplot(df, diag_kind="kde", plot_kws={"alpha": 0.5})
        plt.savefig("crop_health_pairplot.png")
        print("Pairplot saved as crop_health_pairplot.png")
