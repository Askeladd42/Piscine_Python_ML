import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def estimate_price(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)


def load_data(file_path):
    data = np.loadtxt(file_path, delimiter=',', skiprows=1)
    mileage = data[:, 0]
    price = data[:, 1]
    return mileage, price


def train_model(mileage, price, learning_rate=0.01, iterations=1000):
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
    with open(file_path, 'w') as f:
        f.write(f"{theta0},{theta1}")


def plot_results(mileage, price, theta0, theta1):
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


def main():
    mileage, price = load_data('data.csv')
    theta0, theta1 = train_model(mileage, price)
    save_model(theta0, theta1, 'model.txt')
    print(f"Model trained with theta0: {theta0}, theta1: {theta1}")
    plot_results(mileage, price, theta0, theta1)


if __name__ == "__main__":
    main()
