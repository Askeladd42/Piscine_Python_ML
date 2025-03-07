import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def estimate_price(mileage, theta0, theta1):
    """Formula to estimate the price of a car given its mileage"""
    return theta0 + (theta1 * mileage)


def load_data(file_path):
    """Load the data from the csv file"""
    data = pd.read_csv(file_path)
    mileage = data['km'].values
    price = data['price'].values
    return mileage, price


def normalize_data(data):
    """Normalize the data"""
    return (data - np.mean(data)) / np.std(data)


def train_model(mileage, price, learning_rate=0.01, iterations=1000):
    """Train the model to find the best theta0 and theta1"""
    m = len(mileage)
    theta0 = 0
    theta1 = 0

    for _ in range(iterations):
        error = estimate_price(mileage, theta0, theta1) - price
        tmp_theta0 = theta0 - learning_rate * (1/m) * np.sum(error)
        tmp_theta1 = theta1 - learning_rate * (1/m) * np.sum(error * mileage)
        theta0, theta1 = tmp_theta0, tmp_theta1

    return theta0, theta1


def save_model(theta0, theta1, file_path):
    """Save the model to a file"""
    with open(file_path, 'w') as f:
        f.write(f"{theta0},{theta1}")


def plot_results(mileage, price, theta0, theta1):
    """Plot the data points and the regression line"""
    plt.scatter(mileage, price, color='blue', label='Data points')
    plt.plot(
        mileage, estimate_price(mileage, theta0, theta1),
        color='red', label='Regression line'
          )
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.title('Linear Regression: Mileage vs Price')
    plt.legend()
    plt.show()


def calculate_precision(mileage, price, theta0, theta1):
    """Calculate the mean squared error of the model"""
    predictions = estimate_price(mileage, theta0, theta1)
    mse = np.mean((predictions - price) ** 2)
    return mse


def main():
    """Main function of the program"""
    mileage, price = load_data('data.csv')
    mileage = normalize_data(mileage)
    price = normalize_data(price)
    theta0, theta1 = train_model(mileage, price)
    save_model(theta0, theta1, 'model.txt')
    print(f"Model trained with theta0: {theta0}, theta1: {theta1}")
    plot_results(mileage, price, theta0, theta1)
    mse = calculate_precision(mileage, price, theta0, theta1)
    print(f"Mean Squared Error of the model: {mse}")


if __name__ == "__main__":
    main()
