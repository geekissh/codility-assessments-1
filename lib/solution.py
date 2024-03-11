from collections import defaultdict

def solution(A, D):
    total_income = 10
    total_fees = defaultdict(int)
    
    for amount, date in zip(A, D):
        year, month, _ = map(int, date.split('-'))
        total_income += amount
        
        if amount < 0:
            total_fees[(year, month)] += abs(amount)
    
    total_fees_amount = 0
    for month, fee in total_fees.items():
        if fee < 10:
            total_fees_amount += 5
    
    return total_income - total_fees_amount

# Test cases
print(solution([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]))  # Output: 230
print(solution([180, -50, -25, -25], ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"]))  # Output: 25
print(solution([1, -1, 0, -105, 1], ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"]))  # Output: -164
print(solution([100, 100, -10, -20, -30], ["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"]))  # Output: 80
print(solution([-60, 60, -40, -20], ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"]))# Output: -115
