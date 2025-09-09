'''
7. Taxi Fare Calculation

Scenario:

A taxi service calculates fares based on the following rates: 

- **Base fare**: $50 

- **Distance fare**: $10/km 

Write a program to calculate the total fare for multiple trips.

Requirements:

- Use a function to calculate fare for each trip.

Input Example:

```python

trips = [5, 10, 3]  # Distances in km

```

Expected Output:

```

Trip 1: $100

Trip 2: $150

Trip 3: $80

Total Fare: $330

```

'''

def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    return base_fare + distance_fare

trips = list(map(int, input("Enter Distance in km separated by commas: ").split(',')))

total_fare = 0

for i, distance in enumerate(trips, start=1):
    fare = calculate_fare(distance)
    print(f"Trip {i}: ${fare}")
    total_fare += fare

print(f"\nTotal Fare: ${total_fare}")
