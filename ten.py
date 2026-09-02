# To input the value of X and n and print the sum of the series 1 + X + X^2 + X^3 + ....+ X^n 
X = int(input("Enter the base (X): "))
n = int(input("Enter the exponent (n): "))

sum_series = 0
for i in range(n + 1):
    sum_series += X ** i

print("The sum of the series is:", sum_series)
