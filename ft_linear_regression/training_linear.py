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


def train_model(mileage, price, learning_rate, iterations):
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


# Converts normalized thetas to real-world thetas
def denormalize_thetas(theta0_norm, theta1_norm, mileage_mean, mileage_std,
                       price_mean, price_std):
    theta1_real = theta1_norm * (price_std / mileage_std)
    theta0_real = (
        price_mean + price_std * theta0_norm
        - theta1_real * mileage_mean
    )
    return theta0_real, theta1_real


def main():
    """Main function to execute the training process"""
    # Load data
    mileage, price = load_data('data.csv')
    mileage_mean, mileage_std = np.mean(mileage), np.std(mileage)
    price_mean, price_std = np.mean(price), np.std(price)

    mileage_norm = normalize_data(mileage)
    price_norm = normalize_data(price)

    theta0, theta1 = train_model(mileage_norm, price_norm, 0.01, 10000)
    save_model(theta0, theta1, 'model.txt')
    # Save normalization parameters for later use
    with open('norm_params.txt', 'w') as f:
        f.write(f"{mileage_mean},{mileage_std},{price_mean},{price_std}")

    print(f"Model trained with normalized theta0: {theta0}, theta1: {theta1}")
    mse = calculate_precision(mileage_norm, price_norm, theta0, theta1)
    print(f"Mean Squared Error of the model: {mse}")

    # Denormalize thetas for real-world predictions
    theta0_real, theta1_real = denormalize_thetas(
        theta0,
        theta1,
        mileage_mean,
        mileage_std,
        price_mean,
        price_std
    )
    print(
        f"Denormalized thetas: theta0 = {theta0_real}, "
        f"theta1 = {theta1_real}"
    )

    # Save real thetas for use in prediction
    save_model(theta0_real, theta1_real, 'model.txt')

    # Plot regression on original data
    plot_results(mileage, price, theta0_real, theta1_real)


if __name__ == "__main__":
    main()
