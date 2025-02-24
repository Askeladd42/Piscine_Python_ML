import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from load_csv import load


def millions(x, pos):
    """The two args are the value and tick position."""
    return '%1.0fM' % (x * 1e-6)


def main():
    """Program for the graphs display."""
    data = load("population_total.csv")
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

        # Plot the population over time for the country of your campus and another country
        campus_country = input("Please enter the country of your campus: ")
        other_country = input("Please enter another country of your choice: ")

        if campus_country in data['country'].values and other_country in data['country'].values:
            country_data = data.set_index('country').transpose()
            country_data.index = country_data.index.astype(int)

            plt.plot(country_data.index, country_data[campus_country], label=campus_country)
            plt.plot(country_data.index, country_data[other_country], label=other_country)

            plt.xlabel("Year")
            plt.ylabel("Population")
            plt.title("Population Projections")
            plt.legend()

            # Set x-axis ticks to be every 40 years from 1800 to 2050
            plt.xticks(range(1800, 2051, 40), rotation=45)
            plt.xlim(1800, 2050)

            # Set y-axis ticks to be every 20 million
            max_population = max(country_data[campus_country].max(), country_data[other_country].max())
            plt.yticks(range(0, int(max_population) + 20000000, 20000000))

            # Format y-axis labels to show in millions
            formatter = FuncFormatter(millions)
            plt.gca().yaxis.set_major_formatter(formatter)

            plt.show()
        else:
            if campus_country not in data['country'].values:
                print(f"Country '{campus_country}' not found in the dataset.")
            if other_country not in data['country'].values:
                print(f"Country '{other_country}' not found in the dataset.")
    else:
        print("An error occurred while loading the dataset.")


if __name__ == "__main__":
    main()
