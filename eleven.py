# Write a program to compute distance between two points taking input from users
x1 = float(input("Enter x-coordinate of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 # formula to calculation the distance between two points 
print("The distance between the two points is:", distance)

