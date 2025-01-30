import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load

def main():
    data = load("life_expectancy_years.csv")
    if data is not None:
        # Print the first few rows of the dataset
        print(data.head())

        # Print the last few rows of the dataset
        print(data.tail())

        # Print the columns of the dataset
        print(data.columns)

        # Print the shape of the dataset
        print(data.shape)

        # Print the data types of the columns
        print(data.dtypes)

        # Print the summary statistics of the dataset
        print(data.describe())

        # Plot the life expectancy over time
        plt.plot(data["France"], data["1800":])
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.title("Life expectancy over time")
        plt.show()
    else:
        print("An error occurred while loading the dataset.")


if __name__ == "__main__":
    main()