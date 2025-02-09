import matplotlib.pyplot as plt
from load_csv import load


def main():
    # Load the datasets
    gdp_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy_data = load("life_expectancy_years.csv")

    if gdp_data is not None and life_expectancy_data is not None:
        # Filter the data for the year 1900
        gdp_1900 = gdp_data[['country', '1900']]
        life_expectancy_1900 = life_expectancy_data[['country', '1900']]

        # Merge the datasets on the country column
        merged_data = gdp_1900.merge(life_expectancy_1900, on='country',
                                     suffixes=('_gdp', '_life_expectancy'))

        # Plot the data
        plt.scatter(merged_data['1900_gdp'],
                    merged_data['1900_life_expectancy'])
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy ")
        plt.title("1900")
        # plt.legend(["Countries"])
        plt.show()
    else:
        print("An error occurred while loading the datasets.")


if __name__ == "__main__":
    main()
