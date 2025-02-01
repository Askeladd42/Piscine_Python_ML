import matplotlib.pyplot as plt
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

        # Plot the life expectancy over time for the country of your campus
        country = input("Please enter the country you are looking for: ")
        if country in data['country'].values:
            country_data = data.set_index('country').transpose()
            plt.plot(country_data.index, country_data[country], label=country)
            plt.xlabel("Year")
            plt.ylabel("Life expectancy")
            plt.title(f"{country} Life expectancy Projections")
            plt.legend()
            plt.show()
        else:
            print(f"Country {country}' not found in the dataset.")
    else:
        print("An error occurred while loading the dataset.")


if __name__ == "__main__":
    main()
