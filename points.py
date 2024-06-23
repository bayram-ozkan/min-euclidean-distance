#Random points generator
import random

def generateRandomPoints(num_points, range_min, range_max):
    points = []
    for _ in range(num_points):
        x = random.randint(range_min, range_max)
        y = random.randint(range_min, range_max)
        points.append((x, y))
    return points

#10 points create and 0 to 10 
points = generateRandomPoints(10, 0, 10)

with open('points.txt', 'w') as file:
    for point in points:
        file.write(f"{point[0]}, {point[1]}\n")

    
