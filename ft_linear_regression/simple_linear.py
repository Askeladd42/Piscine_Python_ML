def estimate_price(mileage, theta0, theta1):
    """Formula to estimate the price of a car given its mileage"""
    return theta0 + (theta1 * mileage)


def main():
    """Program making the prediction"""
    # Initialize theta0 and theta1 to 0
    theta0 = 0
    theta1 = 0

    mileage = float(input("Enter the mileage of the car: "))

    # Estimation of the price of the car
    estimated_price = estimate_price(mileage, theta0, theta1)
    print(f"Estimated price: {estimated_price}")


if __name__ == "__main__":
    main()
