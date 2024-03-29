def solution(A, D):
    total_income = 0
    total_fees = {}  # Store total fees for each month

    # loop through the transaction to calculate the income and fees
    for amount, date in zip(A, D):
        year, month, _ = map(int, date.split('-'))
        total_income += amount

        # checks if transaction is a card payment
        if amount < 0:
            # Check if the key exists, if not, initialize it
            if (year, month) not in total_fees:
                total_fees[(year, month)] = abs(amount)
            else:
                total_fees[(year, month)] += abs(amount)

    total_fees_amount = 0
    # calculates the total to be deducted every month
    for month, fee in total_fees.items():
        if fee < 10:
            total_fees_amount += 5

    # Returns the final balance after deducting fees from income
    return total_income - total_fees_amount

# Test cases
print(solution([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]))  # Output: 230
print(solution([180, -50, -25, -25], ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"]))  # Output: 25
print(solution([1, -1, 0, -105, 1], ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"]))  # Output: -164
print(solution([100, 100, -10, -20, -30], ["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"]))  # Output: 80
print(solution([-60, 60, -40, -20], ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"]))# Output: -115
